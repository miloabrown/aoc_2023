"""
Advent Of Code 2023
Code written by Milo
Solution based partially on solution by HyperNeutrino
Day 16: The floor will be lava
"""
from collections import deque

# Deal with input.
with open("day_16/input.txt", "r") as file:
    grid = file.read().splitlines()

def count_hits(start):
    """
    Function to calculate how many tiles are hit by a beam
    starting with given parameter.

    start/parameter: tuple of (row, col, delta_r, delta_c)
    """

    a = [start]
    seen = set()
    q = deque(a)

    while q:
        row, col, delta_r, delta_c = q.popleft()

        row += delta_r
        col += delta_c

        if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
            continue

        ch = grid[row][col]

        if ch == "." or (ch == "-" and delta_c != 0) or (ch == "|" and delta_r != 0):
            if (row, col, delta_r, delta_c) not in seen:
                seen.add((row, col, delta_r, delta_c))
                q.append((row, col, delta_r, delta_c))
        elif ch == "/":
            delta_r, delta_c = -delta_c, -delta_r
            if (row, col, delta_r, delta_c) not in seen:
                seen.add((row, col, delta_r, delta_c))
                q.append((row, col, delta_r, delta_c))

        elif ch == "\\":

            delta_r, delta_c = delta_c, delta_r
            if (row, col, delta_r, delta_c) not in seen:
                seen.add((row, col, delta_r, delta_c))
                q.append((row, col, delta_r, delta_c))

        else:
            for delta_r ,delta_c in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (row, col, delta_r, delta_c) not in seen:
                    seen.add((row, col, delta_r, delta_c))
                    q.append((row, col, delta_r, delta_c))

    coords = {(r,c) for r, c, _, _ in seen}
    return (len(coords))

def part1():
    return count_hits((0, -1, 0, 1))

def part2():
    max_val = max(
        max(count_hits((row, -1, 0, 1)), count_hits((row, len(grid[0]), 0, -1)))
        for row in range(len(grid))
    )

    max_val = max(
        max(count_hits((-1, col, 1, 0)), count_hits((len(grid), col, -1, 0)))
        for col in range(len(grid[0]))
    )

    return max_val

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()