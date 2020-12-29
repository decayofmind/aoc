import fileinput
from copy import deepcopy

data = [line.rstrip() for line in fileinput.input()]

instr = []
field = {}

D = {
    'e': (1,0),
    'se': (0,1),
    'sw': (-1,1),
    'w': (-1,0),
    'nw': (0,-1),
    'ne': (1,-1)
}


for d in data:
    p = 0
    d = list(d)
    directions = []
    while p < len(d):
        if d[p] in ['n', 's'] and d[p+1] in ['e', 'w']:
            directions.append(''.join([str(x) for x in (d[p], d[p+1])]))
            p += 2
        else:
            directions.append(str(d[p]))
            p += 1
    instr.append(directions)


for i in instr:
    pos = [0,0]
    for m in i:
        pos[0] += D[m][0]
        pos[1] += D[m][1]

    pos = tuple(pos)
    field[pos] = 'b' if field.get(pos, 'w') == 'w' else 'w'

print(sum([1 for v in field.values() if v == 'b']))

dim = (min([d[0] for d in field.keys()]), max([d[0] for d in field.keys()]))

for q in range(dim[0],dim[1]+1):
    for r in range(dim[0],dim[1]+1):
        if not field.get((q,r), False):
            field[(q,r)] = 'w'

for _ in range(0,100):
    dim = (min([d[0] for d in field.keys()]), max([d[0] for d in field.keys()]))

    for q in range(dim[0]-1,dim[1]+2):
        for r in range(dim[0]-1,dim[1]+2):
            if not field.get((q, r), False):
                field[(q,r)] = 'w'

    new_field = deepcopy(field)

    state = list(field.items())
    for pos, c in state:
        blacks = 0
        for v in D.values():
            if field.get((pos[0]+v[0], pos[1]+v[1]), 'w') == 'b':
                blacks += 1
        if blacks == 0 or blacks > 2 and c == 'b':
            new_field[pos] = 'w'
        elif blacks == 2 and c == 'w':
            new_field[pos] = 'b'

    field = deepcopy(new_field)


print(sum([1 for v in field.values() if v == 'b']))
