import json
import time
from typing import List, Tuple
from itertools import groupby

_CARD_HEX_VALUES = {str(i): str(i) for i in range(2, 10)}
_CARD_HEX_VALUES.update({'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'})

def values_to_hex(cards: Tuple[str]):
    """Translate all card values to hexadecimal numbers"""
    return [f"{_CARD_HEX_VALUES[card[0]]}{card[1]}" for card in cards]

def by_suit(hand: List[str]) -> List[Tuple[str, Tuple[int]]]:
    hand = sorted(hand, key=lambda card: card[1])
    return [(k, tuple(g)) for k, g in groupby(hand, lambda x: x[1])]

def by_value(hand: List[str]) -> List[Tuple[str, Tuple[int]]]:
    hand = sorted(hand, key=lambda card: card[0])
    return [(k, tuple(g)) for k, g in groupby(hand, lambda x: x[0])]

def get_values(cards: List[str]) -> List[str]:
    return [card[0] for card in cards]

def get_suits(cards: List[str]) -> List[str]:
    return [card[1] for card in cards]

def are_consecutive(values: List[str]) -> bool:
    for i in range(1, len(values)):
        if int(values[i], 16) - int(values[i-1], 16) != 1:
            return False
    return True

def eval_high(hand: List[str]) -> Tuple[str, str]:
    shift = '0' * (5 - len(hand))
    values = sorted(get_values(hand), reverse=True)
    return [], ''.join(values) + shift

def eval_pairs(hand: List[str]) -> Tuple[str, str]:
    shift = '0' * 5
    pairs = filter(lambda x: len(x[1]) == 2, by_value(hand))
    values = []
    for value, cards in pairs:
        values += value
        for card in cards:
            hand.remove(card)
    values.sort(reverse=True)
    return hand, ''.join(values).zfill(2) + shift

def eval_three_of_a_kind(hand: List[str]) -> Tuple[str, str]:
    shift = '0' * 7
    values = {len(b): a for a, b in by_value(hand)}
    values = by_value(hand)
    for value, cards in values:
        if len(cards) == 3:
            for card in cards:
                hand.remove(card)
            return hand, value + shift
    return hand, '0' + shift

def eval_straight(hand: List[str]) -> Tuple[List[str], str]:
    shift = '0' * 8
    values = sorted(get_values(hand))
    if len(values) == 5 and are_consecutive(values):
        values = get_values(hand)
        return [], values[-1] + shift
    return hand, '0' + shift

def eval_flush(hand: List[str]) -> Tuple[List[str], str]:
    shift = '0' * 9
    suits = by_suit(hand)
    if len(suits) == 1 and len(hand) == 5:
        values = get_values(hand)
        return [], ''.join(values) + shift
    return hand, '00000' + shift

def eval_full_house(hand: List[str]) -> Tuple[List[str], str]:
    shift = '0' * 14
    values = {len(b): a for a, b in by_value(hand)}
    if sorted(values.keys()) == [2,3]:
        return [], f'{values[3]}{values[2]}' + shift
    return hand, '00' + shift

def eval_four_of_a_kind(hand: List[str]) -> Tuple[List[str], str]:
    shift = '0' * 16
    values = by_value(hand)
    for value, cards in by_value(hand):
        if len(cards) == 4:
            for card in cards:
                hand.remove(card)
            return hand, value + shift
    return hand, '0' + shift

def eval_straight_flush(hand: List[str]) -> Tuple[List[str], str]:
    shift = '0' * 17
    suits = by_suit(hand)
    if len(suits) == 1 and are_consecutive(get_values(suits[0][1])):
        suit, values = suits[0]
        return [], values[-1] + shift
    return hand, '0' + shift

EVAL_ORDER = (
    eval_straight_flush,
    eval_four_of_a_kind,
    eval_full_house,
    eval_flush,
    eval_straight,
    eval_three_of_a_kind,
    eval_pairs,
    eval_high,
)

def hand_eval(hand) -> int:
    """Create a hexadecimal evaluation of a hand
    high -> XXXXX (every X represents one card, descending order)
    pairs -> XX00000 (every X represents card value in a pair, desceding order)
    three -> X0000000 (X represents highest card value)
    straight -> X00000000 (X represents highest value)
    flush -> XXXXX000000000 (every X represents one card in the flus,
    descending order)
    full house -> XX00000000000000 (first x is value of three and second value
    of pair)
    four of a kind -> X0000000000000000 (X card value)
    straight flush (including royal) -> X00000000000000000 (X highest value in
    the flush)
    """
    evaluation = 0
    for eval_func in EVAL_ORDER:
        hand, _evalualtion = eval_func(hand)
        evaluation += int(_evalualtion, 16)
    return evaluation

def load_hands():
    with open('p054_poker.txt', 'r') as f:
        hands = f.read().strip().split('\n')
        return [values_to_hex(cards.split(' ')) for cards in hands]

def solution() -> int:
    hands = load_hands()
    p1_wins = 0
    for hand in hands:
        p1, p2 = hand_eval(hand[:5]), hand_eval(hand[5:])
        p1_wins += p1 > p2
    return p1_wins

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
