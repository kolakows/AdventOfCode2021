from collections import Counter

with open('input.txt') as f:
    data = f.read()
poly, rules = data.split('\n\n')
rules = {p : n for p, n in (line.split(' -> ') for line in rules.split('\n'))}
steps = 40
for i in range(steps):
    npoly = []
    for a, b in zip(poly, poly[1:]):
        p = a + b
        if p in rules:
            npoly += [a, rules[p]]
        else:
            npoly += [a]
    npoly += [poly[-1]]
    # print(''.join(npoly))
    poly = npoly
c = Counter(poly)
print(max(c.values()) - min(c.values()))
