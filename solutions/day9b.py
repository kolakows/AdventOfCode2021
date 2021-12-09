import numpy as np

with open('input.txt') as f:
    data = f.readlines()
g = np.array([list(map(int, list(l.strip()))) for l in data])

wall = 9
grid = np.zeros((len(g)+2, len(g[0])+2))
grid.fill(wall)
grid[1:-1, 1:-1] = g

sources = []
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if grid[i, j] < min(grid[i-1, j], grid[i+1, j], grid[i, j-1], grid[i, j+1]):
            sources.append((i, j))

visited = np.zeros(grid.shape)


def ffill(grid, i, j):
    if visited[i, j]:
        return 0
    visited[i, j] = 1
    v = 1
    nbs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for nb in nbs:
        if grid[i, j] < grid[nb] < wall:
            v += ffill(grid, nb[0], nb[1])
    return v


basins = []
for s in sources:
    basins.append(ffill(grid, s[0], s[1]))
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
