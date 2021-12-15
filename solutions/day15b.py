with open('input.txt') as f:
    data = f.read()

import heapq

rows = data.splitlines()
grid = {(i, j) : int(v) for i, row in enumerate(rows) for j, v in enumerate(row)}
paths = [(0, (0, 0))]
heapq.heapify(paths)
visited = {(0, 0)}
h = len(rows)
w = len(rows[0])
max_h = 5 * h - 1
max_w = 5 * w - 1
while heapq:
    risk, (i, j) = heapq.heappop(paths)
    if (i, j) == (max_h, max_w):
        print(risk)
        break
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni <= max_h and 0 <= nj <= max_w and (ni, nj) not in visited:
            visited.add((ni, nj))
            val = (grid[(ni % h, nj % w)] + (ni // h + nj // w))
            val = val % 10 + val // 10
            heapq.heappush(paths, (risk + val, (ni, nj)))

