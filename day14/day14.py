#!/usr/bin/env python3


import itertools
import re

def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh]

    mem1, mem2 = {}, {}
    for line in lines:
        if line[:7] == 'mask = ':
            mask = line[7:]
        else:
            address, val = re.search(r'\[(\d+)\] = (\d+)', line).groups()
            
            # part one
            masked_val = [
                bit if mask[i] == 'X' else mask[i] for i, bit in enumerate(f'{int(val):0>36b}')
            ]
            mem1[address] = int(''.join(masked_val), 2)

            # part two
            masked_addr = [
                bit if mask[i] == '0' else mask[i] for i, bit in enumerate(f'{int(address):0>36b}')
            ]
            floatings = itertools.product('01', repeat=masked_addr.count('X'))
            for comb in floatings:
                addr = masked_addr.copy()
                for bit in comb:
                    addr[addr.index('X')] = bit
                mem2[''.join(addr)] = int(val)
    print(sum(mem1.values()))  # first answer
    print(sum(mem2.values()))  # second answer

if __name__ == '__main__':
    run()
