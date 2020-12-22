#!/usr/bin/env python3


from collections import deque


def combat(p1, p2, second, prevs):
    while p1 and p2:
        tp1, tp2 = tuple(p1), tuple(p2)
        if (tp1, tp2) in prevs:
            return p1
        prevs.add((tp1, tp2))
        c1, c2 = p1.popleft(), p2.popleft()
        if second and c1 <= len(p1) and c2 <= len(p2):
            p1c = deque(list(p1)[:c1])
            p2c = deque(list(p2)[:c2])
            winner = combat(p1c, p2c, True, set())
            if winner is p1c:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        elif c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    return p1 if len(p1) > len(p2) else p2


def run():
    with open('input.txt') as fh:
        players = [deque(), deque()]
        i = -1
        for line in fh:
            if line.startswith('Player'):
                i += 1
                continue
            if line.strip():
                players[i].append(int(line.strip()))
    p1, p2 = players[0], players[1]

    winner = combat(p1.copy(), p2.copy(), False, set())
    print(sum(winner.pop() * i for i in range(1, len(winner) +1)))  # first answer

    winner = combat(p1, p2, True, set())
    print(sum(winner.pop() * i for i in range(1, len(winner) +1)))  # second answer


if __name__ == '__main__':
    run()
