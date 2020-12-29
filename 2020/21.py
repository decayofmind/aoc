import fileinput
from copy import deepcopy

data = [line.rstrip() for line in fileinput.input()]

a_l = []
A = set()
W = set()
T = {}

for l in data:
    l = l.split(' (contains ')
    el = []
    ags = [a for a in l[0].split(' ')]
    trs = [t for t in l[1].strip(')').split(', ')]
    W.update(ags)
    A.update(trs)
    el.append(ags)
    el.append(trs)
    a_l.append(el)

for a in A:
    hits = []
    for el in a_l:
        if a in el[1]:
            hits.append(set(el[0]))
    T[a] = set.intersection(*hits)

ans = {}

L = len(T)

while len(ans) != L:
    r = None
    items = T.items()
    for k,v in items:
        if len(v) == 1:
            r = T.pop(k).pop()
            ans.update({k: r})
            break

    for k,v in T.items():
        if r in v:
            T[k].remove(r)

p1 = 0

for x in range(len(a_l)):
    p1 += len(set(a_l[x][0]).difference(set(ans.values())))

print(p1)

ans = dict(sorted(ans.items()))
print(','.join(ans.values()))
