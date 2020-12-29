from math import ceil, sqrt

def solve(g, h, p):
    N = ceil(sqrt(p - 1))

    tbl = {pow(g, i, p): i for i in range(N)}

    c = pow(g, N * (p - 2), p)

    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]
    return None

A = 2959251
B = 4542595
p = 20201227
base = 7

a = solve(base, A, p)

print(pow(B,a,p))
