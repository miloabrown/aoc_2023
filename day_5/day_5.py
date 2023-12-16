from functools import reduce  # For the reduce function

"""
Advent Of Code 2023
Code written by Milo
Day5: If You Give A Seed A Fertilizer
"""

# Deal with input.
with open("day_5/input.txt", "r") as file:
    data = file.read().split("\n\n")

seeds = data[0].split(": ")[1].split()
maps = list(
    map(lambda x: [row.split() for row in x.split(":")[1].strip().split("\n")],data[1:]))


def part1():
    """
    PART1

    Maps: destination range start | source range start | range length
    Find the smallest location from all seeds.

    Conversions: seed -> soil -> fertilizer -> water -> light -> temp -> humidity -> location

    Answer for part1: 282277027
    """
    def convert_value(value, map):
        """
        Function to convert value to new value based on map.
        """
        for range in map:
            if int(range[1]) <= value <= int(range[1]) + int(range[2]):
                return value - (int(range[1]) - int(range[0]))
        return value

    def get_location(seed):
        return reduce(lambda x, y: convert_value(x, y), [seed] + [*maps])

    return min([get_location(int(seed)) for seed in seeds])

def part2():
    """
    PART2
    Answer for part2: 11554135
    """

    new_seeds = [(int(a),int(a)+int(b)) for a,b in zip(seeds[:-1:2],seeds[1::2])]

    for block in maps:
        ranges = [list(map(int, line)) for line in block]

        new = []
        while new_seeds:
            start, end = new_seeds.pop()
            for dest_rng_start, src_rng_start, rng_len in ranges:
                overlap_start = max(start, src_rng_start)
                overlap_end = min(end, src_rng_start+rng_len)
                if overlap_start < overlap_end:
                    new.append((overlap_start - src_rng_start + dest_rng_start, overlap_end - src_rng_start + dest_rng_start))
                    if overlap_start > start:
                        new_seeds.append((start,overlap_start))
                    if end > overlap_end:
                        new_seeds.append((overlap_end, end))
                    break
            else:
                new.append((start,end))
        new_seeds = new
    return(min(new_seeds)[0])

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()