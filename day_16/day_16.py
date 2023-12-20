"""
Advent Of Code 2023
Code written by Milo
Day 16: The floor will be lava
"""
from collections import deque

# Deal with input.
with open("day_16/input.txt", "r") as file:
    data = file.read().splitlines()


"""
data is a 2d grid
beam starts at 0,0 going right
calculate how many spaces are hit by at least one beam
Beam behavior:
- "." continue in same direction
- "/" or "\" turn 90 degrees
- "|" split into two beams if hiting from left or right, otherwise continue in same direction
- "-" split into two beams if hiting from top or bottom, otherwise continue in same direction

"""
def beam(start, direction):
    """
    Function to calculate how many tiles are hit by a beam
    starting at start and going in direction
    """
    tiles_hit = set()
    checked = set()
    count = 0
    directions = {
        "r": (0,1),
        "l": (0,-1),
        "u": (-1,0),
        "d": (1,0)
    }

    tile_queue = deque()
    tile_queue.append((start, direction))

    while tile_queue:
        tile, direction = tile_queue.popleft()
        #check inbounds
        if not 0 <= tile[0] < len(data) or not 0 <= tile[1] < len(data[0]) or (tile,direction) in checked:
            continue

        tiles_hit.add(tile)
        checked.add((tile, direction))

        if data[tile[0]][tile[1]] == ".":
            tile_queue.append(((tile[0]+directions[direction][0], tile[1]+directions[direction][1]), direction))
        elif data[tile[0]][tile[1]] == "/":
            if direction == "r":
                tile_queue.append(((tile[0]+directions["u"][0], tile[1]+directions["u"][1]), "u"))
            elif direction == "l":
                tile_queue.append(((tile[0]+directions["d"][0], tile[1]+directions["d"][1]), "d"))
            elif direction == "u":
                tile_queue.append(((tile[0]+directions["r"][0], tile[1]+directions["r"][1]), "r"))
            elif direction == "d":
                tile_queue.append(((tile[0]+directions["l"][0], tile[1]+directions["l"][1]), "l"))

        elif data[tile[0]][tile[1]] == "\\":
            if direction == "r":
                tile_queue.append(((tile[0]+directions["d"][0], tile[1]+directions["d"][1]), "d"))
            elif direction == "l":
                tile_queue.append(((tile[0]+directions["u"][0], tile[1]+directions["u"][1]), "u"))
            elif direction == "u":
                tile_queue.append(((tile[0]+directions["l"][0], tile[1]+directions["l"][1]), "l"))
            elif direction == "d":
                tile_queue.append(((tile[0]+directions["r"][0], tile[1]+directions["r"][1]), "r"))

        elif data[tile[0]][tile[1]] == "|":
            if direction == "r" or direction == "l":
                tile_queue.append(((tile[0]+directions["u"][0], tile[1]+directions["u"][1]), "u"))
                tile_queue.append(((tile[0]+directions["d"][0], tile[1]+directions["d"][1]), "d"))
            else:
                tile_queue.append(((tile[0]+directions[direction][0], tile[1]+directions[direction][1]), direction))

        elif data[tile[0]][tile[1]] == "-":
            if direction == "u" or direction == "d":
                tile_queue.append(((tile[0]+directions["r"][0], tile[1]+directions["r"][1]), "r"))
                tile_queue.append(((tile[0]+directions["l"][0], tile[1]+directions["l"][1]), "l"))
            else:
                tile_queue.append(((tile[0]+directions[direction][0], tile[1]+directions[direction][1]), direction))

        #need something to stop infinite loops
        count+=1
        if count > len(data)*len(data[0])*10:
            break

    return len(tiles_hit)

def part1():
    """
    PART1

    Answer for part1: 7951
    """
    return beam((0,0), "r")

def part2():
    """
    PART2
    Where to start the beam and what direction
    to hit the most tiles?

    it can start from any edge, going in that direction
    or from any corner going in one of the two directions

    Answer for part2: 8148
    """

    #top row
    top_row = [(0, i) for i in range(len(data[0]))]
    #bottom row
    bottom_row = [(len(data)-1, i) for i in range(len(data[0]))]
    #left column
    left_column = [(i, 0) for i in range(len(data))]
    #right column
    right_column = [(i, len(data[0])-1) for i in range(len(data))]

    top_max = max([beam(tile, "d") for tile in top_row])
    bottom_max = max([beam(tile, "u") for tile in bottom_row])
    left_max = max([beam(tile, "r") for tile in left_column])
    right_max = max([beam(tile, "l") for tile in right_column])

    return max(top_max, bottom_max, left_max, right_max)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()