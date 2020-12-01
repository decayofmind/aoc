#!/usr/bin/env python

import re
from copy import deepcopy
from itertools import combinations
from math import gcd

step = 0
moons = []

for r in open('input').readlines():
    #  for r in open('input_test').readlines():
    m = re.match(r"^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", r)
    moon = {
        'pos': [int(m.group(1)),
                int(m.group(2)),
                int(m.group(3))],
        'vel': [0, 0, 0]
    }
    moons.append(moon)

pairs = list(combinations(list(range(len(moons))), 2))

initial_state = deepcopy(moons)

while step < 1000:
    # apply gravity
    for p in pairs:
        m1 = moons[p[0]]
        m2 = moons[p[1]]

        for c in range(3):
            if m1['pos'][c] < m2['pos'][c]:
                m1['vel'][c] += 1
                m2['vel'][c] -= 1
            elif m1['pos'][c] > m2['pos'][c]:
                m1['vel'][c] -= 1
                m2['vel'][c] += 1

    # apply velocity
    for m in moons:
        for c in range(3):
            m['pos'][c] += m['vel'][c]

    step += 1

energy = 0

for m in moons:
    pot = 0
    kin = 0
    for x in m['pos']:
        pot += abs(x)
    for x in m['vel']:
        kin += abs(x)

    energy += kin * pot

print(energy)

# PART2

# X
moons = deepcopy(initial_state)
step = 0

x_rep = 0

while True:
    # apply gravity
    for p in pairs:
        m1 = moons[p[0]]
        m2 = moons[p[1]]

        for c in range(3):
            if m1['pos'][c] < m2['pos'][c]:
                m1['vel'][c] += 1
                m2['vel'][c] -= 1
            elif m1['pos'][c] > m2['pos'][c]:
                m1['vel'][c] -= 1
                m2['vel'][c] += 1

    # apply velocity
    for m in moons:
        for c in range(3):
            m['pos'][c] += m['vel'][c]

    step += 1

    if ((moons[0]['pos'][0] == initial_state[0]['pos'][0])
            and (moons[1]['pos'][0] == initial_state[1]['pos'][0])
            and (moons[2]['pos'][0] == initial_state[2]['pos'][0])
            and (moons[3]['pos'][0] == initial_state[3]['pos'][0])
            and (moons[0]['vel'][0] == initial_state[0]['vel'][0])
            and (moons[1]['vel'][0] == initial_state[1]['vel'][0])
            and (moons[2]['vel'][0] == initial_state[2]['vel'][0])
            and (moons[3]['vel'][0] == initial_state[3]['vel'][0])):
        x_rep = step
        print(step)
        break

# Y
moons = deepcopy(initial_state)
step = 0

y_rep = 0

while True:
    # apply gravity
    for p in pairs:
        m1 = moons[p[0]]
        m2 = moons[p[1]]

        for c in range(3):
            if m1['pos'][c] < m2['pos'][c]:
                m1['vel'][c] += 1
                m2['vel'][c] -= 1
            elif m1['pos'][c] > m2['pos'][c]:
                m1['vel'][c] -= 1
                m2['vel'][c] += 1

    # apply velocity
    for m in moons:
        for c in range(3):
            m['pos'][c] += m['vel'][c]

    step += 1

    if ((moons[0]['pos'][1] == initial_state[0]['pos'][1])
            and (moons[1]['pos'][1] == initial_state[1]['pos'][1])
            and (moons[2]['pos'][1] == initial_state[2]['pos'][1])
            and (moons[3]['pos'][1] == initial_state[3]['pos'][1])
            and (moons[0]['vel'][1] == initial_state[0]['vel'][1])
            and (moons[1]['vel'][1] == initial_state[1]['vel'][1])
            and (moons[2]['vel'][1] == initial_state[2]['vel'][1])
            and (moons[3]['vel'][1] == initial_state[3]['vel'][1])):
        y_rep = step
        print(step)
        break

# Z
moons = deepcopy(initial_state)
step = 0

z_rep = 0

while True:
    # apply gravity
    for p in pairs:
        m1 = moons[p[0]]
        m2 = moons[p[1]]

        for c in range(3):
            if m1['pos'][c] < m2['pos'][c]:
                m1['vel'][c] += 1
                m2['vel'][c] -= 1
            elif m1['pos'][c] > m2['pos'][c]:
                m1['vel'][c] -= 1
                m2['vel'][c] += 1

    # apply velocity
    for m in moons:
        for c in range(3):
            m['pos'][c] += m['vel'][c]

    step += 1

    if ((moons[0]['pos'][2] == initial_state[0]['pos'][2])
            and (moons[1]['pos'][2] == initial_state[1]['pos'][2])
            and (moons[2]['pos'][2] == initial_state[2]['pos'][2])
            and (moons[3]['pos'][2] == initial_state[3]['pos'][2])
            and (moons[0]['vel'][2] == initial_state[0]['vel'][2])
            and (moons[1]['vel'][2] == initial_state[1]['vel'][2])
            and (moons[2]['vel'][2] == initial_state[2]['vel'][2])
            and (moons[3]['vel'][2] == initial_state[3]['vel'][2])):
        z_rep = step
        print(step)
        break


def lcm(a, b):
    return int(a * b // gcd(a, b))


print(lcm(lcm(x_rep, y_rep), z_rep))
