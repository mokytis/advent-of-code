#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 7: The Treachery of Whales
Puzzle Link:      https://adventofcode.com/2021/day/7
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
from collections import defaultdict
from statistics import median


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip():
            data = [int(num) for num in line.rstrip().split(",")]
    return data


def solve_part1(data):
    mid_point = round(median(data))
    return sum(abs(point - mid_point) for point in data)


def solve_part2(data):
    mid_points = defaultdict(int)
    for point in range(min(data), max(data)):
        for num in data:
            distance = abs(point - num)
            mid_points[point] += (distance * (distance + 1)) // 2
    return mid_points[min(mid_points, key=mid_points.get)]


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
