#!/usr/bin/env python3

import functools

def run():
    with open('input.txt', encoding='utf-8') as fh:
        groups = [group.split('\n') for group in fh.read().split('\n\n')]

    print(sum(len(set(''.join(group))) for group in groups))
    print(
        sum(
            len(
                functools.reduce(
                    lambda a,b: a & b, (set(person) for person in group)
                )
            ) for group in groups
        )
    )


if __name__ == '__main__':
    run()
