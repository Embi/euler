#!/usr/bin/env python
"""
Script for managing all life-cycle around project euler problems:
    - download problem
    - prepare boilerplate solution files
    - execute solutions and collect stats
    - promt GPT for a solution

Usage:
  euler solve <problem_id> [<language>]
  euler gpt <problem_id>
  euler run <problem_id>
  euler run-gpt <problem_id>
  euler stats
"""

import os
import subprocess
import shutil
import json
import openai
import pandas as pd
from jinja2 import Template
from typing import List
from docopt import docopt
from pathlib import Path

openai.organization = os.getenv('OPENAI_ORG')
openai.api_key = os.getenv('OPENAI_KEY')

_EULER_DIR = Path(Path.home(), 'projects/euler')
_PROBLEMS_DIR = _EULER_DIR / 'problems'
_TEMPL_DIR = _EULER_DIR / 'templates'
_LANGUAGES = ('py', 'cpp', 'hs')


class Problem():

    def __init__(self, problem_id: int):
        self.problem_id = problem_id
        self.problem_dir = _PROBLEMS_DIR / f'problem_{problem_id:03}'
        self.metadata_file = self.problem_dir / 'metadata.json'
        self.readme_file = self.problem_dir / 'readme.md'
        self.__init_problem()

    def solve(self, language: str = 'py'):
        assert language in _LANGUAGES
        solution_file_name = f'solution.{language}'
        if solution_file_name not in self.solution_files():
            self.__copy_template(f'solution.{language}')
        self.__open_in_brave()
        self.__open_in_vim(language)
        self.run()

    def solve_gpt(self):
        """Prompt ChatGPT to solve the problem in python
        """
        with self.readme_file.open() as f:
            readme = f.read()

        prompt = (f"Solve the following problem in Python and make the"
                  f"solution accessible via an argument-less function called"
                  f"'solution'. The result returned by the 'solution' function"
                  f"must be an integer value. Also the solution should be as"
                  f"fast as possible. Here is the problem: {readme}")
        kwargs = {
            'model': "gpt-3.5-turbo",
            'temperature': 0,
            'messages': [{"role": "user", "content": prompt}],
        }
        try:
            response = openai.ChatCompletion.create(**kwargs)
            solution = response['choices'][0]['message']['content']
        except Exception as e:
            print("Unable to generate solution", e.args)
            return

        render_template(
            template='gpt_solution.py.j2',
            dst=self.problem_dir / 'gpt_solution.py',
            params={'solution': solution},
            overwrite=True
        )
        self.__open_in_vim('py', 'gpt_')
        self.run(gpt_generated=True)

    def generate_tags(self) -> str:
        """Prompt ChatGPT to generate tags that describe the problem.
        """
        with self.readme_file.open() as f:
            readme = f.read()

        prompt = (f"Create two tags (every tag has to consist of exactly one "
                  f"word and be prefixed by a hash character - separate the "
                  f"tags by one space; never use a newline) that describe the nature "
                  f"of the following problem : {readme}")
        kwargs = {
            'model': "gpt-3.5-turbo",
            'temperature': 0,
            'messages': [{"role": "user", "content": prompt}],
        }
        try:
            response = openai.ChatCompletion.create(**kwargs)
            # tags are in the following form: '#Multiples #Summation'
            # transform them to '`#Multiples` `#Summation`'
            tags = response['choices'][0]['message']['content']
            tags = ' '.join(map(lambda x: f"`{x}`", tags.split(" ")))
        except Exception as e:
            print("Unable to generate tags", e.args)
            tags = ''
        self.update_metadata({'tags': tags})
        return tags

    def run(self, language: str = 'py', gpt_generated: bool = False):
        """Run a solution and collect results and stats"""
        assert language in _LANGUAGES
        prefix = 'gpt_' if gpt_generated else ''
        if language == 'py':
            result = self.__execute(['python', f'{prefix}solution.py'], capture_output=True)
            result = json.loads(result)
        if self.check_result(result):
            update = {
                'solution': result['solution'],
                f'{prefix}{language}': {
                    'cpu': result['cpu'],
                    'wall': result['wall'],
                }
            }
        else:
            update = {f'{prefix}{language}': "Failed"}
        self.update_metadata(update)

    def check_result(self, result: dict) -> bool:
        with self.metadata_file.open() as s:
            metadata = json.load(s)
        if metadata['solution'] == None:
            print(result)
            answer = input("Is this result right (y/n)?")
            result['right'] = True if answer == 'y' else False
        else:
            result['right'] = metadata['solution'] == result['solution']
            result['right_solution'] = metadata['solution']
            print(result)
        return result['right']

    def update_metadata(self, update: dict):
        metadata = self.get_metadata()
        metadata.update(update)
        _dump_json(metadata, self.metadata_file)

    def get_metadata(self) -> dict:
        return _load_json(self.metadata_file)

    def solution_files(self):
        return list(map(
            lambda x: x.name, self.problem_dir.glob('solution*')))

    def readme_files(self):
        return list(map(
            lambda x: x.name, self.problem_dir.glob('readme*')))

    def __init_problem(self):
        try:
            self.problem_dir.mkdir()
        except FileExistsError:
            pass
        self.__create_readme()
        self.__create_metadata()

    def __create_metadata(self):
        self.__copy_template('metadata.json')
        meta = self.get_metadata()
        if meta.get('id') and meta.get('tags'):
            return
        self.update_metadata({'id': self.problem_id})
        self.generate_tags()

    def __create_readme(self):
        readme_files = self.readme_files()
        if 'readme.md' in readme_files and 'readme.html' in readme_files:
            return

        self.__execute([
            'pandoc', '-f', 'html+tex_math_dollars', '--mathml',
            '--extract-media=assets', '-t', 'html',
            f'https://projecteuler.net/minimal={self.problem_id}',
            '-o', 'readme.html'
        ])
        self.__execute([
            'wget', '-q', '--force-html', '-p', '-nd',
            '--base', 'https://projecteuler.net/', '-i',  'readme.html'
        ], False)
        self.__execute([
            'pandoc', '-f', 'html+tex_math_dollars',
            '--extract-media=assets', '-t', 'gfm',
            f'https://projecteuler.net/minimal={self.problem_id}',
            '-o', 'readme.md'
        ])

    def __open_in_brave(self):
        self.__execute(
            ['brave', f'https://projecteuler.net/problem={self.problem_id}'],
            check=False
        )

    def __open_in_vim(self, language: str, prefix: str = ''):
        self.__execute(
            ['vim', '-o', f'{prefix}solution.{language}', 'readme.md'],
            check=False
        )

    def __execute(self, command: List[str], check: bool = True,
                  capture_output: bool = False) -> bytes:
        try:
            result = subprocess.run(command, check=check,
                                    capture_output=capture_output,
                                    cwd=self.problem_dir)
            return result.stdout
        except subprocess.CalledProcessError as e:
            cmd_string = ' '.join(command)
            print(f'error while running {cmd_string}: {e.stderr}')
            raise e

    def __copy_template(self, template_name: str):
        template = _TEMPL_DIR / template_name
        destination = self.problem_dir / template_name
        assert template.exists()
        if not destination.exists():
            shutil.copy(template, self.problem_dir)


