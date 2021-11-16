#!/usr/bin/env python

"""
Puzzle Title:     AoC 2020 Day 1: Report Repair
Puzzle Link:      https://adventofcode.com/2020/day/1
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
import itertools
import math


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip().isnumeric():
            data.append(int(line))
    return data


def combination_add_to(items, amount, total):
    for nums in itertools.combinations(items, amount):
        if sum(nums) == total:
            return nums


def solve_part1(data):
    return math.prod(combination_add_to(data, 2, 2020))


def solve_part2(data):
    return math.prod(combination_add_to(data, 3, 2020))


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
