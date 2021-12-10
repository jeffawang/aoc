with open("inputs/day10") as f:
    raw = f.read().splitlines()

d = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
s = list(d.keys())
e = list(d.values())
delims = s+e

p = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
incomplete_lines = []
stacks = []
for line in raw:
    stack = []
    poo = False
    for c in line:
        if c in s:
            stack.append(c)
        else:
            o = stack.pop()
            if c != d[o]:
                poo = True
                break
    if not poo:
        stacks.append(stack)

p2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def score(stack):
    score = 0
    for c in reversed(stack):
        score *= 5
        score += p2[d[c]]
    return score

scores = sorted([score(stack) for stack in stacks])
from math import floor
print(scores[floor(len(scores)/2)])
