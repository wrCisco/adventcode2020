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

    pos = [0, 0]  # H, V
    facing = 'E'
    for line in lines:
        d = line[0]
        if d in dirs:
            pos = instr[d](pos, int(line[1:]))
        elif d == 'F':
            pos = instr[facing](pos, int(line[1:]))
        else:
            facing = instr[d](facing, int(line[1:]))
    print(sum(map(abs, pos)))  # first answer

    pos = [0, 0]
    waypoint = [10, 1]
    for line in lines:
        d = line[0]
        if d in dirs:
            waypoint = instr2[d](waypoint, int(line[1:]))
        elif d == 'F':
            pos = instr2[d](pos, waypoint, int(line[1:]))
        else:
            waypoint = instr2[d](waypoint, radians(int(line[1:])))
    print(sum(map(abs, pos)))  # second answer


if __name__ == '__main__':
    run()