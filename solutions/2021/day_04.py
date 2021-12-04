#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 4: Giant Squid
Puzzle Link:      https://adventofcode.com/2021/day/4
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
from dataclasses import dataclass


@dataclass
class Square:
    value: int
    called: bool = False


@dataclass
class BingoGrid:
    numbers: list[list[Square]]
    winning_num: int = -1

    def has_won(self):
        return self.winning_num != -1

    def play_num(self, num_called):
        cols_all_called = [True for _ in range(5)]
        for row in self.numbers:
            all_called = True
            for col, item in enumerate(row):
                if item.value == num_called:
                    item.called = True
                if item.called == False:
                    all_called = False
                    cols_all_called[col] = False
            if all_called:
                self.winning_num = num_called
        if sum(cols_all_called) > 0:
            self.winning_num = num_called


def parse_input():
    data = []
    grids = []
    grid = []
    for i, line in enumerate(fileinput.input()):
        line = line.rstrip()
        if i == 0:
            call_order = [int(num) for num in line.split(",")]
            continue
        if line:
            row = [Square(int(num)) for num in line.split(" ") if num]
            grid.append(row)
        else:
            if grid:
                grids.append(BingoGrid(grid))
                grid = []
    return call_order, grids


def play_until_winner(call_order, grids):
    for num in call_order:
        for grid in grids:
            grid.play_num(num)
            if grid.has_won():
                return grid


def play_until_last_winner(call_order, grids):
    winners = set()
    for num in call_order:
        for i, grid in enumerate(grids):
            grid.play_num(num)
            if grid.has_won():
                winners.add(i)
            if len(winners) == len(grids):
                return grid


def calculate_score(grid):
    score = 0
    for row in grid.numbers:
        for item in row:
            if not item.called:
                score += item.value
    score *= grid.winning_num
    return score


def solve_part1(call_order, grids):
    winning_grid = play_until_winner(call_order, grids)
    return calculate_score(winning_grid)


def solve_part2(call_order, grids):
    losing_grid = play_until_last_winner(call_order, grids)
    return calculate_score(losing_grid)


def main():
    call_order, grids = parse_input()

    part1_ans = solve_part1(call_order, grids)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(call_order, grids)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
