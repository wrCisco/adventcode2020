#!/usr/bin/env python3

from math import sin, cos, radians

dirs = ('E', 'S', 'W', 'N')
instr = {
    'E': lambda x, d: [x[0] + d, x[1]],
    'W': lambda x, d: [x[0] - d, x[1]],
    'N': lambda x, d: [x[0], x[1] + d],
    'S': lambda x, d: [x[0], x[1] - d],
    'R': lambda f, d: dirs[(dirs.index(f) + (d // 90)) % len(dirs)],
    'L': lambda f, d: dirs[(dirs.index(f) - (d // 90)) % len(dirs)]
}

instr2 = {
    **instr,
    'F': lambda pos, waypoint, d: [pos[0]+waypoint[0]*d, pos[1]+waypoint[1]*d],
    'R': lambda waypoint, d: [
        int(waypoint[0]*cos(-d)) + int(waypoint[1]*sin(d)),
        int(waypoint[0]*sin(-d)) + int(waypoint[1]*cos(-d))
    ],
    'L': lambda waypoint, d: instr2['R'](waypoint, -d)
}

def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh]

    pos1 = [0, 0]  # H, V
    pos2 = [0, 0]
    facing = 'E'
    waypoint = [10, 1]
    for line in lines:
        d, n = line[0], int(line[1:])
        if d in dirs:
            pos1 = instr[d](pos1, n)
            waypoint = instr2[d](waypoint, n)
        elif d == 'F':
            pos1 = instr[facing](pos1, n)
            pos2 = instr2[d](pos2, waypoint, n)
        else:
            facing = instr[d](facing, n)
            waypoint = instr2[d](waypoint, radians(n))
    print(sum(map(abs, pos1)))  # first answer
    print(sum(map(abs, pos2)))  # second answer


if __name__ == '__main__':
    run()
