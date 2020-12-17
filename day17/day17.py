#!/usr/bin/env python3

from itertools import product

nbrs4d = set(product((-1, 0, 1), repeat=4)) - {(0,0,0,0)}
nbrs3d = set(filter(lambda x: x[-1] == 0, nbrs4d))

def count_nbr_cubes(cubes, coords, nbrs):
    return sum(tuple(coords[i]+nbr[i] for i in range(len(nbr))) in cubes for nbr in nbrs)

def cycle(cubes, dimensions):
    deltas = nbrs3d if dimensions == 3 else nbrs4d
    for _ in range(6):
        next_cubes = set()
        void_nbrs = set()
        for coords in cubes:
            # all cube's neighbours
            nbrs = set(tuple(coords[i]+nbr[i] for i in range(len(coords))) for nbr in deltas)
            # all cubes in cube's neighbourhood
            nbrs_cubes = set(nbr for nbr in nbrs if nbr in cubes)
            # update set of all empty spaces around cubes
            void_nbrs.update(nbrs - nbrs_cubes)
            if len(nbrs_cubes) in (2, 3):
                next_cubes.add(coords)
        for coords in void_nbrs:
            if count_nbr_cubes(cubes, coords, deltas) == 3:
                next_cubes.add(coords)
        cubes = next_cubes
    return cubes

# alternative method, less efficient
def cycle2(cubes, dimensions):
    deltas = nbrs3d if dimensions == 3 else nbrs4d
    l = [(0, 1)] * 4  # range limits
    for _ in range(6):
        for i in range(dimensions):
            l[i] = (
                min(cubes, key=lambda x: x[i])[i] - 1,
                max(cubes, key=lambda x: x[i])[i] + 2
            )
        next_cubes = set()
        for w in range(l[3][0], l[3][1]):
            for z in range(l[2][0], l[2][1]):
                for y in range(l[1][0], l[1][1]):
                    for x in range(l[0][0], l[0][1]):
                        neighbours = count_nbr_cubes(cubes, (x, y, z, w), deltas)
                        if (
                            (x,y,z,w) in cubes and neighbours in (2, 3) or
                            (x,y,z,w) not in cubes and neighbours == 3
                        ):
                            next_cubes.add((x,y,z,w))
        cubes = next_cubes
    return cubes

def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh]

    cubes = set()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '#':
                cubes.add((x, y, 0, 0))

    print(len(cycle(cubes.copy(), 3)))  # first answer
    print(len(cycle(cubes, 4)))  # second answer

    # print(len(cycle2(cubes.copy(), 3)))
    # print(len(cycle2(cubes, 4)))

if __name__ == '__main__':
    run()
