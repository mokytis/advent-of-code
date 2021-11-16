#!/usr/bin/env python

"""
Puzzle Title:     AoC 2020 Day 2: Password Philosophy
Puzzle Link:      https://adventofcode.com/2020/day/2
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip():
            data.append(line)
    return data


def parse_policy(line):
    policy, password = line.split(": ")
    amount, letter = policy.split(" ")
    low, high = amount.split("-")
    return int(low), int(high), letter, password


def check_password_1(line):
    low, high, letter, password = parse_policy(line)
    return int(low) <= password.count(letter) <= int(high)


def check_password_2(line):
    low, high, letter, password = parse_policy(line)
    return (password[low - 1] == letter) ^ (password[high - 1] == letter)


def solve_part1(data):
    return sum(map(check_password_1, data))


def solve_part2(data):
    return sum(map(check_password_2, data))


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
