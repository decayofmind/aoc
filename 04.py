#!/usr/bin/env python

from typing import Dict

start = 123257
stop = 647015

ans1 = []

for i in range(start, stop):
    n = [int(d) for d in str(i)]
    for d in range(len(n) - 1):
        if n[d + 1] >= n[d]:
            pass
        else:
            good = False
            break
        good = True

    if len(set(n)) < len(n) and good:
        ans1.append(i)

print(len(ans1))

ans2 = []

for i in ans1:
    n = [int(d) for d in str(i)]
    hits: Dict[int, int] = {}
    groups = {}

    for d in n:
        if hits.get(d):
            hits[d] += 1
        else:
            hits[d] = 1

    for k, v in hits.items():
        if v >= 2:
            groups[k] = v

    if len(groups) > 0 and 2 in groups.values():
        print(i)
        ans2.append(i)

print(len(ans2))
