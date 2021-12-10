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
for line in raw:
    stack = []
    for c in line:
        if c in s:
            stack.append(c)
        else:
            o = stack.pop()
            if c != d[o]:
                score += p[c]
print(score)
