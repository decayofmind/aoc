#!/usr/env/bin python

import random
from copy import deepcopy
from time import sleep
from typing import List


class IntCode(object):
    def __init__(self, program):
        self.program = program
        self.running = True
        self.ptr = 0
        self.rel_base = 0
        self.inputs = []

    def get_arg(self, pos, modes):
        mode = (0 if pos >= len(modes) else modes[pos])
        arg = self.program[self.ptr + (pos + 1)]
        if mode == 0:
            while len(self.program) <= arg:
                self.program.append(0)
            arg = self.program[arg]
        elif mode == 2:
            while len(self.program) <= arg:
                self.program.append(0)
            arg = self.program[arg + self.rel_base]
        return arg

    def get_idx(self, pos, modes):
        mode = (0 if pos >= len(modes) else modes[pos])
        arg = self.program[self.ptr + (pos + 1)]
        if mode == 0:
            pass
        elif mode == 2:
            arg += self.rel_base
        else:
            assert False, mode

        while len(self.program) <= arg:
            self.program.append(0)
        return arg

    def run(self, tty=False, inputs=[]):
        self.inputs += inputs
        while self.running:
            instr = str(self.program[self.ptr])
            op_code = int(instr[-2:])
            modes = list(reversed([int(x) for x in instr[:-2]]))

            if op_code == 1:
                self.program[self.get_idx(
                    2,
                    modes)] = self.get_arg(0, modes) + self.get_arg(1, modes)
                self.ptr += 4
            elif op_code == 2:
                self.program[self.get_idx(
                    2,
                    modes)] = self.get_arg(0, modes) * self.get_arg(1, modes)
                self.ptr += 4
            elif op_code == 3:
                a1 = self.get_idx(0, modes)
                if tty:
                    self.program[a1] = int(input('Enter value:').strip())
                else:
                    if len(self.inputs) == 0:
                        return None
                    self.program[a1] = int(self.inputs.pop(0))
                self.ptr += 2
            elif op_code == 4:
                a1 = self.get_arg(0, modes)
                self.ptr += 2
                if tty:
                    print("{}".format(a1))
                else:
                    #  yield a1
                    return a1
            elif op_code == 5:
                self.ptr = self.get_arg(
                    1, modes) if self.get_arg(0, modes) != 0 else self.ptr + 3
            elif op_code == 6:
                self.ptr = self.get_arg(1, modes) if self.get_arg(
                    0, modes) == 0 else self.ptr + 3
            elif op_code == 7:
                self.program[self.get_idx(2, modes)] = (1 if self.get_arg(
                    0, modes) < self.get_arg(1, modes) else 0)
                self.ptr += 4
            elif op_code == 8:
                self.program[self.get_idx(2, modes)] = (1 if self.get_arg(
                    0, modes) == self.get_arg(1, modes) else 0)
                self.ptr += 4
            elif op_code == 9:
                self.rel_base += self.get_arg(0, modes)
                self.ptr += 2
            else:
                assert op_code == 99
                self.running = False
                return None


program = [int(x) for x in open('input').read().strip().split(',')]

field = {}
start_pos = (20, 20)

movements = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

mk = list(movements.keys())

opposites = {1: 2, 2: 1, 3: 4, 4: 3}


def draw(f):
    X_len = Y_len = 45

    for y in range(0, Y_len):
        print('')
        print('\033[92m' + str(y)[-1] + '\033[0m', end=' ')
        for x in range(0, X_len):
            s = f.get((x, y), 0)
            if s == 0:  # wall
                char = '#'
            elif s == 1:  # corridor
                char = ' '
            elif s == 9:  # start
                char = 'S'
            elif s == 8:  # path to oxygen
                char = '·'
            elif s == 5:  # blind corridor
                char = ' '
            else:  # oxygen
                char = '\033[94m' + 'O' + '\033[0m'
            print(char, end=' ')
    print()
    print(' ', end=' ')
    [print('\033[92m' + str(x)[-1], end=' ') for x in range(0, X_len)]
    print('\033[0m', end='')
    print()


def get_surround(p, f, t):
    s = []
    for v in movements.values():
        c = (p[0] + v[0], p[1] + v[1])
        if f.get(c) == t:
            s.append(c)
    return s


# BRUTEFORCE METHOD (just oxygen)

#  res = 0

#  while True:
#      for m in mk:
#          res = p.run(inputs=[m], tty=False)
#          if res == 1:
#              current_pos = (current_pos[0]+movements[m][0], current_pos[1]+movements[m][1])
#              if not field.get(current_pos):
#                  field[current_pos] = 1
#              break
#          elif res == 2:
#              current_pos = (current_pos[0]+movements[m][0], current_pos[1]+movements[m][1])
#              field[current_pos] = 2
#              print('BINGO!!!')
#              break
#          else:  # wall
#              field[(current_pos[0]+movements[m][0], current_pos[1]+movements[m][1])] = 0
#      if res == 2:
#          break
#      random.shuffle(mk)


# recursive walkthrough METHOD (full board)
def walk(start, program):
    P = IntCode(program)
    field[start] = 1
    pos = start
    new_pos = None

    while True:
        for m in mk:
            new_pos = (pos[0] + movements[m][0], pos[1] + movements[m][1])
            if not field.get(new_pos):
                res = P.run(inputs=[m])

                if res == 1:
                    field[new_pos] = 1

                    # check previous pos for forks
                    b = opposites[m]
                    _ = P.run(inputs=[b])
                    assert _ == 1

                    for m_b in mk:
                        pos_b = (pos[0] + movements[m_b][0],
                                 pos[1] + movements[m_b][1])
                        if not field.get(pos_b):
                            res_b = P.run(inputs=[m_b])
                            if res_b == 1:
                                p = deepcopy(P.program)
                                _ = P.run(inputs=[opposites[m_b]])
                                assert _ == 1
                                walk(pos_b, p)
                            else:
                                field[pos_b] = 0

                    # go back forward
                    P.run(inputs=[m])
                    pos = new_pos

                elif res == 2:
                    field[new_pos] = 2
                    return

                elif res == 0:
                    field[new_pos] = 0

        if len(get_surround(pos, field, 0)) == 3:
            break


walk(start_pos, program)
field[start_pos] = 9
draw(field)

# PART 1

field1 = deepcopy(field)

field1[start_pos] = 9
path_buf: List[list] = [[]]
fork_buf = []

pos = start_pos

while True:

    field1[pos] = 8

    if len(get_surround(pos, field1, 2)) > 0:
        break

    s = get_surround(pos, field1, 1)

    path_buf[-1].append(pos)

    if len(s) > 1:
        fork_buf.append(pos)
        path_buf.append([])

    elif len(s) == 0:
        lp = path_buf.pop()
        for p in lp:
            field1[p] = 5

        pos = fork_buf.pop()
        continue

    pos = random.choice(s)

field1[start_pos] = 9

draw(field1)

ans1 = 0
for k, v in field1.items():
    if v == 8 or v == 9:
        ans1 += 1
print(ans1)

quit()
# PART 2

oxygen_pos = None
for k, v in field.items():
    if v == 2:
        oxygen_pos = k

minutes = 0

while True:
    filled = False
    updated = {}

    for k in field.keys():
        if field[k] == 2:
            for s in get_surround(k, field, 1):
                updated[s] = 2

    field.update(updated)

    if updated:
        minutes += 1
    else:
        break

    draw(field)
    sleep(0.4)

print(minutes)
