#!/usr/bin/env python3


import re
from collections import defaultdict


dirs = {
    'e': 1j,
    'w': -1j,
    'ne': 1+1j,
    'sw': -1-1j,
    'nw': 1,
    'se': -1
}


def floor_size(tiles):
    return int(max((max(abs(v.real), abs(v.imag)) for v in tiles.keys())))


def run():
    with open('input.txt') as fh:
        instr = [re.findall(r'(se|sw|nw|ne|w|e)', line.strip()) for line in fh]

    tiles = defaultdict(bool)

    for i in instr:
        pos = 0
        for step in i:
            pos += dirs[step]
        tiles[pos] = not tiles[pos]

    print(sum(tiles.values()))  # first answer

    fsize = floor_size(tiles)
    limits = [-fsize-1, fsize+2] 
    for _ in range(100):
        ts = tiles.copy()
        for r in range(limits[0], limits[1]):
            for i in range(limits[0], limits[1]):
                pos = r+complex(0, i)
                color = ts.get(pos, False)
                nbrs = sum(ts.get(pos+nbr, False) for nbr in dirs.values())
                if (color and (nbrs == 0 or nbrs > 2)) or (not color and nbrs == 2):
                    tiles[pos] = not color
        fsize = floor_size(tiles)
        limits = [-fsize-1, fsize+2] 

    print(sum(tiles.values()))  # second answer


if __name__ == '__main__':
    run()
