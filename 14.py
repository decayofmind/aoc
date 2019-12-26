#!/usr/bin/env python

reactions = {}
for line in open('input').readlines():
#  for line in open('test_input').readlines():
    consume, produce = line.strip().split('=>')
    produce_qty, produce_type = produce.lstrip(' ').rstrip(' ').split(' ')
    consume = [(c.split(' ')[1],int(c.split(' ')[0])) for c in consume.lstrip(' ').rstrip(' ').split(', ')]
    reactions[(produce_type, int(produce_qty))] = consume


def simplify(t, c, reactions):
    for i in reactions.keys():
        if t == i[0]:
            s = reactions[i]
            q = i[1]
    #  r = c // q  # for ans1
    r = c / q  # for ans2
    if r*q < c:
        r += 1
    l = (t,r*q-c)
    return s, r, l

fuel_reaction = reactions[('FUEL',1)]

leftovers = {}

def calculate(reaction):
    while True:
        remove = []
        update = []
        optimized = []
        for i in reaction:
            basic = False
            for k,v in reactions.items():
                if k[0] == i[0]:
                    for j in v:
                        if j[0] == 'ORE':
                            basic = True
            if not basic:
                nk, nv, lo = simplify(i[0], i[1], reactions)
                remove.append(i)
                for el in nk:
                    update.append((el[0],nv*el[1]))
                if lo[1] > 0:
                    leftovers[lo[0]] = leftovers.get(lo[0],0) + lo[1]

        if len(update) == 0:
            break

        for r in remove:
            reaction.remove(r)
        for u in update:
            reaction.append(u)

        for l in set([i[0] for i in reaction]):
            o = 0
            for i in reaction:
                if l == i[0]:
                    o += i[1]
            for j,v in leftovers.items():
                if l == j:
                    o -= v
                    leftovers[j] = 0
            optimized.append((l,o))

        reaction = optimized
    return reaction


fuel_reaction = calculate(fuel_reaction)
ans1 = 0
for i in fuel_reaction:
    nk, nv, lo = simplify(i[0], i[1], reactions)
    ans1 += nk[0][1]*nv

print(ans1)


M = calculate([(k,v) for k,v in leftovers.items()])
L = 0
for m in M:
    nk, nv, lo = simplify(m[0], m[1], reactions)
    L += nk[0][1]*nv

print(L)

ans2 = int(1000000000000/(ans1-L))
print(ans2)
