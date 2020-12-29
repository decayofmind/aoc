#!/usr/bin/env python3

field = []
moves = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

with open('input', 'r') as input:
    for line in input:
        field.append(line.rstrip())


def count_trees(field, move):
    count = 0
    pos = (0,0)
    p_w = len(field[0])

    while True:
        if pos[1] >= len(field):
            break

        if field[pos[1]][pos[0]] == '#':
            count += 1

        pos = ((pos[0]+move[0])%p_w, pos[1]+move[1])

    return count


out = []

for move in moves:
    c = count_trees(field, move)
    out.append(c)

sum = 1

for el in out:
    sum = sum*el

print(sum)
