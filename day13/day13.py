#!/usr/bin/env python3


def gcd(first: int, second: int) -> int:
    """
    Greatest common divisor.
    """
    while second != 0:
        first, second = second, first % second
    return abs(first)


def lcm(first: int, second: int) -> int:
    """
    Least common multiple.
    """
    if first == 0 or second == 0:
        return 0
    return abs(first * second) // gcd(first, second)


def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh]

    lowest = int(lines[0])
    buses = [int(n) for n in lines[1].split(',') if n != 'x']
    mintime = 9999999999999999999999999
    chosen = 0
    for bus in buses:
        mins = 0
        while mins < lowest:
            mins += bus
        if mins < mintime:
            mintime = mins
            chosen = bus
    print((mintime - lowest) * chosen)  # first answer

    buses = [(int(n), i) for i, n in enumerate(lines[1].split(',')) if n.isdigit()]
    t = buses.pop(0)[0]
    buses.sort(reverse=True)
    start, step = t, t
    while buses:
        bus, delta = buses.pop(0)
        while (t + delta) % bus:
            t += step
        step = lcm(step, bus)
    print(t)  # second answer


if __name__ == '__main__':
    run()
