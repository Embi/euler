import json
import time
from itertools import cycle, starmap
from typing import List, Iterator

def decrypt(message: List[int], key: List[int]) -> List[int]:
    """Decrypt ascii chars using the given key"""
    key_char = cycle(key)
    for enc_ascii_code in message:
        dec_ascii_code = enc_ascii_code ^ next(key_char)
        yield dec_ascii_code

def decode(message: List[int]) -> str:
    """Decode from ascii to plaintext"""
    return ''.join([chr(i) for i in message])

def load_message() -> List[int]:
    with open('p059_cipher.txt', 'r') as f:
        return [int(i) for i in f.read().strip().split(',')]

def solution() -> int:
    m = load_message()
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                decrypted = list(decrypt(m, [i,j,k]))
                plain = decode(decrypted)
                if " the " in plain:
                    return sum(decrypted)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
