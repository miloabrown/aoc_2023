"""
Advent Of Code 2023
Code written by Milo
Day 15: Lens library
"""
import re
from functools import reduce

# Deal with input.
with open("day_15/test_input.txt", "r") as file:
    data = file.read().strip().split(",")

def h_algorithm(s):
    """
    HASH algo for part1
    """
    cur = reduce(lambda acc, c: (acc + ord(c)) * 17 % 256, s, 0)
    return cur

def part1():
    """
    PART1

    Answer for part1: 519603
    """
    return sum(map(h_algorithm, data))

def part2():
    """
    PART2

    Answer for part2: 244342
    """
    boxes = {}
    for lens in data:
        label, focal = re.split(r"=|-", lens)
        if not focal:
            boxes.setdefault(h_algorithm(label), {}).pop(label, None)
            continue
        boxes.setdefault(h_algorithm(label), {})[label] = int(focal)

    return sum((int(key)+1) * sum([idx * val for idx, val in enumerate(box.values(), 1)]) for key, box in boxes.items())

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()