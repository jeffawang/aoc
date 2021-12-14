import re
from collections import Counter, defaultdict

with open("inputs/day14") as f:
    polymer = f.readline()[:-1]
    f.readline()
    rules = dict(i.split(" -> ") for i in f.read().splitlines())

pairs = zip(polymer, polymer[1:])
start = defaultdict(int)
for pair in pairs:
    start[pair] += 1

def insert(pairs):
    newpairs = defaultdict(int)
    for pair, count in pairs.items():
        v = rules[''.join(pair)]
        p1 = (pair[0], v)
        p2 = (v, pair[1])
        newpairs[p1] += count
        newpairs[p2] += count
    return newpairs

def counts(pairs):
    counts = defaultdict(int)
    counts[polymer[0]] += 1
    for pair, count in pairs.items():
        counts[pair[1]] += count
    return counts

def output(pairs):
    c = sorted(counts(pairs).values())
    return c[-1] - c[0]

pairs = start
for i in range(40):
    pairs = insert(pairs)
    if i == 9:
        print("Part 1:", output(pairs))

print("Part 2:", output(pairs))