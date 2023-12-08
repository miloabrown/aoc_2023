"""
Advent Of Code 2023
Code written by Milo
Day3
"""

import math  # For product function

# Deal with input.
with open("day_3/input.txt", "r") as file:
    data = file.read().splitlines()

def create_full_number(x,y):
    """
    Helper function to connect the singular digits
    to create the full number.

    The parts for the number will be in
    the coordinates to the left and/or right of it,
    until there are no more digits.
    """

    y_left = y_right = y
    while y_left > 0 and data[x][y_left-1].isdigit():
        y_left -=1
    while y_right < len(data[x])-1 and data[x][y_right+1].isdigit():
        y_right +=1

    return int(data[x][y_left:y_right+1])

def add_to_checked(x,y, coords_checked):
    """
    Helper function to add the coordinates
    of the digits that have been checked
    to a list.
    This function checks if the next coordinate(s)
    to the right are digits and also adds these to
    prevent duplicates.
    """

    coords_checked.append((x,y))
    if y < len(data[x])-1 and data[x][y+1].isdigit():
        coords_checked.append((x,y+1))
        add_to_checked(x,y+1,coords_checked)

def part1():
    """
    PART1
    Find all the "parts" with adjacent numbers.
    Sum these numbers to find the answer.

    Answer for part1: 525911
    """
    def is_part(x,y):
        """
        Helper function to check if number
        at given coordinates is a part.
        Checks all the 8 surrounding coordinates
        for a character other than "." or a number.
        """

        adjacent = [
            (x-1,y-1), (x,y-1), (x+1,y-1),
            (x-1,y), (x+1,y),
            (x-1,y+1), (x,y+1), (x+1,y+1)
        ]

        for i,j in adjacent:
            if 0 <= i\
            and 0 <= j\
            and i < len(data)\
            and j < len(data[0])\
            and data[i][j] != "."\
            and not data[i][j].isdigit():
                return True
        return False

    parts = []
    coords_checked = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit() and is_part(i,j) and (i,j) not in coords_checked:
                parts.append(create_full_number(i,j))
                add_to_checked(i,j,coords_checked)

    return sum(parts)

def part2():
    """
    PART2

    Gears are any "*" symbols with exactly two adjacent numbers.
    The gear ratio of a gear is the result of multiplying the two
    adjacent numbers.
    Find all the gears and sum their gear ratios.

    Answer for part2: 75805607
    """
    def valid_gear(x, y):
        """
        Helper function to check if gear
        at given coordinates has two adjacent numbers.
        Checks all the 8 surrounding coordinates
        for numbers.
        """

        adjacent = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),           (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]

        part_numbers = 0
        part_coords = []
        coords_checked = []

        for i, j in adjacent:
            if 0 <= i < len(data) and 0 <= j < len(data[0])\
            and data[i][j].isdigit() and (i,j) not in coords_checked:
                part_numbers += 1
                part_coords.append((i, j))
                add_to_checked(i, j, coords_checked)

        return [create_full_number(i, j) for i, j in part_coords] if part_numbers == 2 else False


    gears = [
        math.prod(valid_gear(i, j))
        for i in range(len(data))
        for j in range(len(data[i]))
        if data[i][j] == "*" and valid_gear(i, j)
        ]

    return sum(gears)


def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()