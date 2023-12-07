"""
Advent Of Code 2023
Code written by Milo
Day7: Camel Cards
"""
from collections import Counter

# Deal with input.
with open("day_7/input.txt", "r") as file:
    cards,bets = zip(*[line.strip().split() for line in file.readlines()])

CARDS1, CARDS2 = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}, {"T": 10, "J": 00, "Q": 12, "K": 13, "A": 14}
hands1, hands2 = [(tuple(int(CARDS1.get(card, card)) for card in cards), int(bid)) for cards, bid in zip(cards, bets)],\
                [(tuple(int(CARDS2.get(card, card)) for card in cards), int(bid)) for cards, bid in zip(cards, bets)]

VALUES = {
    ((5,), 0): 6,   # 5 of a kind
    ((4,), 1): 6,   # 4 of a kind + joker
    ((4,), 0): 5,   # 4 of a kind
    ((2,3), 0): 4,  # Full house
    ((3,), 2): 6,   # 3 of a kind + 2 jokers
    ((3,), 1): 5,   # 3 of a kind + 1 joker
    ((3,), 0): 3,   # 3 of a kind
    ((2,2), 1): 4,  # 2 pairs + 1 joker
    ((2,2), 0): 2,  # 2 pairs
    ((2,), 3): 6,   # 1 pair + 3 jokers
    ((2,), 2): 5,   # 1 pair + 2 jokers
    ((2,), 1): 3,   # 1 pair + 1 joker
    ((2,), 0): 1,   # 1 pair
    ((), 5): 6,     # 5 jokers
    ((), 4): 6,     # 4 jokers
    ((), 3): 5,     # 3 jokers
    ((), 2): 3,     # 2 jokers
    ((), 1): 1,     # 1 joker
    ((), 0): 0,     # No jokers
}

def hand_strength(hand):
    """
    Calculate the value of a hand.
    The value is determined by the hand type
    and the number of jokers in the hand.
    """
    cards = Counter(card for card in hand if card)
    count = tuple(card for card in sorted(cards.values()) if card >1)
    joker = hand.count(0)
    return VALUES[count, joker]

def solve(hands):
    hands = [(hand_strength(hand), hand, bet) for hand, bet in hands]
    return sum(rank * bet for rank, (_, _, bet) in enumerate(sorted(hands), 1))

def part1():
    """
    PART1

    Answer for part1: 253910319
    """
    return solve(hands1)

def part2():
    """
    PART2

    Answer for part2: 254083736
    """
    return solve(hands2)


def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()