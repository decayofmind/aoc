import ast
import fileinput
import re

data = [line.rstrip() for line in fileinput.input()]

to_match = []
rules = {}

is_rules = True
for d in data:
    if d == '':
        is_rules = False
        continue
    if is_rules:
        r = d.split(': ')
        rules[r[0]] = r[1].strip('"')
    else:
        to_match.append(d)


def to_regex(rule):
    global rules

    rule = rules[rule]

    if rule in 'ab':
        return rule

    return "(?:%s)" % "|".join(
        "".join(to_regex(r) for r in rl.split())
        for rl in rule.split(" | ")
    )


r = re.compile(to_regex('0'))
print(sum(r.fullmatch(m) is not None for m in to_match))
