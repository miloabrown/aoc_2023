"""
Advent Of Code 2023
Code written by Milo
Solution based on HyperNeutrino's solution
Day 14: Parabolic reflector dish
"""

# Deal with input.
with open("day_14/test_input.txt", "r") as file:
    data = tuple(file.read().splitlines())

def cycle(rotation = 4):
    global data
    for _ in range(rotation):
        data = tuple(map("".join, zip(*data)))
        data = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in data)
        #p1
        if rotation == 1:
            data = tuple(map("".join, zip(*data)))
        #p2
        else:
            data = tuple(row[::-1] for row in data)


def part1():
    """
    PART1

    Answer for part1: 110274
    """
    cycle(1)
    return (sum(row.count("O") * (len(data) - r) for r, row in enumerate(data)))



def part2():
    """
    PART2

    Answer for part2: 90982
    """
    grid = data
    seen = {grid}
    array = [grid]
    iter = 0

    while True:
        iter += 1
        cycle()
        grid = data
        if grid in seen:
            break
        seen.add(grid)
        array.append(grid)

    first = array.index(grid)
    grid = array[(1000000000 - first) % (iter - first) + first]

    return (sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))


def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()