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
            # if player1 has the highest card, they're the winner, otherwise play the subgame
            winner = p1c if max(p1c) > max(p2c) else combat(p1c, p2c, True, set())
            if winner is p1c:
                w = p1
            else:
                w, c1, c2 = p2, c2, c1
        elif c1 > c2:
            w = p1
        else:
            w, c1, c2 = p2, c2, c1
        w.extend((c1, c2))
    return p1 if not len(p2) else p2


def run():
    with open('input.txt') as fh:
        p1, p2 = [
            deque(
                map(int, (n for n in seq.split('\n')))
            ) for seq in fh.read()[10:].split('\n\nPlayer 2:\n')
        ]

    winner = combat(p1.copy(), p2.copy(), False, set())
    print(sum(winner.pop() * i for i in range(1, len(winner) +1)))  # first answer

    winner = combat(p1, p2, True, set())
    print(sum(winner.pop() * i for i in range(1, len(winner) +1)))  # second answer


if __name__ == '__main__':
    run()
