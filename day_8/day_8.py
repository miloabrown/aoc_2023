from math import gcd

"""
Advent Of Code 2023
Code written by Milo
Day8: Haunted wasteland
"""

# Deal with input
with open("day_8/input.txt", "r") as file:
    steps, _, *nodes= file.read().splitlines()

nodes = {node.split(" = ")[0]:(node.split(" = ")[1][1:-1].split(", ")) for node in nodes}
directions = {"R": 1, "L": 0}

def part1():
    """
    PART1
    Answer for part1: 19951
    """

    step_count = 0
    current = "AAA"
    while current != "ZZZ":
        current = nodes[current][directions[steps[int(step_count % len(steps))]]]
        step_count += 1
    return step_count

def part2():
    """
    PART2
    Answer for part2: 16342438708751
    """

    starts = [node for node in nodes if node.endswith("A")]
    cycles = []

    for current in starts:
        cycle = []
        current_steps = steps
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not current.endswith("Z"):
                step_count += 1
                current = nodes[current][directions[current_steps[0]]]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    lcm = cycles[0][0]
    for cycle in cycles[1:]:
        lcm = lcm * cycle[0] // gcd(lcm, cycle[0])

    return lcm




def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()