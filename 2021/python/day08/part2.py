with open("inputs/day08") as f:
    raw = f.read().splitlines()

s = [a.split("|") for a in raw]
i = [a[0] for a in s]
o = [a[1].split() for a in s]

v = [a.split() for a in raw]
v = [[set(i) for i in x if i != '|'] for x in v]

def count(l, n):
    return [a for a in l if len(a) == n][0]

#   8:
#  aaaa 
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 

output = 0
for r in v:
    l = [len(x) for x in r]
    one = count(r, 2)
    four = count(r, 4)
    seven = count(r, 3)
    eight = count(r, 7)

    a = (seven - one).pop()

    nine = [i for i in r if (len(i) == 6 and len(i-four-seven) == 1)][0]
    g = (nine-four-seven).pop()
    e = (eight-nine).pop()

    three = [i for i in r if (len(i) == 5 and len(i-seven-set(g))==1)][0]
    d = (three-seven-set(g)).pop()

    two = [i for i in r if (len(i) == 5 and len(i-set([a,g,d,e]))==1)][0]
    c = (two-set([a,g,d,e])).pop()

    f = (three - set([a,c,d,g])).pop()
    b = (eight - set([a,c,d,e,f,g])).pop()

    def mk(x):
        return ''.join(sorted(x))

    key = {
        mk([a,b,c,e,f,g]): '0',
        mk([c,f]): '1',
        mk([a,c,d,e,g]): '2',
        mk([a,c,d,f,g]): '3',
        mk([b,c,d,f]): '4',
        mk([a,b,d,f,g]): '5',
        mk([a,b,d,e,f,g]): '6',
        mk([a,c,f]): '7',
        mk([a,b,c,d,e,f,g]): '8',
        mk([a,b,c,d,f,g]): '9'
    }

    # output is always 4 digits long
    output += int(''.join([key[mk(i)] for i in r[-4:]]))
print(output)