#!/usr/bin/env python3


def run():
    with open('input.txt', encoding='utf-8') as fh:
        data = [line.strip() for line in fh]

    max_id = -1
    ids = []
    for line in data:
        row = [0, 127]
        for char in line[:7]:
            if char == 'F':
                row[1] = row[1] - (row[1] - row[0]) // 2 - 1
            elif char == 'B':
                row[0] = row[0] + (row[1] - row[0]) // 2 + 1
        assert row[0] == row[1]
        col = [0, 7]
        for char in line[7:]:
            if char == 'L':
                col[1] = col[1] - (col[1] - col[0]) // 2 - 1
            elif char == 'R':
                col[0] = col[0] + (col[1] - col[0]) // 2 + 1
        assert col[0] == col[1]
        id_ = row[0] * 8 + col[0]
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
