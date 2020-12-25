#!/usr/bin/env python3

from functools import reduce

def step(val, subj):
    return (val * subj) % 20201227

def run():
    with open('input.txt') as fh:
        pks = [int(line) for line in fh]
    subj = 7
    k = 1
    i = 0
    while k != pks[0]:
        i += 1
        k = step(k, subj)
    print(reduce(step, [pks[1]] * i, 1))

    # to check both keys:
    # subj = 7
    # loop_sizes = []
    # for n in range(2):
    #     i = 0
    #     val = 1
    #     while val != pks[n]:
    #         i += 1
    #         val = step(val, subj)
    #     loop_sizes.append(i)
    # for n in range(2):
    #     val = 1
    #     for i in range(loop_sizes[n]):
    #         val = step(val, pks[(n+1)%len(pks)])
    #     print(val)

if __name__ == '__main__':
    run()
