import fileinput
from itertools import product
from copy import deepcopy


data = [line.rstrip() for line in fileinput.input()]

mask = ''
mem = ['0']*100000

def apply_mask1(n,m):
    n = list(format(n,'b').zfill(36))
    for i,c in enumerate(list(m)):
        if c in ['0','1']:
            n[i] = c
    return ''.join(n)


def apply_mask2(a,m):
    addr = []
    fl = 0
    a = list(format(a,'b').zfill(36))
    for i,c in enumerate(list(m)):
        if c in ['1','X']:
            if c == 'X':
                fl += 1
            a[i] = c

    vars = product(['0','1'], repeat=fl)

    for v in vars:
        v = list(v)
        na = deepcopy(a)

        for i,c in enumerate(na):
            if c == 'X':
                na[i] = v.pop(0)
        addr.append(int(''.join(na), 2))
    return addr


for l in data:
    t,v = l.split(' = ')
    if t == 'mask':
        mask = v
    if 'mem' in t:
        pos = int(t.split('mem[')[1].strip(']'))
        v = apply_mask1(int(v), mask)
        mem[pos] = v


p1 = 0

for cell in mem:
    p1 += int(cell,2)

print(p1)


mask = ''
mem = {}

for l in data:
    t,v = l.split(' = ')
    if t == 'mask':
        mask = v
    if 'mem' in t:
        pos = int(t.split('mem[')[1].strip(']'))
        addrs = apply_mask2(int(pos), mask)
        for a in addrs:
            mem[a] = v

p2 = 0

for cell in mem.values():
    p2 += int(cell)

print(p2)
