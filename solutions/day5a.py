import numpy as np

with open('input.txt', 'r') as f:
    data = f.read()
data = data.splitlines()
max_int = max([int(z) for x in data for y in x.split(' -> ') for z in y.split(',')]) + 1


map = np.zeros((max_int, max_int), dtype=int)
for coords in data:
    start, end = coords.split(' -> ')
    sx, sy = [int(x) for x in start.split(',')]
    ex, ey = [int(x) for x in end.split(',')]
    if sy == ey:
        for i in range(abs(sx - ex) + 1):
            beg = min(sx, ex)
            map[beg + i, sy] += 1
    elif sx == ex:
        for i in range(abs(sy - ey) + 1):
            beg = min(sy, ey)
            map[sx, beg + i] += 1

print(map.T)
print(sum(map.flatten() > 1))
