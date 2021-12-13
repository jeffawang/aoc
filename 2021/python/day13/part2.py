with open("inputs/day13") as f:
    raw = f.read().splitlines()

dots = [[int(n) for n in i.split(',')] for i in raw if ',' in i]
folds = [tuple(i.split()[-1].split("=")) for i in raw if 'fold' in i]

def fold(dots, coord, axis):
    for dot in dots:
        if dot[axis] > coord:
            dot[axis] = coord - (dot[axis]-coord)

for i, f in enumerate(folds):
    fold(dots, int(f[1]), 0 if f[0] == 'x' else 1)
    if i == 0:
        print("Part 1:", len(set(map(tuple,dots))))

print("Part 2:")
d = set(map(tuple,dots))
for y in range(max(i[1] for i in d)+1):
    for x in range(max(i[0] for i in d)+1):
        print("@@" if (x, y) in d else "  ", end='')
    print()
