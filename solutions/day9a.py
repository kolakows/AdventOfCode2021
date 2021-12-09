import numpy as np

with open('input.txt') as f:
    data = f.readlines()
g = np.array([list(map(int, list(l.strip()))) for l in data])

wall = 10
grid = np.zeros((len(g)+2, len(g[0])+2))
grid.fill(wall)
grid[1:-1, 1:-1] = g

s = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if grid[i, j] < min(grid[i-1, j], grid[i+1, j], grid[i, j-1], grid[i, j+1]):
            # print(i, j, grid[i, j])
            s += grid[i, j] + 1
print(s)
