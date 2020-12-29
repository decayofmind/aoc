import fileinput
from collections import OrderedDict

data = [line.rstrip() for line in fileinput.input()]

y_idx = data.index('your ticket:')
n_idx = data.index('nearby tickets:')

conditions = {}
y_ticket = ''
n_tickets = []

for c in data[:y_idx-1]:
    c = c.split(': ')
    n = c[0]
    c = c[1].split(' or ')
    cond = []
    for el in c:
        cond.append(
            (int(el.split('-')[0]), int(el.split('-')[1]))
        )
    conditions[n] = cond

y_ticket = data[y_idx+1].split(',')

for t in data[n_idx+1:]:
    n_tickets.append(t.split(','))


print(conditions)
print(y_ticket)
print(n_tickets)


errors = []
v_tickets = []


for ticket in n_tickets:
    valid_t = True
    for field in ticket:
        valid_f = False
        for conds in conditions.values():
            for c in conds:
                if c[0] <= int(field) <= c[1]:
                    valid_f = True
        if not valid_f:
            errors.append(int(field))
            valid_t = False
    if valid_t:
        v_tickets.append(ticket)

p1 = 0

for e in errors:
    p1 += e

print(p1)

fields = {}
v_tickets.append(y_ticket)

for name,conds in conditions.items():
    for pos in range(len(y_ticket)):
        s = []
        for ticket in v_tickets:
            valid = False
            for c in conds:
                if c[0] <= int(ticket[pos]) <= c[1]:
                    valid = True
            s.append(valid)
        if len(set(s)) == 1:
            if fields.get(name, False):
                fields[name].append(pos)
            else:
                fields[name] = [pos]

print(fields)

fl = len(fields.keys())

f = {}

while len(f) < fl:
    keys = list(fields.keys())

    for k in keys:
        if len(fields[k]) == 1:
            f[k] = fields.pop(k)[0]
            red = f[k]

    for k in fields.keys():
        fields[k].remove(red)


p2 = 1

for k,v in f.items():
    if k.startswith('departure'):
        p2 *= int(y_ticket[v])

print(p2)
