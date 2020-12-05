#!/usr/bin/env python3


def calc_pos(code, max_):
    pos = 0
    for c in code:
        max_ //= 2
        if c in ('B', 'R'):
            pos += max_
    return pos

def run():
    with open('input.txt', encoding='utf-8') as fh:
        data = [line.strip() for line in fh]

    max_id = -1
    ids = []
    for line in data:
        row = calc_pos(line[:7], 128)
        col = calc_pos(line[7:], 8)
        id_ = row * 8 + col
        if id_ > max_id:
            max_id = id_
        ids.append(id_)
    print(max_id)  # first answer
    ids.sort()
    for i in range(len(ids) - 1):
        if ids[i] < ids[i+1] - 1:
            print(ids[i] + 1)  # second answer
            return

if __name__ == '__main__':
    run()
