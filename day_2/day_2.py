"""
Advent Of Code 2023
Code written by Milo
Day2
"""
import re

# Deal with input.
with open("day_2/input.txt", "r") as file:
    data = [[tuple(x.split(" ")) for x in re.split(': |; |, ',row)[1:]] for row in file.read().splitlines()]

def part1():
    """
    PART1
    Which games are possible with 12 red, 13 green and 14 blue cubes?
    Return the sum of the id's of the rows that are possible.

    Answer for part1: 2727
    """
    return sum([
        id for id, game in enumerate(data, 1) if
        all(int(x[0]) <= 12 for x in game if x[1] == "red") and
        all(int(x[0]) <= 13 for x in game if x[1] == "green") and
        all(int(x[0]) <= 14 for x in game if x[1] == "blue")
        ])

def part2():
    """
    PART2
    Find the minimum amount of cubes to make each game possible,
    multiply the number of min cubes for the "power" of each row.
    Return the sum of the "powers" of each row.

    Answer for part2: 56580
    """

    return sum([
        max([int(x[0]) for x in row if x[1] == "red"]) *
        max([int(x[0]) for x in row if x[1] == "green"]) *
        max([int(x[0]) for x in row if x[1] == "blue"])
        for row in data
    ])

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()