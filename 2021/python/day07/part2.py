with open("inputs/day07") as f:
    p = [int(n) for n in f.read().split(",")]

found = False
for i in range(max(p)):
    # Sum of arithmetic series
    f = int(sum(abs(i-j) * ((1 + abs(i-j))/2) for j in p))
    if not found or f < fuels:
        found = True
        fuels = f

print(fuels)