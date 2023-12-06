"""
Advent Of Code 2023
Code written by Milo
Day6: Wait For It
"""
import numpy as np  # For product function.

# Deal with input.
with open("day_6/input.txt", "r") as file:
    data = [row.split()[1:] for row in file.readlines()]

def count_possible_wins(time, distance):
    return len([x for x in range(time) if (time - x) * x > distance])

def part1():
    """
    PART1

    Answer for part1: 3317888
    """

    times,distances = [list(map(int,row)) for row in [*data]]
    return np.prod([count_possible_wins(x, y) for x, y in zip(times, distances)])

def part2():
    """
    PART2

    Answer for part2: 24655068
    """

    time, distance = [int("".join(row)) for row in data]

    def binary_search(is_left):
        left = 0
        right = time
        while left < right:
            mid = (left + right) // 2
            if (time - mid) * mid > distance:
                if is_left:
                    right = mid
                else:
                    left = mid + 1
            else:
                if is_left:
                    left = mid + 1
                else:
                    right = mid
        return left

    return binary_search(False) - binary_search(True)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()