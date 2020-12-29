import fileinput
from functools import lru_cache
from copy import deepcopy

data = []

p1 = 0
p2 = 0

surround = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for line in fileinput.input():
    l = line.rstrip()
    data.append(list('.' + l + '.'))

floor = ['.'*len(data[0])]

data = floor + data + floor


def check_surround(d, r, c, conf):
    res = []
    if conf == (-1,-1):
        y = r-1
        x = c-1
        while y >= 0 and x>= 0:
            res.append(d[y][x])
            x -= 1
            y -= 1

    if conf == (-1,0):
        y = r-1
        while y >= 0:
            res.append(d[y][c])
            y -= 1

    if conf == (-1,1):
        y = r-1
        x = c+1
        while y >= 0 and x < len(d[y]):
            res.append(d[y][x])
            x += 1
            y -= 1

    if conf == (0,-1):
        res = d[r][:c]
        res.reverse()


    if conf == (0,1):
        res = d[r][c+1:]

    if conf == (1,-1):
        y = r+1
        x = c-1
        while y < len(d) and x >= 0:
            res.append(d[y][x])
            x -= 1
            y += 1

    if conf == (1,0):
        y = r+1
        while y < len(d):
            res.append(d[y][c])
            y += 1

    if conf == (1,1):
        y = r+1
        x = c+1
        while y < len(d) and x < len(d[r]):
            res.append(d[y][x])
            x += 1
            y += 1

    for r in res:
        if r in ['L', '#']:
            return r
    return '.'

while True:
    change = False
    next_data = deepcopy(data)
    for y in range(len(data)-2):
        for x in range(len(data[0])-2):
            Y = y+1
            X = x+1
            sur = []
            for s in surround:
                #  sur.append(data[Y+s[0]][X+s[1]])
                sur.append(check_surround(data, Y, X, s))
            if data[Y][X] == 'L':
                if '#' not in sur:
                    change = True
                    next_data[Y][X] = '#'
            if data[Y][X] == '#':
                #  if sur.count('#') >= 4:
                if sur.count('#') >= 5:
                    change = True
                    next_data[Y][X] = 'L'

    data = deepcopy(next_data)
    for r in data:
        print(' '.join(r))
    print('')
    if not change:
        break


for r in data:
    p1 += r.count('#')

print(p1)
