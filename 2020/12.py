import fileinput


data = [line.rstrip() for line in fileinput.input()]

directions = {0: 'E',
              270: 'N',
              180: 'W',
              90: 'S',
              -90:  'N',
              -180: 'W',
              -270: 'S'
              }

C = [0,0]
D = 0

for m in data:
    cmd = m[0]
    num = int(m[1:])

    if cmd == 'F':
        cmd = directions[D]

    if cmd == 'N':
        C[1] += num
    elif cmd == 'S':
        C[1] -= num
    elif cmd == 'E':
        C[0] += num
    elif cmd == 'W':
        C[0] -= num
    elif cmd == 'L':
        D = (D-num)%360
    elif cmd == 'R':
        D = (D+num)%360

print(abs(C[0])+abs(C[1]))

W = [10,1]
S = [0,0]
D = 0

for m in data:
    cmd = m[0]
    num = int(m[1:])

    if cmd == 'F':
        S[0] += W[0]*num
        S[1] += W[1]*num

    if cmd == 'N':
        W[1] += num
    elif cmd == 'S':
        W[1] -= num
    elif cmd == 'E':
        W[0] += num
    elif cmd == 'W':
        W[0] -= num
    elif cmd == 'L':
        o_x, o_y = W
        for _ in range(int(num/90)):
            o_x, o_y = -o_y, o_x
        W = [o_x, o_y]
    elif cmd == 'R':
        o_x, o_y = W
        for _ in range(int(num/90)):
            o_x, o_y = o_y, -o_x
        W = [o_x, o_y]

print(abs(S[0])+abs(S[1]))
