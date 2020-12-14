#!/usr/bin/env python3


from collections import defaultdict
import itertools
import re

def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh]

    mem = defaultdict(int)
    for line in lines:
        if line[:7] == 'mask = ':
            mask = line[7:]
        else:
            address, val = re.search(r'\[(\d+)\] = (\d+)', line).groups()
            masked_val = [
                bit if mask[i] == 'X' else mask[i] for i, bit in enumerate(f'{int(val):0>36b}')
            ]
            mem[address] = int(''.join(masked_val), 2)
    print(sum(mem.values()))  # first answer

    mem = defaultdict(int)
    for line in lines:
        if line[:7] == 'mask = ':
            mask = line[7:]
        else:
            address, val = re.search(r'\[(\d+)\] = (\d+)', line).groups()
            masked_addr = [
                bit if mask[i] == '0' else mask[i] for i, bit in enumerate(f'{int(address):0>36b}')
            ]
            floatings = itertools.product('01', repeat=masked_addr.count('X'))
            addresses = []
            for comb in floatings:
                addr = masked_addr.copy()
                for bit in comb:
                    addr[addr.index('X')] = bit
                addresses.append(''.join(addr))
            for addr in addresses:
                mem[addr] = int(val)
    print(sum(mem.values()))  # second answer

if __name__ == '__main__':
    run()
