#!/usr/bin/env python3


def calc_pos(code, max_):
    min_ = 0
    for c in code:
        if c in ('F', 'L'):
            max_ = max_ - (max_ - min_) // 2 - 1
        else:
            min_ = min_ + (max_ - min_) // 2 + 1
    assert min_ == max_
    return min_

def run():
    with open('input.txt', encoding='utf-8') as fh:
        data = [line.strip() for line in fh]

    max_id = -1
    ids = []
    for line in data:
        row = calc_pos(line[:7], 127)
        col = calc_pos(line[7:], 7)
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
