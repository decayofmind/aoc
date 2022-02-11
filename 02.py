#! /usr/bin/env python


def op(input, op_code, in1, in2, out):
    if op_code == 1:
        input[out] = input[in1] + input[in2]
    elif op_code == 2:
        input[out] = input[in1] * input[in2]
    elif op_code == 99:
        return
    else:
        print("Wrong OP code")


def init_input():
    with open('input') as fp:
        for l in fp:
            return list(map(int, l.strip().split(',')))


def run(input):
    i = 0
    while i < len(input) - 4:
        line = input[i:i + 4]
        op(input, *line)
        i += 4
    return input


for noun in range(99):
    for verb in range(99):
        input = init_input()
        input[1] = noun
        input[2] = verb
        run(input)
        output = input[0]
        if output == 19690720:
            print(100 * noun + verb)
