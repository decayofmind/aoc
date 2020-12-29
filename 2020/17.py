import fileinput
from collections import defaultdict
from copy import deepcopy
from itertools import product

data = [line.rstrip() for line in fileinput.input()]

world = defaultdict(lambda: '.')
#  surround = list(product([-1,0,1], repeat=3))
surround = list(product([-1,0,1], repeat=4))
#  surround.remove((0,0,0))
surround.remove((0,0,0,0))
turn = 0


for y in range(len(data)):
    for x in range(len(data[0])):
        #  world[(x,y,0)] = data[y][x]
        world[(x,y,0,0)] = data[y][x]


while True:
    turn += 1
    cur_dims = []
    #  for dim in range(3):
    for dim in range(4):
        m = min(world.keys(), key=lambda k: k[dim])
        M = max(world.keys(), key=lambda k: k[dim])
        cur_dims.append((m[dim],M[dim]))

    for m,M in cur_dims:
        for w in range(m-1,M+2):
            for z in range(m-1,M+2):
                for y in range(m-1,M+2):
                    for x in range(m-1,M+2):
                        if not world.get((x,y,z,w), False):
                            world[x,y,z,w] = '.'

    new_world = deepcopy(world)

    items = list(world.items())
    for k,v in items:
        act = 0
        for c in surround:
            if world[(k[0]+c[0],k[1]+c[1],k[2]+c[2],k[3]+c[3])] == '#':
                act += 1

        if v == '#':
            if 2 <= act <= 3:
                new_world[k] = v
            else:
                new_world[k] = '.'

        if v == '.':
            if act == 3:
                new_world[k] = '#'

    world = deepcopy(new_world)

    if turn == 6:
        break

p1 = 0

for v in world.values():
    if v == '#':
        p1 += 1

print(p1)
