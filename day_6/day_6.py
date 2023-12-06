import math

"""
Advent Of Code 2023
Code written by Milo
Day6: Wait For It
"""

# Deal with input.
with open("day_6/input.txt", "r") as file:
    data = [row.split()[1:] for row in file.readlines()]

def count_possible_wins(time, distance):
    """
    Helper function that solves the amount of
    possible wins using the quadratic formula.
    """
    root1 = (float(time) + math.sqrt(float(time)**2 - 4.0 * float(distance))) / 2.0 - 1.0
    root2 = (float(time) - math.sqrt(float(time)**2 - 4.0 * float(distance))) / 2.0 + 1.0

    return math.ceil(root1) - math.floor(root2) +1

def part1():
    """
    PART1

    Answer for part1: 3317888
    """

    times, distances = [list(map(int, row)) for row in [*data]]
    return math.prod([count_possible_wins(x, y) for x, y in zip(times, distances)])


def part2():
    """
    PART2

    Answer for part2: 24655068
    """

    time, distance = [int("".join(row)) for row in data]
    return count_possible_wins(time, distance)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()
