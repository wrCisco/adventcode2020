#!/usr/bin/env python3

import re

def run():
    with open('input.txt', encoding='utf-8') as fh:
        database = [line.rstrip().split(': ') for line in fh.readlines()]

    valids1 = 0
    valids2 = 0
    for policy, password in database:
        min_, max_, char = re.split(r'[- ]', policy)
        min_ = int(min_)
        max_ = int(max_)
        if min_ <= password.count(char) <= max_:
            valids1 += 1
        if (password[min_-1] == char) ^ (password[max_-1] == char):
            valids2 += 1
    print(valids1)  # first answer
    print(valids2)  # second answer

if __name__ == '__main__':
    run()
