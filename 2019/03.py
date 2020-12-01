#!/usr/bin/env python

from typing import Dict


class Cell(object):
    def __init__(self, x, y, content=[], steps_made=[]):
        self.x = x
        self.y = y
        self.content = content
        self.steps_made = steps_made


field: Dict[str, Cell] = {}


class Wire(object):
    def __init__(self, name, lines):
        self.lines = lines.split(',')
        self.name = name

    def draw(self):
        start = [0, 0]
        steps = -1
        for line in self.lines:
            direction = line[0]
            length = int(line[1:])
            if direction == 'U':
                for i in range(length):
                    steps += 1
                    cell_key = "{}:{}".format(start[0], start[1] + i)
                    c = field.get(cell_key, False)
                    if c:
                        c.content.append(self.name)
                        c.steps_made.append(steps)
                    else:
                        field[cell_key] = Cell(start[0],
                                               start[1] + i,
                                               content=[self.name],
                                               steps_made=[steps])
                start[1] += length
            if direction == 'D':
                for i in range(length):
                    steps += 1
                    cell_key = "{}:{}".format(start[0], start[1] - i)
                    c = field.get(cell_key, False)
                    if c:
                        c.content.append(self.name)
                        c.steps_made.append(steps)
                    else:
                        field[cell_key] = Cell(start[0],
                                               start[1] - i,
                                               content=[self.name],
                                               steps_made=[steps])
                start[1] -= length
            if direction == 'R':
                for i in range(length):
                    steps += 1
                    cell_key = "{}:{}".format(start[0] + i, start[1])
                    c = field.get(cell_key, False)
                    if c:
                        c.content.append(self.name)
                        c.steps_made.append(steps)
                    else:
                        field[cell_key] = Cell(start[0] + i,
                                               start[1],
                                               content=[self.name],
                                               steps_made=[steps])
                start[0] += length
            if direction == 'L':
                for i in range(length):
                    steps += 1
                    cell_key = "{}:{}".format(start[0] - i, start[1])
                    c = field.get(cell_key, False)
                    if c:
                        c.content.append(self.name)
                        c.steps_made.append(steps)
                    else:
                        field[cell_key] = Cell(start[0] - i,
                                               start[1],
                                               content=[self.name],
                                               steps_made=[steps])
                start[0] -= length


with open('input') as f:
    count = 0
    for line in f.readlines():
        Wire(count, line.strip()).draw()
        count += 1

distances = []
steps_total = []
for key, cell in field.items():
    if len(cell.content) == 2 and len(set(
            cell.content)) > 1 and cell.x != 0 and cell.y != 0:
        distances.append(abs(cell.x) + abs(cell.y))
        steps_total.append(sum(cell.steps_made))

print(min(distances))
print(min(steps_total))
