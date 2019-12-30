#!/usr/bin/env python

import math
from decimal import Decimal
from collections import OrderedDict

FIELD = [l.strip() for l in open('input').readlines()]

F_Y = len(FIELD)
F_X = len(FIELD[0])

asteroids = []

for ny, y in enumerate(FIELD):
    for nx, x in enumerate(y):
        if x == '#':
            asteroids.append((nx, ny))

counts = []

F = {}

for c in asteroids:
    f = {}
    F[c] = {}
    count = 0
    for a in asteroids:
        if c[0] == a[0] and c[1] == a[1]:
            continue
        if c[0] == a[0]:
            k = math.inf
            b = c[1]
        else:
            k = Decimal(c[1] - a[1]) / Decimal(c[0] - a[0])
            b = (c[1] - (k * c[0]))

        index = (k, b)

        if f.get(index):
            f[index].append(a)
        else:
            f[index] = [a]

    for k, v in f.items():
        L = []
        R = []

        for i in v:
            if i[0] < c[0]:
                L.append(i)
            elif c[0] < i[0]:
                R.append(i)
            else:
                if i[1] < c[1]:
                    L.append(i)
                elif c[1] < i[1]:
                    R.append(i)

        if len(L) > 0:
            count += 1
        if len(R) > 0:
            count += 1

        F[c][math.degrees(math.atan(k[0]))] = {
            'L': sorted(L, key=lambda x: x[0]),
            'R': sorted(R, key=lambda x: x[0])
        }

    counts.append(count)

ans1 = max(counts)
print(ans1)

winner = None

assert len(asteroids) == len(counts)

for a, c in zip(asteroids, counts):
    if c == ans1:
        winner = F[a]

winner[-90.0] = winner.pop(90.0)

winner = OrderedDict(sorted(winner.items()))

i = 0
while i < len(asteroids) - 1:
    for k in winner.keys():
        if len(winner[k]['R']) > 0:
            c = winner[k]['R'].pop(0)
            i += 1
        if i == 200:
            print(c)
    for k in winner.keys():
        if len(winner[k]['L']) > 0:
            c = winner[k]['L'].pop()
            i += 1
        if i == 200:
            print(c)
