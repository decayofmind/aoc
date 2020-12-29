import fileinput

bps = []

def dec_row(row):
    r = range(128)
    for c in row:
        if c == 'F':
            r = r[:len(r)/2]
        if c == 'B':
            r = r[len(r)/2:]
    return r.pop()

def dec_col(col):
    r = range(8)
    for c in col:
        if c == 'L':
            r = r[:len(r)/2]
        if c == 'R':
            r = r[len(r)/2:]
    return r.pop()

for line in fileinput.input():
    p = {}
    r_dec = dec_row(line.rstrip()[:7])
    p['row'] = r_dec
    c_dec = dec_col(line.rstrip()[-3:])
    p['col'] = c_dec
    p['id'] = r_dec*8+c_dec
    bps.append(p['id'])

print(max(bps))

ans2 = set(range(min(bps),max(bps)+1)).difference(set(bps))
print(ans2)
