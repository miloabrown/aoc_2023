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


# Find the starting pipe.
start = next((i, j) for i, row in enumerate(data) for j, pipe in enumerate(row) if pipe == "S")
# Define the direction mappings for the starting pipe.
direction_mapping = {
    (1, 0): "|JL",  # Down
    (0, -1): "-FL", # Left
    (-1, 0): "|F7", # Up
    (0, 1): "-J7"   # Right
}
# Find the first two pipes connected to the start.
loop = [(row, col) for direction in direction_mapping.keys()
    for row, col in [(start[0] + direction[0], start[1] + direction[1])]
    if 0 <= row < len(data) and 0 <= col < len(data[0])
    if data[row][col] in direction_mapping[direction]]


# Find the loop.
next_pipe, last_pipe = loop[0], loop[1]
previous_pipe = start

# Figure out which shape the starting pipe is
start_shape = (set(direction_mapping[start[0]-next_pipe[0],start[1]-next_pipe[1]]) &
               set(direction_mapping[start[0]-last_pipe[0], start[1]-last_pipe[1]])).pop()
# Replace the starting pipe with the correct shape.
data[start[0]] = data[start[0]].replace("S", start_shape)

while next_pipe != last_pipe:
    loop.append(next_pipe)
    valid_steps = find_valid_steps(next_pipe[0], next_pipe[1])
    step = next((step for step in valid_steps if step != previous_pipe))
    previous_pipe, next_pipe = next_pipe, step
loop.append(start)

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

    # Change all the spaces in data to "." if they are not in the loop.
    cleaned_data = ["".join(["." if (i, j) not in loop else pipe for j, pipe in enumerate(row)]) for i, row in enumerate(data)]

#Solution by HyperNeutrino
#---------------------------------------------------------------------
    outside = set()
    for row_num, row in enumerate(cleaned_data):
        within = False
        up = None
        for col_idx, space in enumerate(row):
            if space == "|":
                assert up is None
                within = not within
            elif space == "-":
                assert up is not None
            elif space in "LF":
                assert up is None
                up = space == "L"
            elif space in "J7":
                assert up is not None
                if space != ("J" if up else "7"):
                    within = not within
                up = None
            elif space == ".":
                pass
            else:
                raise RuntimeError(f"Unknown space: {space}")
            if not within:
                outside.add((row_num, col_idx))
#---------------------------------------------------------------------

    return (len(data) * len(data[0]) - len(set(loop)|outside))

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()