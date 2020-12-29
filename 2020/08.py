import fileinput

from copy import copy, deepcopy


code = []

for line in fileinput.input():
    l = line.rstrip()
    code.append([l, 0])


variants = []
for i in range(len(code)):
    if 'nop' in code[i][0]:
        variant = code[i][0].replace('nop', 'jmp')
        variants.append([i, variant])
    elif 'jmp' in code[i][0]:
        variant = code[i][0].replace('jmp', 'nop')
        variants.append([i, variant])

def run(prg):
    acc = 0
    idx = 0
    exited = False
    while True:
        if idx == len(prg):
            exited = True
            break

        cmd = prg[idx][0].split()

        prg[idx][1] += 1

        if prg[idx][1] == 2:
            break


        if cmd[0] == 'nop':
            idx += 1
        elif cmd[0] == 'acc':
            idx += 1
            acc += int(''.join(cmd[1]))
        elif cmd[0] == 'jmp':
            idx += int(''.join(cmd[1]))

    return (acc, exited)


for v in variants:
    p = deepcopy(code)
    p[v[0]] = [v[1],0]
    acc, e = run(p)
    if e:
        print(acc)
        break
