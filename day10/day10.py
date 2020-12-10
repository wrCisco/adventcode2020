#!/usr/bin/env python3

import itertools

def run():
    with open('input.txt') as fh:
        lines = [int(line.strip()) for line in fh]

    s = sorted(lines)
    diffs = [ 0, 0, 0 ]
    start = 0
    for n in s:
        if n == start + 1:
            diffs[0] += 1
        elif n == start + 2:
            diffs[1] += 1
        elif n == start + 3:
            diffs[2] += 1
        start = n
    diffs[2] += 1
    print(diffs[0] * diffs[2])  # first answer

    start = 0
    not_expendables = [0]
    s.insert(0, 0)
    for i in range(1, len(s) - 1):
        if abs(s[i - 1] - s[i + 1]) > 3:
            not_expendables.append(i)
    not_expendables.append(len(s) - 1)
    tot = 1
    for i in range(1, len(not_expendables)):
        diff = abs(s[not_expendables[i]] - s[not_expendables[i-1]])
        distance = not_expendables[i] - not_expendables[i-1]
        tot *= sum(len(list(itertools.combinations(s[not_expendables[i-1]+1:not_expendables[i]], n))) for n in range(max(0, diff - 3), distance))
    # not really a universal solution, but if differences between consecutive values in original sequence are all 1 and 3, it should hold
    print(tot)  # second answer


if __name__ == '__main__':
    run()
