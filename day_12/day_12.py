"""
Advent Of Code 2023
Code written by Milo
Solution by HyperNeutrino
Day 12: Hot Springs
"""
# Deal with input.
with open("day_12/input.txt", "r") as file:
    data = file.read().splitlines()

cache = {} # for optimization
def count(springs, nums):
    if springs == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in springs else 1

    key = (springs, nums)
    if key in cache:
        return cache[key]

    result = 0

    if springs[0] in ".?":
        result += count(springs[1:], nums)

    if springs[0] in "#?":
        if nums[0] <= len(springs) and "." not in springs[:nums[0]]\
        and(nums[0] == len(springs) or springs[nums[0]] != "#"):
            result += count(springs[nums[0]+1:], nums[1:])

    cache[key] = result
    return result

def part1():
    """
    PART1
    Answer for part1: 8180
    """
    ans = 0
    for line in data:
        springs, numbers = line.split()
        numbers = tuple(map(int, numbers.split(",")))

        ans += count(springs, numbers)
    return ans

def part2():
    """
    PART2
    Answer for part2: 620189727003627
    """
    ans = 0
    for line in data:
        springs, numbers = line.split()
        numbers = tuple(map(int, numbers.split(",")))

        # Unfold the instructions
        springs = "?".join([springs]*5)
        numbers *= 5

        ans += count(springs, numbers)
    return ans


def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()