#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 13: Transparent Origami
Puzzle Link:      https://adventofcode.com/2021/day/13
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
from dataclasses import dataclass
import copy


@dataclass
class Fold:
    axis: str
    value: int


def parse_input():
    points = set()
    folds = []
    for line in map(lambda x: x.rstrip(), fileinput.input()):
        if line:
            if line.startswith("fold along "):
                axis, value = line[11:].split("=")
                folds.append(Fold(axis, int(value)))
            else:
                num1, num2 = line.split(",")
                points.add((int(num1), int(num2)))
    return points, folds


def fold_points(points, fold):
    if fold.axis == "x":
        i = 0
    else:
        i = 1
    for point in copy.copy(points):
        if point[i] == fold.value:
            points.remove(point)
        elif point[i] > fold.value:
            points.remove(point)
            distance = point[i] - fold.value
            if i == 0:
                points.add((fold.value - distance, point[1]))
            else:
                points.add((point[0], fold.value - distance))
    return len(points)


def output(points):
    ys = [point[1] for point in points]
    xs = [point[0] for point in points]
    for row in range(min(ys), max(ys) + 1):
        for value in range(min(xs), max(xs) + 1):
            if (value, row) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def solve_part1(points, fold):
    return fold_points(points, fold)


def solve_part2(points, folds):
    for fold in folds:
        fold_points(points, fold)

    output(points)


def main():
    points, folds = parse_input()

    part1_ans = solve_part1(points, folds[0])
    print(f"Part 1: {part1_ans}")

    print("Part 2:")
    solve_part2(points, folds)


if __name__ == "__main__":
    main()
