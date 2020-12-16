#!/usr/bin/env python3

from functools import reduce
import math
import re

def check_rule(rules, name, x):
    n1, n2, n3, n4 = rules[name]
    return n1 <= x <= n2 or n3 <= x <= n4

def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh if line.strip()]

    part = 0
    rules = {}
    your_ticket: list
    nearby_tickets = []
    for i, line in enumerate(lines):
        if line[:4] in ('your', 'near'):
            part += 1
            continue
        if not part:
            name = line[:line.index(':')]
            rules[name] = [int(x) for x in re.findall(r'\d+', line[line.index(':')+1:])]
        elif part == 1:
            your_ticket = [int(x) for x in line.split(',')]
        else:
            nearby_tickets.append(tuple(int(x) for x in line.split(',')))

    error_rate = 0
    valids = set()
    for ticket in nearby_tickets:
        valid = True
        for n in ticket:
            for rule in rules.keys():
                if check_rule(rules, rule, n):
                    break
            else:
                error_rate += n
                valid = False
        if valid:
            valids.add(ticket)

    print(error_rate)  # first answer

    possible_fields = {n: set(rules.keys()) for n in range(len(rules))}
    for ticket in valids:
        for i, n in enumerate(ticket):
            for rule in rules.keys():
                if not check_rule(rules, rule, n):
                    possible_fields[i].discard(rule)

    fields = {}
    while possible_fields.keys():
        for i, field in possible_fields.items():
            if len(field) == 1:
                fields[i] = list(field)[0]
                for f in possible_fields.values():
                    f.discard(fields[i])
                del possible_fields[i]
                break
        else:
            break

    # python3.8 and up
    # print(math.prod(your_ticket[k] for k, field in fields.items() if field.startswith('departure')))
    print(
        reduce(
            lambda x, y: x * y,
            (your_ticket[k] for k, field in fields.items() if field.startswith('departure')),
            1
        )
    )  # second answer


if __name__ == '__main__':
    run()
