#!/usr/env/bin python


class IntCode(object):
    def __init__(self, program):
        self.program = program
        self.running = True
        self.ptr = 0
        self.rel_base = 0
        self.inputs = []

    def get_arg(self, pos, modes):
        mode = (0 if pos>=len(modes) else modes[pos])
        arg = self.program[self.ptr+(pos+1)]
        if mode == 0:
            while len(self.program) <= arg:
                self.program.append(0)
            arg = self.program[arg]
        elif mode == 2:
            while len(self.program) <= arg:
                self.program.append(0)
            arg = self.program[arg+self.rel_base]
        return arg

    def get_idx(self, pos, modes):
        mode = (0 if pos>=len(modes) else modes[pos])
        arg = self.program[self.ptr+(pos+1)]
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
                self.program[self.get_idx(2,modes)] = self.get_arg(0,modes) + self.get_arg(1,modes)
                self.ptr += 4
            elif op_code == 2:
                self.program[self.get_idx(2,modes)] = self.get_arg(0,modes) * self.get_arg(1,modes)
                self.ptr += 4
            elif op_code == 3:
                a1 = self.get_idx(0, modes)
                if tty:
                    self.program[a1] = int(input('Enter value:').strip())
                else:
                    self.program[a1] = int(self.inputs.pop(0))
                self.ptr += 2
            elif op_code == 4:
                a1 = self.get_arg(0, modes)
                self.ptr += 2
                if tty:
                    print("{}".format(a1))
                else:
                    return a1
            elif op_code == 5:
                self.ptr = self.get_arg(1, modes) if self.get_arg(0, modes) != 0 else self.ptr + 3
            elif op_code == 6:
                self.ptr = self.get_arg(1, modes) if self.get_arg(0, modes) == 0 else self.ptr + 3
            elif op_code == 7:
                self.program[self.get_idx(2, modes)] = (1 if self.get_arg(0, modes) < self.get_arg(1, modes) else 0)
                self.ptr += 4
            elif op_code == 8:
                self.program[self.get_idx(2, modes)] = (1 if self.get_arg(0, modes) == self.get_arg(1, modes) else 0)
                self.ptr += 4
            elif op_code == 9:
                self.rel_base += self.get_arg(0, modes)
                self.ptr += 2
            else:
                assert op_code == 99
                self.running = False
                return None

program = [int(x) for x in open('input').read().strip().split(',')]

p = IntCode(program)

#  cur_pos = (0,0)
cur_pos = (34,58)
cur_dir = 90
panels = {}

start = True

while p.running:
    if start:
        color = p.run(inputs=[1], tty=False)
        start = False
    else:
        color = p.run(inputs=[panels.get(cur_pos, 0)], tty=False)

    direction = p.run(tty=False)

    if color is not None:
        panels[cur_pos] = color

    if direction == 0:
        cur_dir -= 90
    elif direction == 1:
        cur_dir += 90
    elif direction is None:
        break
    else:
        print("Wrong direction")

    cur_dir = cur_dir % 360.0

    if cur_dir == 180:
        cur_pos = (cur_pos[0]+1, cur_pos[1])
    elif cur_dir == 0:
        cur_pos = (cur_pos[0]-1, cur_pos[1])
    elif cur_dir == 90:
        cur_pos = (cur_pos[0], cur_pos[1]-1)
    elif cur_dir == 270:
        cur_pos = (cur_pos[0], cur_pos[1]+1)
    else:
        print("Wrong move")

print(len(panels))

x_cords = sorted([p[0] for p in panels.keys()])
y_cords = sorted([p[1] for p in panels.keys()])

for y in range(y_cords[0], y_cords[-1]+1):
    print()
    for x in range(x_cords[0], x_cords[-1]+1):
        if panels.get((x,y), 0) == 1:
            print('#', end='')
        else:
            print(' ', end='')
