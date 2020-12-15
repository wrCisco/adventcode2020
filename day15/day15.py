#!/usr/bin/env python3

# Running time (on my laptop) of today's solutions:
# day15.py with CPython3.7: ~5.3s
# day15.py with pypy3: ~1.2s
# day15.pyx compiled with Cython 0.29 in CPython3.7 console: ~3.7s
# day15.cpp compiled with g++ 7.5.0 with -Ofast: 0.8s

def run():
    with open('input.txt') as fh:
        nums = [int(n) for n in fh.read().split(',')]

    prevs = [0] * 30000000
    for i, n in enumerate(nums, 1):
        prevs[n] = i
    last = nums[-1]
    for turn in range(len(nums), 30000000):
        prevs[last], last = turn, turn - prevs[last] if prevs[last] else 0
        if turn == 2019:
            print(last)  # first answer
    print(last)  # second answer

if __name__ == '__main__':
    run()
