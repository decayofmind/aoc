import fileinput
from collections import defaultdict
from copy import deepcopy
from functools import lru_cache

data = [line.rstrip() for line in fileinput.input()]

P1 = []
P2 = []

d_p1 = False
d_p2 = False
for d in data:
    if d.startswith('Player 1'):
        d_p1 = True
        continue
    if d.startswith('Player 2'):
        d_p2 = True
        d_p1 = False
        continue
    if d_p1 and not d_p2 and d != '':
        P1.append(int(d))
    elif d_p2 and not d_p1 and d != '':
        P2.append(int(d))
    else:
        pass


def get_fingerprint(h):
    return ','.join([str(e) for e in h])

@lru_cache(maxsize=None)
def play(h1, h2, recursive=True):
    log = [defaultdict(int),defaultdict(int)]

    h1 = list(h1)
    h2 = list(h2)

    winner = None
    w_h = None

    while h1 and h2:
        log[0][get_fingerprint(h1)] += 1
        log[1][get_fingerprint(h2)] += 1

        if (log[0][get_fingerprint(h1)] > 1 and log[1][get_fingerprint(h2)] > 1) and recursive:
            return 1,h1

        t1 = h1.pop(0)
        t2 = h2.pop(0)

        if (len(h1) >= t1 and len(h2) >= t2) and recursive:
            winner,_ = play(deepcopy(tuple(h1[:t1])), deepcopy(tuple(h2[:t2])))
        else:
            if t1 > t2:
                winner = 1
            elif t2 > t1:
                winner = 2

        if winner == 1:
            h1 += t1,t2
            w_h = h1
        elif winner == 2:
            h2 += t2,t1
            w_h = h2

    return winner,tuple(w_h)

in_p1 = [tuple(deepcopy(P1)), tuple(deepcopy(P2))]
in_p2 = [tuple(deepcopy(P1)), tuple(deepcopy(P2))]

_,p1 = play(*in_p1, recursive=False)
print(sum((x+1)*y for x,y in enumerate(reversed(p1))))

_,p2 = play(*in_p2)
print(sum((x+1)*y for x,y in enumerate(reversed(p2))))
