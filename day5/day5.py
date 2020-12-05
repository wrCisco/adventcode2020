#!/usr/bin/env python3

import re

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

    # my solution
    # max_id = -1
    # ids = []
    # for line in data:
    #     row = calc_pos(line[:7], 128)
    #     col = calc_pos(line[7:], 8)
    #     id_ = row * 8 + col
    #     if id_ > max_id:
    #         max_id = id_
    #     ids.append(id_)
    # print(max_id)  # first answer

    # I thought of this one after a hint, many hours later...
    ids = [int(f"0b{re.sub(r'[FL]', '0', re.sub(r'[BR]', '1', line))}", 2) for line in data]
    
    ids.sort()
    print(ids[-1])  # first answer
    for i in range(len(ids) - 1):
        if ids[i] < ids[i+1] - 1:
            print(ids[i] + 1)  # second answer
            return

if __name__ == '__main__':
    run()
