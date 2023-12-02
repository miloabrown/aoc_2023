"""
Advent Of Code 2023
Code written by Milo
Day2
"""

import re

# Deal with input.
with open("day_2/test_input.txt", "r") as file:
    data = [
        (list(map(lambda x: tuple(x.split(" ")),
        (", ".join(re.split(': |; ',row)[1:]).split(", ")))))
        for row in file.read().split("\n")[:-1]
        ]

print(data)


def part1():
    """
    PART1
    Which games are possible with 12 red, 13 green and 14 blue cubes?

    Answer for part1: 2727
    """

    filtered_rows = []

    for id,row in enumerate(data):
        filtered_row = (list(map(lambda x: 1 if (int(x[0])<=12 and x[1]=="red")\
                                        or (int(x[0]) <= 13 and x[1]=="green")\
                                        or (int(x[0]) <= 14 and x[1]=="blue") else 0\
                                            ,row)))
        filtered_rows.append(id+1 if all(x == 1 for x in filtered_row) else 0)

    return sum(filtered_rows)



def part2():
    """
    PART2
    Find the minimum amount of cubes to make each game possible,
    multiply the number of cubes for each row and sum all the rows.

    Answer for part2:
    """




def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()