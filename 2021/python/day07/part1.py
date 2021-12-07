with open("inputs/day07") as f:
    p = [int(n) for n in f.read().split(",")]

found = False
for i in range(max(p)):
    f = sum(abs(i-j) for j in p)
    if not found or f < fuels:
        found = True
        fuels = f

print(fuels)