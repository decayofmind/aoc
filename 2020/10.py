import fileinput
from functools import lru_cache


data = []

p1 = 0
p2 = 0

for line in fileinput.input():
    l = line.rstrip()
    data.append(int(l))


cur = 0
counts = [0, 1]

for _ in range(len(data)):
    if (cur + 1) in data:
        counts[0] += 1
        cur += 1
    elif (cur + 3) in data:
        counts[1] += 1
        cur += 3

p1 = counts[0]*counts[1]
print(p1)

data.sort()

data_dct = dict(zip(data, [[0,0]]*len(data)))

@lru_cache(maxsize=None)
def count(s=0):
    ans = 0
    global p2
    for v in [1,2,3]:
        if data_dct.get(s+v, False):
            ans += count(s+v)
    if s == cur:
        ans += 1
    return ans

print(count())
