#!/usr/bin/env python3

import re
import networkx as nx

def contained_bags(graph, node):
    tot = 0
    for neighbour in graph[node]:
        w = int(graph[node][neighbour]['weight'])
        tot += w + w * contained_bags(graph, neighbour)
    return tot

def run():
    with open('input.txt') as fh:
        rules = [line.strip() for line in fh]

    edges = []
    for rule in rules:
        node, neighbours = rule.split(' bags contain ')
        for neighbour in neighbours.split(', '):
            try:
                weight, neighbour_name = re.search(r'(\d+) ([a-z]+ [a-z]+) bags?', neighbour).groups()
            except AttributeError:
                pass
            else:
                edges.append((node, neighbour_name, weight))
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    print(len(nx.ancestors(G, 'shiny gold')))  # first answer
    print(contained_bags(G, 'shiny gold'))  # second answer

if __name__ == '__main__':
    run()
