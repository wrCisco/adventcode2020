#!/usr/bin/env python3

import itertools
import collections

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
        if s[i + 1] - s[i - 1] > 3:
            not_expendables.append(i)
    not_expendables.append(len(s) - 1)
    tot = 1
    for i in range(1, len(not_expendables)):
        diff = abs(s[not_expendables[i]] - s[not_expendables[i-1]])
        distance = not_expendables[i] - not_expendables[i-1]
        tot *= sum(len(list(itertools.combinations(s[not_expendables[i-1]+1:not_expendables[i]], n))) for n in range(max(0, diff - 3), distance))
    # this solution is valid since in the original (well, sorted) sequence
    # the difference between consecutive values is always 1 or 3, and
    # all sequences of elements with a difference of 1 from both
    # successor and predecessor are at most of length 4.
    print(tot)  # second answer method 1

    # this is something I'd like to have thought of by myself...
    combinations = collections.defaultdict(int)
    combinations[0] = 1
    for i in range(1, len(s)):
        for j in range(i - 1, -1, -1):
            if s[i] - s[j] > 3:
                break
            combinations[i] += combinations[j]
    print(combinations[len(s)-1])  # second answer method 2


if __name__ == '__main__':
    run()
