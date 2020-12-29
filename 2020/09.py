import fileinput
from itertools import combinations

data = []
window = 25

pos = 0
p1 = 0

for line in fileinput.input():
    l = line.rstrip()
    data.append(int(l))


for n in range(window,len(data)):
    valid = False
    for p in combinations(data[n-window:n], 2):
        if p[0] + p[1] == data[n]:
            valid = True
    if not valid:
        p1 = data[n]
        pos = n
        break

print(p1)

pre_p2 = []

for w in range(2,pos):
    p = 0
    while p < pos+1:
        if sum(data[p:p+w]) == p1:
            pre_p2 = data[p:p+w]
        p += 1

p2 = min(pre_p2) + max(pre_p2)
print(p2)
