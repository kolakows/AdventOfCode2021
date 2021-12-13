with open('input.txt') as f:
    data = f.read()
dots, folds = data.split('\n\n')
dots = [tuple(map(int, d.split(','))) for d in dots.split('\n')]
folds = [('x', int(v.split('=')[1])) if 'x' in v else ('y', int(v.split('=')[1])) for v in folds.split('\n')]
grid = {*dots}

for axis, cutoff in folds:
    for x, y in grid.copy():
        if axis == 'x':
            if x > cutoff:
                grid.remove((x, y))
                dist = x - cutoff
                grid.add((cutoff - dist, y))
        if axis == 'y':
            if y > cutoff:
                grid.remove((x, y))
                dist = y - cutoff
                grid.add((x, cutoff - dist))
print(len(grid))
p = []
w, _ = max(grid, key=lambda d: d[0])
_, h = max(grid, key=lambda d: d[1])
for j in range(h + 1):
    for i in range(w + 1):
        if (i, j) in grid:
            p.append('#')
        else:
            p.append('.')
    p.append('\n')
print(''.join(p))