def update_readme_stats():
    """Update global readme with problem stats.
    """
    def _meta_to_pandas_row(problem_dir: Path):
        metadata_file = problem_dir / 'metadata.json'
        metadata = _load_json(metadata_file)
        if metadata.pop('solution') is None:
            return {}

        _id = metadata.pop('id')
        problem_dir = f'problems/problem_{_id:03}'
        solution_file = '{problem_dir}/{prefix}solution.{lang}'
        row = {
            'id': f'[{_id}]({problem_dir})',
            'tags': metadata.pop('tags'),
        }
        for lang, meta in metadata.items():
            _solution_file = solution_file.format(
                prefix='gpt_' if 'gpt_' in lang else '',
                lang=lang.removeprefix('gpt_'),
                problem_dir=problem_dir
            )
            if 'wall' in meta:
                row[lang] = (
                    f'[{meta["wall"]:.3f}s]({_solution_file})({meta["cpu"]:.3f}s)')
            else:
                row[lang] = f'[{meta}]({_solution_file})'
        return row

    problem_dirs = sorted(list(_PROBLEMS_DIR.glob('problem_*')))
    df = pd.DataFrame([_meta_to_pandas_row(d) for d in problem_dirs])
    df.dropna(how='all',inplace=True)
    df.fillna('',inplace=True)
    render_template(
        template='readme.md.j2',
        dst=_EULER_DIR / 'README.md',
        params={'stats': df.to_markdown(index=False)},
        overwrite=True
    )


def render_template(template: str, dst: Path, params: dict,
                    overwrite: bool = False):
    if not dst.exists() or overwrite:
        template_file = _TEMPL_DIR / template
        assert template_file.exists()
        with template_file.open() as f:
            template = Template(f.read())
        content = template.render(**params)
        with dst.open('w') as f:
            template = f.write(content)


def _load_json(path: Path) -> dict:
    with open(path, 'r') as j:
        return json.load(j)

def _dump_json(content: dict, path: Path) -> dict:
    with open(path, 'w') as j:
        json.dump(content, j)


if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['stats']:
        update_readme_stats()
        exit(0)

    language = arguments['<language>']
    if language is None:
        language = 'py'

    problem = Problem(int(arguments['<problem_id>']))
    if arguments['solve']:
        problem.solve(language)
    if arguments['gpt']:
        problem.solve_gpt()
    if arguments['run']:
        problem.run()
    if arguments['run-gpt']:
        problem.run(gpt_generated=True)
