#!/usr/env/bin python

import curses
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
                    yield a1
                    #  return a1
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

# PART 1
#  p = IntCode(program)

#  output = []
#  while p.running:
#      o = p.run()
#      if o is not None:
#          output.append(o)

#  block_tiles_count = 0
#  for i in range(0, len(output), 3):
#      tile = output[i:i+3][-1]
#      if tile == 2:
#          block_tiles_count += 1

#  print(block_tiles_count)

objects = {0: ' ', 1: '#', 2: 'X', 3: 'W', 4: '*'}

p = IntCode(program)

tiles = {}
inputs = []
#  saved=[int(x) for x in open('save2').read().strip().split(',')]
saved: List[int] = []

inp = 0

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(False)
curses.halfdelay(3)
score = curses.newwin(3, 38, 0, 0)
score.border()
main = curses.newwin(30, 38, 3, 0)
main.keypad(True)
main.border()

while p.running:
    #  PLAY!
    if saved:
        inp = saved.pop(0)
    else:
        char = screen.getch()
        if char == ord('l'):
            inp = 1
        elif char == ord('h'):
            inp = -1
        elif char == -1:
            inp = 0
    inputs.append(int(inp))
    output = [o for o in p.run(inputs=[inp])]
    tiles.update({(output[i], output[i + 1]): output[i + 2]
                  for i in range(0, len(output), 3)})
    DIM = (max([t[0] for t in tiles.keys()]), max([t[1] for t in tiles]))
    if not saved:
        for k, v in tiles.items():
            if v == 4:
                ball = k
            if v == 3:
                platform = k
        # AI
        #  if ball[0] > platform[0]:
        #      inp = 1
        #  elif ball[0] < platform[0]:
        #      inp = -1
        #  else:0
        #      inp = 0
        score.addstr(
            1, 2, 'SCORE: {} | B:{}/P:{}'.format(tiles.get((-1, 0)), ball,
                                                 platform))
        score.refresh()
        for y in range(DIM[1] + 1):
            for x in range(DIM[0] + 1):
                if tiles.get((x, y)):
                    main.addch(y + 1, x + 1, objects[tiles[(x, y)]])
                else:
                    main.addch(y + 1, x + 1, objects[0])
    main.refresh()
    curses.napms(300)

curses.nocbreak()
main.keypad(False)
main.clear()
curses.echo()
curses.endwin()

print("Data to save:")
print(inputs)
