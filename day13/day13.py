#!/usr/bin/env python3

def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh]

    earliest = int(lines[0])
    buses = [(int(n), i) for i, n in enumerate(lines[1].split(',')) if n.isdigit()]
    waiting, bus = min(
        ((-(earliest % bus) + bus, bus) for bus, _ in buses),
        key=lambda x: x[0]
    )
    print(waiting * bus)  # first answer

    t = buses.pop(0)[0]
    start, step = t, t
    while buses:
        bus, delta = buses.pop(0)
        while (t + delta) % bus:
            t += step
        step *= bus
    print(t)  # second answer

if __name__ == '__main__':
    run()
