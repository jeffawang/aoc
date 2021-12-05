import numpy as np

with open ("inputs/day04") as f:
    lines = f.read().splitlines()

c = calls = np.array(lines[0].split(',')).astype(int)

i = iter( i for i in lines[2:] if len(i) )
b = [ np.array([ y.split() for y in x ]).astype(int) for x in zip(i,i,i,i,i) ]

def evalBoard(board, c):
    def checkRows(b):
        return any(all(y in c for y in x) for x in b)
    return checkRows(board) or checkRows(board.transpose())

def bingoValue(board, c):
    uncalled = [ int(i) for row in board for i in row if i not in c ]
    return sum(uncalled) * int(c[-1])

for i in range(5,len(calls)):
    c = calls[:i]
    f = list(filter(lambda x: evalBoard(x, c), b))
    if len(f):
        break

print(bingoValue(f[0], c))