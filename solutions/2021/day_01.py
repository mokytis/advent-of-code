#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 1: Sonar Sweep
Puzzle Link:      https://adventofcode.com/2021/day/1
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip().isnumeric():
            data.append(int(line))
    return data


def solve_part1(data):
    inc = 0
    prev = data[0]
    for value in data[1:]:
        if value > prev:
            inc += 1
        prev = value
    return inc


def solve_part2(data):
    """as 2 of the 3 values overlap,
    we can compare the first value in block 1, and the last in block 2

    sum(a + b + c) - sum(b + c + d) == a - d

    so comparing data[0] + data[1] + data[2] with data[1] + data[2] + data[3]
    is the same as comparing data[0] with data[3]
    or generalised data[index] with data[index + 3]
    """
    inc = 0
    for index in range(len(data) - 3):
        if data[index + 3] > data[index]:
            inc += 1
    return inc


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
