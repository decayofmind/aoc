#!/usr/env/bin python


class IntCode(object):
    def __init__(self, program):
        #  program.extend([0] * 65536)
        self.program = program
        self.running = True
        self.ptr = 0
        self.rel_base = 0
        self.input = []
        self.output = []

    def get_arg(self, pos, modes):
        mode = (0 if pos >= len(modes) else modes[pos])
        arg = self.program[self.ptr + (pos + 1)]
        if mode == 0:
            arg = self.program[arg]
        elif mode == 2:
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

    def run(self, inp=[]):
        interactive = False if len(inp) > 0 else True
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
                if interactive:
                    self.program[a1] = int(input('Enter value:').strip())
                else:
                    self.program[a1] = int(inp.pop(0))
                self.ptr += 2
            elif op_code == 4:
                a1 = self.get_arg(0, modes)
                self.ptr += 2
                if interactive:
                    print("{}".format(a1))
                else:
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


#  t1 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
#  program = [int(x) for x in t1.split(',')]
program = [int(x) for x in open('input').read().strip().split(',')]

p = IntCode(program)
p.run()
