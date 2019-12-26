#!/usr/env/bin python

from itertools import permutations
from copy import deepcopy
import threading
import queue
import logging

#  t1 = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
#  program = [int(x) for x in t1.split(',')]
program = [int(x) for x in open('input').read().strip().split(',')]

def get_args(p, ip, n, modes, out=True):
    while len(modes) < n:
        modes = [0] + modes
    args = p[ip+1:ip+n+1]
    if out:
        assert modes[0] == 0
        modes[0] = 1
    args = [x if modes[len(modes)-i-1]==1 else p[x] for i,x in enumerate(args)]
    return args

def run(p, phase, queue_in, queue_out):
    input_count = 0

    ip = 0
    while True:
        instr = [int(x) for x in str(p[ip])]
        op_code = (0 if len(instr)==1 else instr[-2])*10+instr[-1]
        modes = instr[:-2]

        if op_code == 1:
            a1,a2,a3 = get_args(p, ip, 3, modes)
            p[a3] = a1+a2
            ip += 4
        elif op_code == 2:
            a1,a2,a3 = get_args(p, ip, 3, modes)
            p[a3] = a1*a2
            ip += 4
        elif op_code == 3:
            a1 = p[ip+1]
            if input_count == 0:
                p[a1] = phase
                input_count = 1
            elif input_count == 1:
                p[a1] = queues[queue_in].get()
            #  p[a1] = int(input('Enter value:').strip())
            ip += 2
        elif op_code == 4:
            a1 = p[ip+1]
            queues[queue_out].put(p[a1])
            queues[queue_in].task_done()
            ip += 2
        elif op_code == 5:
            a1,a2 = get_args(p, ip, 2, modes, out=False)
            if a1 != 0:
                ip = a2
            else:
                ip += 3
        elif op_code == 6:
            a1,a2 = get_args(p, ip, 2, modes, out=False)
            if a1 == 0:
                ip = a2
            else:
                ip += 3
        elif op_code == 7:
            a1,a2,a3 = get_args(p, ip, 3, modes)
            if a1 < a2:
                p[a3] = 1
            else:
                p[a3] = 0
            ip += 4
        elif op_code == 8:
            a1,a2,a3 = get_args(p, ip, 3, modes)
            if a1 == a2:
                p[a3] = 1
            else:
                p[a3] = 0
            ip += 4
        else:
            assert op_code == 99
            break

phases = list(range(5,9+1))
combs = list(permutations(phases,5))
#  combs = [(9,8,7,6,5)]

res = []

for var in combs:
    queues = [queue.Queue() for x in range(5)]
    queues[0].put(0)
    threads = []
    for n,phase in enumerate(var):
        p = deepcopy(program)
        q_in = n
        if n < 4:
            q_out = n+1
        else:
            q_out = 0
        x = threading.Thread(name='{0}-{1}'.format(phase,n), target=run, args=(p,phase,q_in,q_out))
        threads.append(x)
        x.start()

    [x.join() for x in threads]
    res.append(queues[0].get())

print(max(res))
