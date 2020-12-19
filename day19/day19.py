#!/usr/bin/env python3

import re

def matches(rule, msgs):
    return sum(1 for msg in msgs if re.fullmatch(rule, msg))

def run():
    with open('input.txt') as fh:
        rules, msgs = fh.read().split('\n\n')
    msgs = msgs.split('\n')
    rules = {int(k): v.strip('"') for rule in rules.split('\n') for k, v in [rule.split(': ')]}

    completed = {k for k, v in rules.items() if v.isalpha()}
    while len(completed) < len(rules):
        for k, v in rules.items():
            for n in v.split(' '):
                if n.isdigit() and int(n) in completed:
                    rules[k] = re.sub(rf'\b{n}\b', rules[int(n)], v)
            if k not in completed and re.fullmatch(r'[()ab| ]+', v):
                if '|' in v:
                    v = '(' + v + ')'
                rules[k] = v.replace(' ', '')
                completed.add(k)

    print(matches(rules[0], msgs))  # first answer

    rules[8] = '(' + rules[42] + ')+'
    rules[11] = '(' + '|'.join((rules[42] * n + rules[31] * n for n in range(1, 6))) + ')'
    rules[0] = rules[8] + rules[11]

    print(matches(rules[0], msgs))  # second answer

if __name__ == '__main__':
    run()
