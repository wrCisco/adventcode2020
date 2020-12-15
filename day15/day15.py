#!/usr/bin/env python3

from collections import deque

def run():
    with open('input.txt') as fh:
        nums = [int(n) for n in fh.read().split(',')]

    spoken = {num: deque([n], 2) for n, num in enumerate(nums, 1)}
    last = nums[-1]
    for turn in range(len(spoken) + 1, 30000001):
        if len(spoken[last]) == 1:
            n = 0
        else:
            n = spoken[last][1] - spoken[last][0]
        try:
            spoken[n].append(turn)
        except KeyError:
            spoken[n] = deque([turn], 2)
        last = n
        if turn == 2020:
            print(last)  # first answer
    print(last)  # second answer

if __name__ == '__main__':
    run()
