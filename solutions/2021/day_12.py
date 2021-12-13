#!/usr/bin/env python

"""
Puzzle Title:     AoC 2021 Day 12: Passage Pathing
Puzzle Link:      https://adventofcode.com/2021/day/12
Solution Author:  Luke Spademan <info@lukespademan.com>
Solution License: MIT
"""

import fileinput
import copy
from dataclasses import dataclass


@dataclass
class Node:
    name: str
    connections: set[str]

    def is_small(self):
        return self.name.islower()


@dataclass
class Graph:
    nodes: dict[str, Node]


def parse_input():
    data = Graph({})
    for line in map(lambda x: x.rstrip(), fileinput.input()):
        if line:
            node1_name, node2_name = line.split("-")
            if node1_name not in data.nodes:
                node1 = Node(node1_name, set())
                data.nodes[node1_name] = node1
            else:
                node1 = data.nodes[node1_name]

            if node2_name not in data.nodes:
                node2 = Node(node2_name, set())
                data.nodes[node2_name] = node2
            else:
                node2 = data.nodes[node2_name]

            node1.connections.add(node2_name)
            node2.connections.add(node1_name)
    return data


def find_paths(graph, path=None):
    paths = []
    if path == None:
        path = ["start"]
    last_visited = path[-1]
    for n in graph.nodes[last_visited].connections:
        if graph.nodes[n].is_small() and n in path:
            continue
        np = copy.copy(path)
        np.append(n)
        if n == "end":
            paths.append(np)
        else:
            paths += find_paths(graph, np)
    return paths


def find_paths2(graph, path=None):
    paths = []
    if path == None:
        path = ["start"]
    last_visited = path[-1]
    for n in graph.nodes[last_visited].connections:
        if graph.nodes[n].is_small() and n in path:
            if n in ("start", "end"):
                continue
            small = [x for x in path if x.islower()]
            if len(small) >= len(set(small)) + 1:
                continue
        np = copy.copy(path)
        np.append(n)
        if n == "end":
            paths.append(np)
        else:
            paths += find_paths2(graph, np)
    return paths


def solve_part1(data):
    paths = find_paths(data)
    return len(paths)


def solve_part2(data):
    paths = find_paths2(data)
    return len(paths)


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
