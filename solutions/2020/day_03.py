#!/usr/bin/env python

"""
Puzzle Title:     AoC 2020 Day 3: Toboggan Trajectory
Puzzle Link:      https://adventofcode.com/2020/day/3
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
import math


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip():
            data.append(line)
    return data


def trees_on_diag(grid, right, down):
    x_pos = 0
    y_pos = 0
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1
    total = 0
    while y_pos < y_max:
        x_pos += right
        y_pos += down
        if grid[y_pos][x_pos % x_max] == "#":
            total += 1
    return total


def solve_part1(grid):
    return trees_on_diag(grid, 3, 1)


def solve_part2(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod([trees_on_diag(grid, right, down) for right, down in slopes])


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
