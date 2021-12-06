from collections import defaultdict
with open("./inputs/day06") as f:
    raw = f.read()

fishes = defaultdict(int)
for i in [int(n) for n in raw.split(",")]:
    fishes[i] += 1

def gen(fish):
    d = defaultdict(int)
    for k, v in reversed(sorted(fish.items())):
        if k-1 == -1:
            d[6] += v
            d[8] += v
        else:
            d[k-1] += v
    return d

for i in range(80):
    fishes = gen(fishes)

print(sum(fishes.values()))