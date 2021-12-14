import re
from collections import Counter

with open("inputs/day14") as f:
    polymer = f.readline()[:-1]
    f.readline()
    rules = dict(i.split(" -> ") for i in f.read().splitlines())

class List(object):
    def __init__(self, c, prev=None, next=None):
        self.c = c
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<{}>".format(self.c)

l = list(map(List, polymer))
for i, j in zip(l, l[1:]):
    i.next = j
    j.prev = i

def insert(node):
    n = node
    next = n.next
    while next:
        k = "{}{}".format(n.c, next.c)
        v = List(rules[k], n, next)
        n.next = v
        next.prev = v
        n = next
        next = next.next

def p(n):
    s = n.c
    while n.next:
        s = "{}{}".format(s, n.next.c)
        n = n.next
    return s

start = l[0]
for i in range(10):
    insert(start)
    print(i)
    # print(p(start))

s = p(start)
counts = sorted(Counter(s).values())
print("Part 1:", counts[-1] - counts[0])
print(Counter(s).values())
