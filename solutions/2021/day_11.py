#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 11: Dumbo Octopus
Puzzle Link:      https://adventofcode.com/2021/day/11
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
import copy


def parse_input():
    data = []
    for line in map(lambda x: x.rstrip(), fileinput.input()):
        if line:
            data.append([int(octopus) for octopus in line])
    return data


def get_neighbours(x, y):
    return filter(
        lambda coord: 0 <= coord[0] <= 9 and 0 <= coord[1] <= 9,
        [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ],
    )


def flash(x, y, grid, flashed):
    if grid[x][y] >= 10:
        flashed.add((x, y))
        grid[x][y] = 0
        for nx, ny in get_neighbours(x, y):
            if (nx, ny) not in flashed and grid[nx][ny] != 0:
                grid[nx][ny] += 1
                flash(nx, ny, grid, flashed)
    return changed


def flash_cycle(grid):
    to_flash = set()
    flashed = set()
    for x, row in enumerate(grid):
        for y, item in enumerate(row):
            grid[x][y] += 1
            if grid[x][y] > 9:
                to_flash.add((x, y))
    while to_flash:
        for x, y in copy.copy(to_flash):
            grid[x][y] = 0
            to_flash.remove((x, y))
            flashed.add((x, y))
            for nx, ny in get_neighbours(x, y):
                if grid[nx][ny] == 0:
                    continue
                grid[nx][ny] += 1
                if grid[nx][ny] > 9:
                    to_flash.add((nx, ny))
    return len(flashed)


def solve_part1(data):
    flashes = 0
    for _ in range(100):
        flashes += flash_cycle(data)
    return flashes


def solve_part2(data):
    i = 1
    while True:
        if flash_cycle(data) == 100:
            return i
        i += 1


def main():
    data = parse_input()

    part1_ans = solve_part1(copy.deepcopy(data))
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(copy.deepcopy(data))
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
