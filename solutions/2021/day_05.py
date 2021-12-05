#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 5: Hydrothermal Venture
Puzzle Link:      https://adventofcode.com/2021/day/5
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
from dataclasses import dataclass


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_horizonal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_diagonal(self):
        return self.max_x() - self.min_x() == self.max_y() - self.min_y()

    def min_y(self):
        return min((self.y1, self.y2))

    def max_y(self):
        return max((self.y1, self.y2))

    def min_x(self):
        return min((self.x1, self.x2))

    def max_x(self):
        return max((self.x1, self.x2))

    def points(self):
        if self.x1 > self.x2:
            x_dir = -1
        else:
            x_dir = 1
        if self.y1 > self.y2:
            y_dir = -1
        else:
            y_dir = 1

        if self.is_diagonal():
            for x, y in zip(
                range(self.x1, self.x2 + x_dir, x_dir),
                range(self.y1, self.y2 + y_dir, y_dir),
            ):
                yield (x, y)
        else:
            for x in range(self.x1, self.x2 + x_dir, x_dir):
                for y in range(self.y1, self.y2 + y_dir, y_dir):
                    yield (x, y)


def parse_input():
    data = []
    for line in map(lambda l: l.rstrip(), fileinput.input()):
        if not line:
            continue
        point1, point2 = line.split(" -> ")
        x1, y1 = map(int, point1.split(","))
        x2, y2 = map(int, point2.split(","))
        data.append(Line(x1, y1, x2, y2))
    return data


def solve_part1(data):
    grid_squares = {}
    for line in data:
        if line.is_horizonal() or line.is_vertical():
            for point in line.points():
                if point not in grid_squares:
                    grid_squares[point] = 1
                else:
                    grid_squares[point] += 1

    return len([point for point in grid_squares if grid_squares[point] >= 2])


def solve_part2(data):
    grid_squares = {}
    for line in data:
        for point in line.points():
            if point not in grid_squares:
                grid_squares[point] = 1
            else:
                grid_squares[point] += 1

    return len([point for point in grid_squares if grid_squares[point] >= 2])


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
