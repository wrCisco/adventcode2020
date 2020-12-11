#!/usr/bin/env python3


from collections import defaultdict
from copy import deepcopy

nbrs = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1)
)

def nbrs_vals(map_, seats, x, y):
    return sum(seats[(x+nbr[0], y+nbr[1])] for nbr in nbrs)

def seen_vals(map_, x, y):
    occupied = 0
    for direction in nbrs:
        x1, y1 = x + direction[0], y + direction[1]
        while 0 <= x1 < len(map_[0]) and 0 <= y1 < len(map_):
            if map_[y1][x1] == '#':
                occupied += 1
                break
            elif map_[y1][x1] == 'L':
                break
            x1 += direction[0]
            y1 += direction[1]
    return occupied

def is_to_update(map_, seats, x, y):
    vals = nbrs_vals(map_, seats, x, y)
    if (map_[y][x] == 'L' and vals == 0) or (map_[y][x] == '#' and vals >= 4):
        return True
    return False

def is_to_update2(map_, seats, x, y):
    vals = seen_vals(map_, x, y)
    if (map_[y][x] == 'L' and vals == 0) or (map_[y][x] == '#' and vals >= 5):
        return True
    return False

def update(map_, seats, x, y):
    map_[y][x] = '#' if map_[y][x] == 'L' else 'L'
    seats[(x, y)] = 1 if seats[(x, y)] == 0 else 0

def cycle_until_stable(map_, is_to_update_func):
    seats = defaultdict(int)
    to_update = [1]
    while to_update:
        to_update = []
        for y, row in enumerate(map_):
            for x in range(len(row)):
                if is_to_update_func(map_, seats, x, y):
                    to_update.append((x, y))
        for pos in to_update:
            update(map_, seats, pos[0], pos[1])
    return sum(seats.values())

def run():
    with open('input.txt') as fh:
        map1 = [[seat for seat in line.strip()] for line in fh]
    map2 = deepcopy(map1)
    print(cycle_until_stable(map1, is_to_update))  # first answer
    print(cycle_until_stable(map2, is_to_update2))  # second answer

if __name__ == '__main__':
    run()
