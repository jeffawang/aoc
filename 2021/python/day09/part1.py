with open("inputs/day09") as f:
    raw = f.read().splitlines()

c = [list([int(n) for n in i]) for i in raw]

def adjacent(c, m, n):
    for i in (-1, 1):
        a=m+i
        if not (a < 0 or a >= len(c)):
            yield c[a][n]
    for i in (-1, 1):
        a=n+i
        if not (a < 0 or a >= len(c[m])):
            yield c[m][a]

mins = []
for i, row in enumerate(c):
    for j, val in enumerate(row):
        adj = adjacent(c,i,j)
        if all([val < a for a in adj]):
            mins += [val]

print(sum(mins) + len(mins))
