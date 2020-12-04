#!/usr/bin/env python3


import re


def run():
    with open('input.txt', encoding='utf-8') as fh:
        data = fh.read().split('\n\n')

    required_fields = {
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
    }
    optional_fields = { 'cid' }
    valids1 = 0
    valids2 = 0
    for doc in data:
        d = {}
        pairs = re.split(r'[\n ]', doc)
        for pair in pairs:
            key, value = pair.split(':')
            d[key] = value.strip()
        if required_fields - set(d.keys()) == set():
            valids1 += 1
            if 1920 <= int(d['byr']) <= 2002 and \
                    2010 <= int(d['iyr']) <= 2020 and \
                    2020 <= int(d['eyr']) <= 2030 and \
                    (
                        (d['hgt'][-2:] == 'cm' and 150 <= int(d['hgt'][:-2]) <= 193) or
                        (d['hgt'][-2:] == 'in' and 59 <= int(d['hgt'][:-2]) <= 76)
                    ) and \
                    re.fullmatch(r'#[0-9a-f]{6}', d['hcl']) and \
                    d['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and \
                    re.fullmatch(r'[0-9]{9}', d['pid']):
                valids2 += 1
    print(valids1)  # first answer
    print(valids2)  # second answer


if __name__ == '__main__':
    run()
