#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 10: Syntax Scoring
Puzzle Link:      https://adventofcode.com/2021/day/10
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
from statistics import median

INVALID_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

BRACKET_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def chunk_is_valid(chunk):
    opened = []
    for c in chunk:
        if c in BRACKET_PAIRS.keys():
            opened.append(c)
        else:
            if c != BRACKET_PAIRS[opened.pop()]:
                return c


def gen_completion_str(chunk):
    opened = []
    for c in chunk:
        if c in BRACKET_PAIRS.keys():
            opened.append(c)
        else:
            opened.pop()
    return "".join([BRACKET_PAIRS.get(c) for c in opened[::-1]])


def parse_input():
    data = []
    for line in map(lambda x: x.rstrip(), fileinput.input()):
        if line:
            data.append(line)
    return data


def solve_part1(data):
    score = 0
    for line in data:
        bracket = chunk_is_valid(line)
        if bracket:
            score += INVALID_SCORES[bracket]
    return score


def solve_part2(data):
    scores = []
    for line in data:
        if not chunk_is_valid(line):
            str_to_complete = gen_completion_str(line)
            score = 0
            for c in str_to_complete:
                score *= 5
                score += INCOMPLETE_SCORES[c]
            scores.append(score)
    return median(scores)


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
