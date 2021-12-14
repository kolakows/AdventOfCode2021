from collections import Counter

with open('input.txt') as f:
    data = f.read()
poly, rules = data.split('\n\n')
rules = {p : n for p, n in (line.split(' -> ') for line in rules.split('\n'))}
first, last = poly[0], poly[-1]
poly = Counter([a+b for a, b in zip(poly, poly[1:])])
steps = 40
# print(poly)
for i in range(steps):
    npoly = {}
    for a, b in poly.keys():
        p = a + b
        if p in rules:
            p1 = a + rules[p]
            p2 = rules[p] + b
            pcount = poly.get(p, 0)
            npoly[p1] = npoly.get(p1, 0) + pcount
            npoly[p2] = npoly.get(p2, 0) + pcount
        else:
            npoly[p] = poly[p]
    # print(npoly)
    poly = npoly
c = {}
# double count every letter
for k, v in poly.items():
    a, b = k
    c[a] = c.get(a, 0) + v
    c[b] = c.get(b, 0) + v
c[first] += 1
c[last] += 1
print((max(c.values()) - min(c.values()))/2)
