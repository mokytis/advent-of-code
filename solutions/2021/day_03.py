#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 3: Binary Diagnostic
Puzzle Link:      https://adventofcode.com/2021/day/3
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
import copy


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip():
            data.append(line.rstrip())
    return data


def solve_part1(data):
    bits = [0 for _ in range(12)]
    gamma = ""
    epsilon = ""
    for num in data:
        for i, bit in enumerate(num):
            if bit == "1":
                bits[i] += 1
            elif bit == "0":
                bits[i] -= 1
    for bit in bits:
        if bit > 0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def solve_part2(data):
    oxy = copy.copy(data)
    co2 = copy.copy(data)

    index = 0
    while len(oxy) > 1:
        oxy_one = []
        oxy_zero = []
        for num in oxy:
            if num[index] == "1":
                oxy_one.append(num)
            else:
                oxy_zero.append(num)
        if len(oxy_one) >= len(oxy_zero):
            oxy = oxy_one
        else:
            oxy = oxy_zero
        index += 1
    index = 0
    while len(co2) > 1:
        co2_one = []
        co2_zero = []
        for num in co2:
            if num[index] == "1":
                co2_one.append(num)
            else:
                co2_zero.append(num)
        if co2_one and (len(co2_one) < len(co2_zero)):
            co2 = co2_one
        else:
            co2 = co2_zero
        index += 1
    return int(oxy[0], 2) * int(co2[0], 2)


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
