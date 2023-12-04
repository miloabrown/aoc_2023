"""
Advent Of Code 2023
Code written by Milo
Day4: Scratchcards
"""
import re  # For splitting the input.

# Deal with input.
with open("day_4/input.txt", "r") as file:
    data = list(map(lambda x: [column.split() for column in x],
                [re.split(': | \| ',row)[1:] for row in file.read().splitlines()]))

def part1():
    """
    PART1
    Find the score for the pile of cards.
    First index: winning numbers
    Second index: numbers on the card

    Score: 1 for first match and doubled for each match after that.

    Answer for part1:
    """

    return sum(map
               (lambda x: 2**(x-1) , filter
                (lambda z: z > 0, map
                 (lambda x: len(list(filter
                  (lambda y: y in x[0], x[1]))), data)))
            )

def part2():
    """
    PART2

    Answer for part2:
    """
    pass

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()