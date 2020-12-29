#!/usr/bin/env python3

from itertools import permutations

in_a = []
out_1 = []
out_2 = []

with open('input', 'r') as input:
    for line in input:
        in_a.append(int(line))


perms_2 = set(permutations(in_a, 2))
for p in perms_2:
    if p[0]+p[1] == 2020:
        out_1.append(p[0])
        out_1.append(p[1])


perms_3 = set(permutations(in_a, 3))
for p in perms_3:
    if p[0]+p[1]+p[2] == 2020:
        out_2.append(p[0])
        out_2.append(p[1])
        out_2.append(p[2])

out_1 = list(set(out_1))
print(out_1[0]*out_1[1])

out_2 = list(set(out_2))
print(out_2[0]*out_2[1]*out_2[2])
