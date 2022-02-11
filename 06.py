#!/usr/bin/env python

from typing import Dict

records = []

#  d = """COM)B
#  B)C
#  C)D
#  D)E
#  E)F
#  B)G
#  G)H
#  D)I
#  E)J
#  J)K
#  K)L
#  K)YOU
#  I)SAN"""

#  records = d.split('\n')

with open('input') as fp:
    for e in fp.readlines():
        records.append(e.strip())

orbits: Dict[str, list] = {}

for r in records:
    a, b = r.split(')')
    if orbits.get(a):
        orbits[a].append(b)
    else:
        orbits[a] = [b]

ends: Dict[str, list] = {}

for k, v in orbits.items():
    for i in v:
        if not orbits.get(i):
            ends[i] = []

orbits.update(ends)


def count_orbits(orbits, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not orbits.get(start):
        return None
    for node in orbits[start]:
        if node not in path:
            newpath = count_orbits(orbits, node, end, path)
            if newpath:
                return newpath
    return None


i = 0
for k in orbits.keys():
    i += len(count_orbits(orbits, 'COM', k)) - 1

print(i)

p1 = count_orbits(orbits, 'COM', 'YOU')
p2 = count_orbits(orbits, 'COM', 'SAN')


def list_diff(l1, l2):
    temp = set(l2)
    return [val for val in l1 if val not in temp]


print(len(list_diff(p1, p2)) + len(list_diff(p2, p1)) - 2)
