"""
Advent Of Code 2023
Code written by Milo
Day6: Wait For It
"""

import numpy as np  # For product function.

# Deal with input.
with open("day_6/test_input.txt", "r") as file:
    times, distances = [row.split()[1:] for row in file.readlines()]

def part1():
    """
    PART1

    Answer for part1: 3317888
    """
    def possible_wins(time,distance):
        return len([x for x in range(int(time)) if (int(time)-int(x)) * int(x) > int(distance)])

    return np.prod([possible_wins(x,y) for x,y in zip(times,distances)])


def part2():
    """
    PART2

    Answer for part2: 24655068
    """
    time,distance = int("".join(times)),int("".join(distances))

    def possible_wins():
        mini = next(x for x in range(int(time)) if (int(time)-int(x)) * int(x) > int(distance))
        maxi = next(x for x in range(int(time),-1,-1) if (int(time)-int(x)) * int(x) > int(distance))

        return maxi-mini+1

    return possible_wins()

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()