import fileinput
from functools import lru_cache

data = [line.rstrip() for line in fileinput.input()]

depart = int(data[0])

data[1] = data[1].split(',')

buses = []
for i in range(len(data[1])):
    try:
        buses.append((int(data[1][i]), i))
    except:
        pass

DEP = {}

for b,_ in buses:
    n = depart//b
    d = (n+1)*b
    DEP[b] = d

BUS = min(DEP, key=DEP.get)

p1 = (DEP[BUS]-depart)*BUS

print(p1)

p2 = 1;
mode = 1;

for (bus_id, offset) in buses:
    print(mode,bus_id,offset,p2)
    while (p2 + offset) % bus_id != 0:
        p2 += mode
    mode *= bus_id

print(p2)

