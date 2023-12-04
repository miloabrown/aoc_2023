"""
Advent Of Code 2023
Code written by Milo
Day4: Scratchcards
"""
import re  # For splitting the input.
from collections import defaultdict  # For counting the cards.

# Deal with input.
with open("day_4/input.txt", "r") as file:
    data = list([int(id[1]),win,card] for id, win, card in
                map(lambda x: [column.split() for column in x],
                [re.split(': | \| ',row) for row in file.read().splitlines()]))

def matches(tic):
    """
    Helper function to count the number of matches in a ticket.
    """
    return len(list(filter(lambda x: x in tic[1], tic[2])))

def part1():
    """
    PART1
    Find the score for the pile of cards.
    First index: winning numbers
    Second index: numbers on the card

    Score: 1 for first match and doubled for each match after that.

    Answer for part1: 26218
    """

    return sum(map
               (lambda x: 2**(x-1) , filter
                (lambda z: z > 0, map
                 (matches, data)))
            )

def part2():
    """
    PART2
    Each winning card wins copies of the next cards,
    according to the number of matches.

    Answer for part2:
    """

    cards_won = defaultdict(int)

    for id,row in enumerate(data):
        cards_won[id] += 1
        for match_id in range(matches(row)):
            cards_won[id+1+match_id] += cards_won[id]

    return(sum(cards_won.values()))

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()