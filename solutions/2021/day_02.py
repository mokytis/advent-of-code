#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 2: Dive!
Puzzle Link:      https://adventofcode.com/2021/day/2
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

from dataclasses import dataclass

import fileinput


@dataclass
class Instruction:
    direction: str
    magnitude: int


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip():
            direction, magnitude = line.split()
            data.append(Instruction(direction, int(magnitude)))
    return data


def solve_part1(data):
    x_pos = 0
    y_pos = 0
    for inst in data:
        match inst.direction:
            case "forward":
                x_pos += inst.magnitude
            case "down":
                y_pos += inst.magnitude
            case "up":
                y_pos -= inst.magnitude
    return x_pos * y_pos


def solve_part2(data):
    x_pos = 0
    y_pos = 0
    aim = 0
    for inst in data:
        match inst.direction:
            case "forward":
                x_pos += inst.magnitude
                y_pos += inst.magnitude * aim
            case "down":
                aim += inst.magnitude
            case "up":
                aim -= inst.magnitude
    return x_pos * y_pos


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
