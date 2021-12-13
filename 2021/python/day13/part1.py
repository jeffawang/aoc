with open("inputs/day13") as f:
    raw = f.read().splitlines()

dots = [[int(n) for n in i.split(',')] for i in raw if ',' in i]
folds = [tuple(i.split()[-1].split("=")) for i in raw if 'fold' in i]

def fold(d, v, xFold):
    cmp = 0 if xFold else 1
    for i in range(len(d)):
        if d[i][cmp] > v:
            d[i][cmp] = v - (d[i][cmp] - v)

f = folds[0]
print(len(dots))
fold(dots, int(f[1]), f[0] == 'x')
print(len(dots))
print(len(set(map(tuple,dots))))