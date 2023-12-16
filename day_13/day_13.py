"""
Advent Of Code 2023
Code written by Milo
Solution inspired by HyperNeutrino

Day 13: Point of incidence
"""

# Deal with input.
with open("day_13/input.txt", "r") as file:
    data = [row.splitlines() for row in file.read().split("\n\n")]

def find_mirror(data):
    for r in range(1, len(data)):
        above = data[:r][::-1]
        below = data[r:]

        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return r
    return 0

def find_mirror2(data):
        for r in range(1, len(data)):
            above = data[:r][::-1]
            below = data[r:]

            if sum(sum(0 if a == b else 1 for a,b in zip(x,y)) for x,y in zip(above, below)) == 1:
                return r
        return 0

def part1():
    """
    PART1

    Answer for part1: 42974
    """
    return sum([100*(find_mirror(block)) + find_mirror(list(zip(*block))) for block in data])

def part2():
    """
    PART2

    Answer for part2: 27587
    """
    return sum([100*(find_mirror2(block)) + find_mirror2(list(zip(*block))) for block in data])

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()