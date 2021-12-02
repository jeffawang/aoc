with open("../../inputs/day02") as f:
    data = list(map(lambda x: x.split(), f.readlines()))

# (horizontal, depth, aim)
def move(direction, amount, aim):
    d = int(amount)
    if direction == "up":
        return (0, 0, -d)
    elif direction == "down":
        return (0, 0, d)
    elif direction == "forward":
        return (d, aim*d, 0)

pos = (0, 0, 0)
for line in data:
    pos = tuple(map(sum, zip(pos, move(line[0], line[1], pos[2]))))
    print(line, pos)

print(pos[0]*pos[1])
