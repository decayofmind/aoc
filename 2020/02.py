#!/usr/bin/env python3

in_a = []
out = 0

def check_1(password, rule):
    s = {}
    for c in password:
        if s.get(c, False):
            s[c] += 1
        else:
            s[c] = 1

    cond = rule[0].split('-')
    t = rule[1]

    if s.get(t, False) and (int(cond[0]) <= s[t] <= int(cond[1])):
        return True
    return False


def check_2(password, rule):
    cond = rule[0].split('-')
    t = rule[1]

    if (password[int(cond[0])-1] == t) and (password[int(cond[1])-1] != t) or \
            (password[int(cond[1])-1] == t) and (password[int(cond[0])-1] != t):
        return True
    return False


with open('input', 'r') as input:
    for line in input:
        rule, password = line.rstrip().split(': ')
        in_a.append((rule.split(' '), password))

for el in in_a:
    if check_1(el[1], el[0]):
        out += 1

print(out)

out = 0

for el in in_a:
    if check_2(el[1], el[0]):
        out += 1

print(out)
