from dataclasses import dataclass

@dataclass
class Cup:
    id: int
    next: object


data = [int(x) for x in list('653427918')]



def play(moves, d):
    cups = {}

    n = None
    for el in d[::-1]:
        cups[el] = Cup(el,n)
        n = cups[el]

    current = cups[d[0]]
    cups[d[-1]].next = current


    for _ in range(moves):

        pick = [current.next, current.next.next, current.next.next.next]
        current.next = pick[-1].next

        dest = cups[current.id-1 if current.id > 1 else max(data)]

        while dest in pick:
            dest = cups[dest.id-1 if dest.id > 1 else max(data)]

        dest.next, pick[-1].next = pick[0], dest.next

        current = current.next

    return cups[1]


c1 = play(100,data)

p1 = ''
n = c1.next
while True:
    if n.id == 1:
        break
    p1 += str(n.id)
    n = n.next

print(p1)

data = data + list(range(10,1000001))
c2 = play(10000000,data)

print(c2.next.id*c2.next.next.id)
