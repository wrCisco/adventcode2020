#!/usr/bin/env python3


import re
from functools import reduce


dirs = {
    'e': 1j,
    'w': -1j,
    'ne': 1+1j,
    'sw': -1-1j,
    'nw': 1,
    'se': -1
}


def floor_size(tiles):
    return int(max((max(abs(v.real), abs(v.imag)) for v in tiles)))


def run():
    with open('input.txt') as fh:
        instr = [re.findall(r'(se|sw|nw|ne|w|e)', line.strip()) for line in fh]

    tiles = reduce(
        lambda x, y: x ^ {y},
        (sum(dirs[step] for step in i) for i in instr),
        set()
    )

    print(len(tiles))  # first answer

    fsize = floor_size(tiles)
    limits = [-fsize-1, fsize+2]
    for _ in range(100):
        ts = tiles.copy()
        for r in range(limits[0], limits[1]):
            for i in range(limits[0], limits[1]):
                pos = complex(r, i)
                color = pos in ts
                nbrs = sum(pos+nbr in ts for nbr in dirs.values())
                if (color and (nbrs == 0 or nbrs > 2)) or (not color and nbrs == 2):
                    tiles.remove(pos) if pos in tiles else tiles.add(pos)
        fsize = floor_size(tiles)
        limits = [-fsize-1, fsize+2]

    print(len(tiles))  # second answer


if __name__ == '__main__':
    run()
