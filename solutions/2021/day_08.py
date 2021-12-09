#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 8: Seven Segment Search
Puzzle Link:      https://adventofcode.com/2021/day/8
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
from collections import defaultdict


def parse_input():
    data = []
    for line in map(lambda l: l.rstrip(), fileinput.input()):
        if line:
            training, test = line.split(" | ")
            data.append(
                {
                    "training": [set(digit) for digit in training.split(" ")],
                    "test": [set(digit) for digit in test.split(" ")],
                }
            )
    return data


def solve_part1(data):
    total = 0
    for row in data:
        for item in row["test"]:
            match len(item):
                case 2:
                    total += 1
                case 4:
                    total += 1
                case 3:
                    total += 1
                case 7:
                    total += 1
    return total



def solve_part2(data):
    total = 0
    for row in data:
        digits = {}
        for item in row["training"]:
            match len(item):
                case 2:
                    digits["1"] = item
                case 4:
                    digits["4"] = item
                case 3:
                    digits["7"] = item
                case 7:
                    digits["8"] = item
        num = 0
        for item in row["test"]:
            num *= 10
            match len(item):
                case 2:
                    num += 1
                case 4:
                    num += 4
                case 3:
                    num += 7
                case 7:
                    num += 8
                case 6:
                    if not digits["1"].issubset(item):
                        num += 6
                    elif digits["4"].issubset(item):
                        num += 9
                    else:
                        digits["0"] = item
                case 5:
                    if digits["1"].issubset(item):
                        num += 3
                    elif (digits["4"] - digits["1"]).issubset(item):
                        num += 5
                    else:
                        num += 2
        total += num
    return total


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
