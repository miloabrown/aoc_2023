"""
Advent Of Code 2023
Code written by Milo
Solution based on HyperNeutrino's solution
Day 17: Clumsy Crucible
"""
from heapq import heappop, heappush

# Deal with input.
with open("day_17/input.txt", "r") as file:
    data = [list(map(int,row))for row in file.read().splitlines()]

# print(*data, sep="\n")

def dijkstra(part2=False):

    seen = set()
    end = (len(data)-1, len(data[0])-1)
    pq = [(0, 0, 0, 0, 0, 0)]

    limit = 10 if part2 else 3

    while pq:
        cost, row, col, delta_row, delta_col, consecutive = heappop(pq)

        if (row, col) == end or (not part2 and consecutive >= 4):
            return cost

        if (row, col, delta_row, delta_col, consecutive) in seen:
            continue

        seen.add((row, col, delta_row, delta_col, consecutive))

        if consecutive < limit and (delta_row, delta_col) != (0, 0):
            new_row = row + delta_row
            new_col = col + delta_col
            if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]):
                heappush(pq, (cost + data[new_row][new_col], new_row, new_col, delta_row, delta_col, consecutive + 1))

        if not part2 or (4 <= consecutive or (delta_row, delta_col) == (0, 0)):
            for new_delta_row, new_delta_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (new_delta_row, new_delta_col) != (delta_row, delta_col)\
                and (new_delta_row, new_delta_col) != (-delta_row, -delta_col):
                    new_row = row + new_delta_row
                    new_col = col + new_delta_col
                    if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]):
                        heappush(pq, (cost + data[new_row][new_col], new_row, new_col, new_delta_row, new_delta_col, 1))


def part1():
    """
    PART1

    Answer for part1: 797
    """
    return dijkstra()

def part2():
    """
    PART2

    Answer for part2: 914
    """
    return dijkstra(True)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()