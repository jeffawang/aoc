with open("inputs/day09") as f:
    raw = f.read().splitlines()

c = [list([int(n) for n in i]) for i in raw]

def adjacent(c, m, n):
    v = c[m][n]
    for i in (-1, 1):
        a=m+i
        if 0 <= a < len(c) and c[a][n] != 9:
            yield (a,n)
    for i in (-1, 1):
        a=n+i
        if 0 <= a < len(c[m]) and c[m][a] != 9:
            yield (m,a)

mins = []
for i, row in enumerate(c):
    for j, val in enumerate(row):
        adj = adjacent(c,i,j)
        if all([val < c[a[0]][a[1]] for a in adj]):
            mins += [(i,j)]

basins = []
for m in mins:
    visited = set()
    visited.add(m)
    q = list(adjacent(c, m[0], m[1]))
    while len(q):
        n = q.pop(0)
        q.extend([a for a in adjacent(c, n[0], n[1]) if a not in visited])
        visited.add(n)
    basins.append(visited)

l = sorted(map(len,basins))
print(l[-1] * l[-2] * l[-3])