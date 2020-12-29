import fileinput

p1 = 0
p2 = 0

groups = []

g = []
for line in fileinput.input():
    if line == '\n':
        groups.append(g)
        g = []
    else:
        g.append(line.rstrip())
groups.append(g)


answers_s = []
for group in groups:
    c = ''
    for p in group:
        c += p

    answers_s.append(len(set(c)))

for a in answers_s:
    p1 += a

print(p1)

answers_g = []
for group in groups:
    if len(group) == 1:
        answers_g.append(len(group[0]))
    else:
        answers_g.append(len(set.intersection(*map(set, group))))

for a in answers_g:
    p2 += a

print(p2)
