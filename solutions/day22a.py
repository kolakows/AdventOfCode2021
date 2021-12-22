with open('input.txt') as f:
    data = f.read()
a, b = data.split('\n')[0].split()
steps = [[x for x in line.split()] for line in data.split('\n')]

grid = {}


def crop(coords):
    x, y = min(*coords), max(*coords)
    if y < -50:
        return -100, -100
    if y > 50:
        return 100, 100
    y += 1
    return x, y


for status, coords in steps:
    bit = 1 if status == 'on' else 0
    coords = [tuple(map(int, c.split('=')[1].split('..'))) for c in coords.split(',')]
    x, y, z = (crop(c) for c in coords)
    for i in range(x[0], x[1]):
        for j in range(y[0], y[1]):
            for k in range(z[0], z[1]):
                grid[(i, j, k)] = bit

print(sum(grid.values()))
