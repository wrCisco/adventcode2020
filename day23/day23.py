#!/usr/bin/env python3


def play(rounds, current, cups):
    for _ in range(rounds):
        picked = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
        dest = current - 1 if current > 1 else len(cups) - 1
        while dest in picked:
            dest = dest - 1 if dest > 1 else len(cups) - 1
        cups[current] = cups[picked[-1]]
        cups[picked[-1]] = cups[dest]
        cups[dest] = picked[0]
        current = cups[current]


def run():
    with open('input.txt') as fh:
        values = [int(n) for n in fh.read().strip()]
    cups = [ None ] * (len(values) + 1)
    for i in range(len(values)):
        cups[values[i]] = values[(i+1)%len(values)]

    play(100, values[0], cups)
    c = 1
    for _ in range(8):
        print(cups[c], end='')  # first answer
        c = cups[c]
    print('')

    cups = [i for i in range(1, 1000002)]
    cups[-1] = values[0]
    for i in range(len(values)):
        cups[values[i]] = values[(i+1)%len(values)]
    cups[values[-1]] = len(values) + 1

    play(10000000, values[0], cups)
    print(cups[1] * cups[cups[1]])  # second answer


if __name__ == '__main__':
    run()
