#!/usr/bin/env python3

import re

keys = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]


def check_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    return False

def check_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    return False

def check_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    return False

def check_hgt(hgt):
    if 'cm' in hgt:
        if 150 <= int(hgt.rstrip('cm')) <= 193:
            return True
    if 'in' in hgt:
        if 59 <= int(hgt.rstrip('in')) <= 76:
            return True
    return False

def check_hcl(hcl):
    p = re.compile(r'#[0-9a-f]{6}$')
    if p.match(hcl) is not None:
        return True
    return False

def check_ecl(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def check_pid(pid):
    p = re.compile(r'[0-9]{9}$')
    if p.match(pid) is not None:
        if len(pid) > 9:
            print(pid)
        return True
    return False


p_parsed = []
passports = []

with open('2020/input', 'r') as input:
    for el in input.read().split('\n\n'):
        p_parsed.append(el.rstrip().replace('\n', ' ').split(' '))

for el in p_parsed:
    p = {}
    for f in el:
        p[f.split(':')[0]] = f.split(':')[1]
    passports.append(p)

count = 0

new_p = []

for p in passports:
    valid = True
    for k in keys:
        if not p.get(k, False):
            valid = False
    if valid:
        new_p.append(p)

print(len(new_p))

for p in new_p:
    valid = True
    for k in keys:
        if not locals()["check_" + k](p[k]):
            valid = False
    if valid:
        count += 1

print(count)
