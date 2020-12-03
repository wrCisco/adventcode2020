#!/usr/bin/env python3


import re


def encountered_trees(map_, dx, dy):
    x, y = 0, 0
    trees = 0
    while y < len(map_):
        if map_[y][x] == '#':
            trees += 1
        x += dx
        y += dy
    return trees


def run():
    with open('input.txt', encoding='utf-8') as fh:
        map_ = [line.rstrip() * 100 for line in fh.readlines()]

    print(encountered_trees(map_, 3, 1))  # first answer
    print(
        encountered_trees(map_, 1, 1) *
        encountered_trees(map_, 3, 1) *
        encountered_trees(map_, 5, 1) *
        encountered_trees(map_, 7, 1) *
        encountered_trees(map_, 1, 2)
    )  # second answer


if __name__ == '__main__':
    run()
