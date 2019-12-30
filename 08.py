#!/usr/env/bin python

input_data = [int(x) for x in open('input').read().strip()]

X = 25
Y = 6

layers = []
layer = []
i = 0
while i < len(input_data) + 1:
    x = input_data[i:i + X]
    layer.append(x)
    if len(layer) == 6:
        layers.append(layer)
        layer = []
    i += X

# part 1

counts = []
for l in layers:
    c = {}
    for r in l:
        for x in r:
            c[x] = c.get(x, 0) + 1
    counts.append(c)

zeros_c = list(map(lambda x: x.get(0), counts))

for n, x in enumerate(zeros_c):
    if x == min(zeros_c):
        ans = counts[n].get(1) * counts[n].get(2)

print(ans)

# part 2

img_merged = []
for y in range(Y):
    img_merged.append(list(zip(*list(map(lambda x: x[y], layers)))))

image = []
for r in img_merged:
    row = []
    for p in r:
        for x in p:
            if x == 0:
                row.append(' ')
                break
            elif x == 1:
                row.append('#')
                break
            else:
                continue
    image.append(row)

for r in image:
    print()
    for x in r:
        print(x, end='')
