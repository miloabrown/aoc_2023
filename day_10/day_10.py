"""
Advent Of Code 2023
Code written by Milo
Day 10: Pipe Maze
"""

# Deal with input.
with open("day_10/input.txt", "r") as file:
    data = file.read().splitlines()


def find_valid_steps(row, col):
    """
    Function that finds the two valid locations to move to from a given location.
    returns a list of tuples, each tuple is a coordinate.
    The other one is the one you came from.
    """
    directions = {
        "|": [(1, 0), (-1, 0)], "-": [(0, 1), (0, -1)], "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)], "7": [(1, 0), (0, -1)], "F": [(1, 0), (0, 1)]
        }
    return [((row + direction[0]), (col + direction[1])) for direction in directions[data[row][col]]]

loop = []

# Find the starting pipe.
start = next((i, j) for i, row in enumerate(data) for j, pipe in enumerate(row) if pipe == "S")
# Define the direction mappings for the starting pipe.
direction_mapping = {
    (1, 0): "|F7",
    (0, -1): "-FL",
    (-1, 0): "|JL",
    (0, 1): "-J7"
}
# Find the first two pipes connected to the start.
start_options = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # Down, Left, Up, Right
loop = [(row, col) for direction in start_options
    for row, col in [(start[0] + direction[0], start[1] + direction[1])]
    if 0 <= row < len(data) and 0 <= col < len(data[0])
    if data[row][col] in direction_mapping[direction]]

# Find the loop.
next_pipe, last_pipe = loop[0], loop[1]
previous_pipe = start

while next_pipe != last_pipe:
    loop.append(next_pipe)
    valid_steps = find_valid_steps(next_pipe[0], next_pipe[1])
    step = next((step for step in valid_steps if step != previous_pipe))
    previous_pipe, next_pipe = next_pipe, step

def part1():
    """
    PART1

    Answer for part1: 6870
    """

    return len(loop) // 2

def part2():
    """
    PART2

    Answer for part2:
    """
    pass

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()