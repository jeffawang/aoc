with open("inputs/day11") as f:
    raw = f.read().splitlines()

def adjacent(m, x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if 0 <= x+i < len(m) and 0 <= y+j < len(m[x]):
                yield (x+i, y+j)

def menum(m):
    for x in range(len(m)):
        for y in range(len(m[0])):
            yield (x,y)

def p(m):
    for r in m:
        print('hi', ''.join(map(str,r)))
    print()

def step(m):
    flashes = set()
    checkFlashes = []
    # Step 1: add 1 to everything
    for x, y in menum(m):
        m[x][y] += 1
        if m[x][y] > 9:
            checkFlashes.extend(adjacent(m,x,y))

    # Step 2: Flash
    i = -1
    while i < len(checkFlashes)-1:
        i += 1
        x, y = checkFlashes[i]
        if (x,y) in flashes:
            continue
        if m[x][y] > 9:
            flashes.add((x,y))
            for a, b in adjacent(m,x,y):
                if m[a][b] != 0:
                    m[a][b] += 1
            m[x][y] = 0
            checkFlashes.extend(adjacent(m,x,y))
    # p(m)
    return len(flashes)

m = [[int(c) for c in r] for r in raw]
flashes = 0
for i in range(100):
    flashes += step(m)
print(flashes)