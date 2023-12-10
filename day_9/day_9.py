from functools import reduce

"""
Advent Of Code 2023
Code written by Milo
Day 9: Mirage Maintenance
"""

# Deal with input.
with open("day_9/input.txt", "r") as file:
    data = [list(map(int,(row.split()))) for row in file.read().splitlines()]

def get_histories(row):
    histories = [row]
    while not all(x == 0 for x in row):
        row = [x[1] - x[0] for x in zip(row, row[1:])]
        histories.append(row)
    return histories

def extrapolate(left):
    next_values = [
        reduce(lambda x, history:
        x + history[-1] if not left
        else history[0] - x, reversed(histories), 0)
        for row in data for histories in [get_histories(row)]
        ]

    return sum(next_values)

def part1():
    """
    PART1

    Answer for part1: 1637452029
    """

    return extrapolate(False)

def part2():
    """
    PART2

    Answer for part2: 908
    """
    return extrapolate(True)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()