import fileinput
import re

p1 = 0
p2 = 0

rules = {}

for line in fileinput.input():
    s = line.rstrip().rstrip('.').split('bags contain ')

    cont = {}
    for c in s[1].split(', '):
        if c == 'no other bags':
            rules[s[0].rstrip(' ')] = None
            continue
        else:
            cont[' '.join(c.split(' ')[1:3])] = int(c.lstrip(' ').split(' ')[0])
    rules[s[0].rstrip(' ')] = cont


r = []

def search(item):
    global r
    for k,v in rules.items():
        for b in v.keys():
            if b == item:
                r.append(k)
                search(k)


search('shiny gold')

p1 = len(set(r))
print(p1)


def count(item):
    cont = rules[item]

    global p2

    s = 0

    for k,v in cont.items():
        s += v + v * count(k)
    return p2 + s

print(count('shiny gold'))
