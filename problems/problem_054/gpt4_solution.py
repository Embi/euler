import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def parse_hand(hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        cards = hand.split()
        card_values = sorted([values[card[0]] for card in cards], reverse=True)
        card_suits = [card[1] for card in cards]
        return card_values, card_suits

    def hand_rank(values, suits):
        is_flush = len(set(suits)) == 1
        is_straight = all(values[i] - 1 == values[i + 1] for i in range(4))
        value_counts = {v: values.count(v) for v in set(values)}
        counts = sorted(value_counts.values(), reverse=True)
        unique_values = sorted(value_counts.keys(), reverse=True)

        if is_straight and is_flush:
            if values[0] == 14:
                return (9, values)  # Royal Flush
            return (8, values)  # Straight Flush
        if counts == [4, 1]:
            return (7, unique_values)  # Four of a Kind
        if counts == [3, 2]:
            return (6, unique_values)  # Full House
        if is_flush:
            return (5, values)  # Flush
        if is_straight:
            return (4, values)  # Straight
        if counts == [3, 1, 1]:
            return (3, unique_values)  # Three of a Kind
        if counts == [2, 2, 1]:
            return (2, unique_values)  # Two Pairs
        if counts == [2, 1, 1, 1]:
            return (1, unique_values)  # One Pair
        return (0, values)  # High Card

    def compare_hands(hand1, hand2):
        values1, suits1 = parse_hand(hand1)
        values2, suits2 = parse_hand(hand2)
        rank1 = hand_rank(values1, suits1)
        rank2 = hand_rank(values2, suits2)
        return rank1 > rank2

    player1_wins = 0
    with open('p054_poker.txt', 'r') as file:
        for line in file:
            cards = line.strip()
            player1_hand = cards[:14]
            player2_hand = cards[15:]
            if compare_hands(player1_hand, player2_hand):
                player1_wins += 1

    return player1_wins
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))