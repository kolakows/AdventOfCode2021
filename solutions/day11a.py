import numpy as np

with open('input.txt') as f:
    data = f.read()
grid = [[int(x) for x in line] for line in data.split('\n')]
grid = np.array(grid)
steps = 100
c = 0
for i in range(steps):
    grid += 1
    stack = np.argwhere(grid > 9).tolist()
    while stack:
        x, y = stack.pop()
        c += 1
        grid[x, y] = 0
        nbs = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
        for xb, yb in nbs:
            if 0 <= xb < len(grid) and 0 <= yb < len(grid[0]):
                if grid[xb, yb] > 0:
                    grid[xb, yb] += 1
                if grid[xb, yb] > 9 and [xb, yb] not in stack:
                    stack.append([xb, yb])
print(c)