import numpy as np

with open ("inputs/day04") as f:
    raw = f.read().splitlines()

c = calls = raw[0].split(',')
bingos = [ i for i in raw[2:] if len(i) ]

i = iter(bingos)

bingos = list(zip(i,i,i,i,i))
b = bingos = list(map(lambda x: list(map(lambda y: y.split(), x)), bingos))

def evalBoard(board):
    board = np.array(board)
    if any(map(lambda x: all(map(lambda y: y in c, x)), board)):
        return True
    if any(map(lambda x: all(map(lambda y: y in c, x)), board.transpose())):
        return True
    return False



for i in range(1,len(calls)):
    c = calls[:i]
    print(len(c), c[-1])
    f = list(filter(evalBoard, b))
    if len(f):
        break

def bingoValue(board):
    global c
    sum = 0
    for row in board:
        for n in row:
            if n not in c:
                print('{:2}'.format(n), end=' ')
                sum += int(n)
            else:
                print('  ', end=' ')
        print()
    print(sum)
    print(int(c[-1]))
    return sum * int(c[-1])
    called = [ int(i) for row in board for i in row if i in c ]
    uncalled = [ int(i) for row in board for i in row if i not in c ]
    # return sum(uncalled) * int(c[-1])

print(bingoValue(f[0]))