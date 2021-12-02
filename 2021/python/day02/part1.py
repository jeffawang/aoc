with open("../../inputs/day02") as f:
    data = list(map(lambda x: x.split(), f.readlines()))

# (horizontal, depth)
def move(direction, amount):
    d = int(amount)
    if direction == "up":
        return (0, -d)
    elif direction == "down":
        return (0, d)
    elif direction == "forward":
        return (d, 0)

pos = (0, 0)
for line in data:
    pos = tuple(map(sum, zip(pos, move(*line))))

print(pos[0]*pos[1])
