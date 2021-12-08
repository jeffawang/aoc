with open("inputs/day08") as f:
    raw = f.read().splitlines()

o = [a.split("|")[1].split() for a in raw]

count = sum(sum(1 for i in l if len(i) in (2,3,4,7)) for l in o)
print(count)
