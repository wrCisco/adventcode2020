#!/usr/bin/env python3


import collections


def run():
    with open('input.txt') as fh:
        lines = [int(line.strip()) for line in fh]

    for i, num in enumerate(lines[25:], 25):
        sums = set()
        for n in lines[i-25:i]:
            if n in sums:
                break
            else:
                sums.add(num - n)
        else:
            print(num)  # first answer
            break

    target = num
    contiguous = collections.deque()
    tot = 0
    i = 0
    while i < len(lines):
        if tot < target:
            contiguous.append(lines[i])
            tot += lines[i]
            i += 1
        elif tot > target:
            tot -= contiguous.popleft()
        else:
            break
    else:
        while len(contiguous):
            tot -= contiguous.popleft()
            if tot == target:
                break
    print(min(contiguous) + max(contiguous))  # second answer

if __name__ == '__main__':
    run()
