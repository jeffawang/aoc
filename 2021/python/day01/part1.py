with open("input2") as f:
    data = list(map(int, f.readlines()))

# increases = 0
# prev = data[0]
# for line in data[1:]:
#     if line > prev:
#         increases += 1
#     prev = line

# print(increases)

increases = 0
prev = sum(data[l-1:l+2])
for l in range(2, len(data)-1):
    line = sum(data[l-1:l+2])
    if prev < line:
        increases += 1
    prev = line
print(increases)
