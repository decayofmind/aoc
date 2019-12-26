#!/usr/env/bin python


#  class IntCode(object):
#      def __init__(self, program):
#          self.exited = False
#          self._ip = 0
#          self.input = []
#          self.output = []

#      def run()



#  t1 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
#  program = [int(x) for x in t1.split(',')]
program = [int(x) for x in open('input').read().strip().split(',')]
program += 10000*[0]

def get_args(program, ip, n, modes, rel_base, out=True):
    while len(modes) < n:
        modes = [0] + modes
    args = program[ip+1:ip+n+1]
    if out:
        if modes[0] == 0:
            modes[0] = 1
        elif modes[0] == 2:
            modes[0] = 4
    res = []
    for i,x in enumerate(args):
        if modes[len(modes)-i-1]==1:
            res.append(x)
        elif modes[len(modes)-i-1]==2:
            res.append(program[x+rel_base])
        elif modes[len(modes)-i-1]==4:
            res.append(x+rel_base)
        else:
            res.append(program[x])
    return res[0] if len(res) < 2 else res

ip = 0
rel_base = 0
while True:
    instr = [int(x) for x in str(program[ip])]
    op_code = (0 if len(instr)==1 else instr[-2])*10+instr[-1]
    modes = instr[:-2]
    if op_code == 1:
        a1,a2,a3 = get_args(program, ip, 3, modes, rel_base)
        program[a3] = a1+a2
        ip += 4
    elif op_code == 2:
        a1,a2,a3 = get_args(program, ip, 3, modes, rel_base)
        program[a3] = a1*a2
        ip += 4
    elif op_code == 3:
        a1 = get_args(program, ip, 1, modes, rel_base)
        program[a1] = int(input('Enter value:').strip())
        ip += 2
    elif op_code == 4:
        a1 = get_args(program, ip, 1, modes, rel_base, out=False)
        print("{}".format(a1))
        ip += 2
    elif op_code == 5:
        a1,a2 = get_args(program, ip, 2, modes, rel_base, out=False)
        if a1 != 0:
            ip = a2
        else:
            ip += 3
    elif op_code == 6:
        a1,a2 = get_args(program, ip, 2, modes, rel_base, out=False)
        if a1 == 0:
            ip = a2
        else:
            ip += 3
    elif op_code == 7:
        a1,a2,a3 = get_args(program, ip, 3, modes, rel_base)
        if a1 < a2:
            program[a3] = 1
        else:
            program[a3] = 0
        ip += 4
    elif op_code == 8:
        a1,a2,a3 = get_args(program, ip, 3, modes, rel_base, out=True)
        if a1 == a2:
            program[a3] = 1
        else:
            program[a3] = 0
        ip += 4
    elif op_code == 9:
        a1 = get_args(program, ip, 1, modes, rel_base, out=False)
        rel_base += a1
        ip += 2
    else:
        assert op_code == 99
        break
