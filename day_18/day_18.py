"""
Advent Of Code 2023
Code written by Milo
Inspiration from HyperNeutrino
Day 18: Lavaduct Lagoon
"""

# Deal with input.
with open("day_18/input.txt", "r") as file:
    data = [row.split() for row in file.read().splitlines()]


def calculate_area(part2=False):

    points = [(0, 0)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    border = 0

    for direction, num, hex  in data:
        hex = hex[2:-1]
        num = int(num) if not part2 else int(hex[:-1], 16)
        delta_row, delta_col = dirs[direction] if not part2 else dirs["RDLU"[int(hex[-1])]]
        border += num
        row, col = points[-1]
        points.append((row + num * delta_row, col + num * delta_col))

    A = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) // 2
    inside = A - border // 2 + 1

    return (inside+border)

def part1():
    """
    PART1

    Answer for part1: 70253
    """
    return calculate_area()


def part2():
    """
    PART2

    Answer for part2: 131265059885080
    """
    return calculate_area(True)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()