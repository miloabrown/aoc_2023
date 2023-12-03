"""
Advent Of Code 2023
Code written by Milo
Day3
"""

from itertools import chain  # For flattening lists

# Deal with input.
with open("day_3/input.txt", "r") as file:
    data = file.read().splitlines()

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
        try:
            if data[i][j] != "." and not data[i][j].isdigit():
                return True
        except IndexError as e:
            continue
    return False

def create_full_number(x,y,digit):
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

def part1():
    """
    PART1
    Find all the "parts" with adjacent numbers.
    Sum these numbers to find the answer.

    Answer for part1: 525911
    """

    parts = []
    coords_checked = []
    def add_to_checked(x,y):
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
            add_to_checked(x,y+1)

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit() and is_part(i,j) and (i,j) not in coords_checked:
                parts.append(create_full_number(i,j,data[i][j]))
                add_to_checked(i,j)

    return sum(parts)

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