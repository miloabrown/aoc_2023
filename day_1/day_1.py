"""
Advent Of Code 2023
Code written by Milo
Day1
"""

# Deal with input.
with open("day_1/input.txt", "r") as file:
    data = file.read().splitlines()

def just_digits(string):
    """
    Helper function
    to remove all non-digits from a string.
    """
    return "".join([char for char in string if char.isdigit()])

def part1():
    """
    PART1

    Answer for part1: 55538
    """

    digits = [just_digits(row) for row in data]
    return sum([int(row[0]+row[-1]) for row in digits])


def part2():
    """
    PART2

    Answer for part2: 54875
    """

    def text_to_digit(string):
        """
        Helper function for part2
        to convert a string to a digit in string format.
        """
        text_digits = {
            "one": "o1e",
            "two": "t2o",
            "three": "t3e",
            "four": "f4r",
            "five": "f5e",
            "six": "s6x",
            "seven":"s7n",
            "eight": "e8t",
            "nine": "n9e",
        }

        for key,item in text_digits.items():
            string = string.replace(key,item)
        return string

    digits = [just_digits(text_to_digit(row)) for row in data]
    return sum([int(row[0]+row[-1]) for row in digits])


def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()