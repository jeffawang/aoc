from collections import defaultdict
with open("./inputs/day05") as f:
    raw = f.read().splitlines()

lines = []
for line in raw:
    lines.append([ list(map(int, coord.split(','))) for coord in line.split(" -> ")])

d = defaultdict(int)

for line in lines:
    x1, x2 = line[0][0], line[1][0]
    y1, y2 = line[0][1], line[1][1]

    if x1 != x2 and y1 != y2:
        continue

    if y2 < y1:
        y1, y2 = y2, y1
    if x2 < x1:
        x1, x2 = x2, x1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            d[(i,j)] += 1

gt1 = {k: v for k, v in d.items() if v > 1}
print(len(gt1))