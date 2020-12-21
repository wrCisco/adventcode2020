#!/usr/bin/env python3


def run():
    with open('input.txt') as fh:
        lines = [line.strip() for line in fh]

    foods = []
    ingredients = set()
    allergens = {}
    for line in lines:
        ingrs = set(line[:line.index('(')-1].split(' '))
        allers = set(line[line.index('(contains ')+10:-1].split(', '))
        foods.extend(ingrs)
        ingredients.update(ingrs)
        for aller in allers:
            try:
                allergens[aller] &= ingrs
            except KeyError:
                allergens[aller] = set(ingrs)
    anallergics = ingredients.copy()
    for k, v in allergens.items():
        anallergics -= v

    print(
        sum(foods.count(ingr) for ingr in anallergics)
    )  # first answer

    while any(len(v) > 1 for v in allergens.values()):
        for k, v in allergens.items():
            if len(v) == 1:
                for other_k, other_v in allergens.items():
                    if len(other_v) > 1:
                        other_v.discard(list(v)[0])

    print(
        ','.join(
            str(list(v)[0]) for k, v in sorted(allergens.items(), key=lambda x: x[0])
        )
    )  # second answer


if __name__ == '__main__':
    run()
