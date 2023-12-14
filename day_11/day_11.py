"""
Advent Of Code 2023
Code written by Milo
Day 11: Cosmic Expansion
"""

# Deal with input.
with open("day_11/input.txt", "r") as file:
    data = file.read().splitlines()

def solve(expand):
    """
    Solves both parts.
    expand is the amount of rows and
    columns to expand the grid by.
    """
    empty_rows = [idx for idx, row in enumerate(data) if all(x == "." for x in row)]
    empty_cols = [idx for idx, col in enumerate(zip(*data)) if all(x == "." for x in col)]

    galaxies = [(row_idx, col_idx) for row_idx, row in enumerate(data)
                for col_idx, col in enumerate(row) if col == "#"]

    ans = 0
    for i, (row1, col1) in enumerate(galaxies):
        for (row2, col2) in galaxies[:i]:
            for row in range(min(row1, row2), max(row1, row2)):
                ans += expand if row in empty_rows else 1
            for col in range(min(col1, col2), max(col1, col2)):
                ans += expand if col in empty_cols else 1
    return ans

def part1():
    """
    PART1
    Expand empty spaces by 2.

    Answer for part1: 9947476
    """
    return solve(2)

def part2():
    """
    PART2
    Expand empty spaces by 1000000.

    Answer for part2: 519939907614
    """
    return solve(1000000)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()