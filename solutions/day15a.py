with open('input.txt') as f:
    data = f.read()

import heapq

rows = data.splitlines()
grid = {(i, j) : int(v) for i, row in enumerate(rows) for j, v in enumerate(row)}
paths = [(0, (0, 0))]
heapq.heapify(paths)
visited = {(0, 0)}
while heapq:
    risk, (i, j) = heapq.heappop(paths)
    if (i, j) == (len(rows) - 1, len(rows[0]) - 1):
        print(risk)
        break
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni <= len(rows) - 1 and 0 <= nj <= len(rows[0]) - 1 and (ni, nj) not in visited:
            visited.add((ni, nj))
            heapq.heappush(paths, (risk + grid[(ni, nj)], (ni, nj)))

