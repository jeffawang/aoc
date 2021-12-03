with open("inputs/day03") as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

l = len(data[0])

def count_ones(data):
    counts = [0] * l
    for line in data:
        for i in range(l):
            counts[i] += int(line[i])
    return counts

def most_common(data):
    counts = count_ones(data)
    total = len(data)
    return ''.join(["1" if i >= total/2 else "0" for i in counts])

def least_common(data):
    counts = count_ones(data)
    total = len(data)
    return ''.join(["1" if i < total/2 else "0" for i in counts])

counts = count_ones(data)

total = len(data)
mc = most_common(data)
lc = least_common(data)
gamma = int(mc, 2)
epsilon = int(lc, 2)
# print(gamma*epsilon)

d = data[:]
for i in range(l):
    mc = most_common(d)
    d = list(filter(lambda x: x[i] == mc[i], d))
    if len(d) == 1:
        oxygen = d[0]
        print("o2", oxygen)
        break

d = data[:]
for i in range(l):
    lc = least_common(d)
    d = list(filter(lambda x: x[i] == lc[i], d))
    if len(d) == 1:
        co2 = d[0]
        print("co2", co2)
        break

print("o2")
print(oxygen)
print(mc)
print("co2")
print(co2)
print(lc)

print(int(co2, 2) * int(oxygen, 2))

# wrong 10601536
# wrong 2722016