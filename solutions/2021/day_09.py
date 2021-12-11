#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 9: Smoke Basin
Puzzle Link:      https://adventofcode.com/2021/day/9
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput


def parse_input():
    data = []
    for line in map(lambda l: l.rstrip(), fileinput.input()):
        if line:
            data.append([int(i) for i in line])
    return data


def solve_part1(data):
    total = 0
    for x, row in enumerate(data):
        for y, item in enumerate(row):
            if x > 0 and data[x - 1][y] <= item:
                continue
            if x < len(data) - 1 and data[x + 1][y] <= item:
                continue
            if y > 0 and data[x][y - 1] <= item:
                continue
            if y < len(data[0]) - 1 and data[x][y + 1] <= item:
                continue
            total += item + 1
    return total


def find_basin(x, y, grid, basin):
    if x > 0 and grid[x - 1][y] != 9:
        if (x - 1, y) not in basin:
            basin.add((x - 1, y))
            find_basin(x - 1, y, grid, basin)
    if x < len(grid) - 1 and grid[x + 1][y] != 9:
        if (x + 1, y) not in basin:
            basin.add((x + 1, y))
            find_basin(x + 1, y, grid, basin)
    if y > 0 and grid[x][y - 1] != 9:
        if (x, y - 1) not in basin:
            basin.add((x, y - 1))
            find_basin(x, y - 1, grid, basin)
    if y < len(grid[0]) - 1 and grid[x][y + 1] != 9:
        if (x, y + 1) not in basin:
            basin.add((x, y + 1))
            find_basin(x, y + 1, grid, basin)


def solve_part2(data):
    sizes = []
    for x, row in enumerate(data):
        for y, item in enumerate(row):
            if x > 0 and data[x - 1][y] <= item:
                continue
            if x < len(data) - 1 and data[x + 1][y] <= item:
                continue
            if y > 0 and data[x][y - 1] <= item:
                continue
            if y < len(data[0]) - 1 and data[x][y + 1] <= item:
                continue
            basin = {(x, y)}
            find_basin(x, y, data, basin)
            sizes.append(len(basin))
    ans = 1
    for num in sorted(sizes)[-3:]:
        ans *= num
    return ans


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
