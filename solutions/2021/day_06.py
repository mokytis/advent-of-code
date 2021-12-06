#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 6: Lanternfish
Puzzle Link:      https://adventofcode.com/2021/day/6
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
from collections import Counter
import copy


def parse_input():
    for line in fileinput.input():
        if line.strip():
            return Counter([int(timer) for timer in line.rstrip().split(",")])


def fishes_after_days(fishes, days):
    # children get held for 2 days before being added to the general population
    children = [0, 0]

    for day in range(days + 1):
        for timer in range(7):
            offset_timer = (timer - day) % 7
            if offset_timer == 6:
                children.append(fishes[timer])
                fishes[timer] += children.pop(0)

    return sum([fishes[t] for t in fishes]) + sum(children)


def solve_part1(data):
    return fishes_after_days(data, 80)


def solve_part2(data):
    return fishes_after_days(data, 256)


def main():
    data = parse_input()

    part1_ans = solve_part1(copy.copy(data))
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(copy.copy(data))
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
