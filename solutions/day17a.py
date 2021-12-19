

ax = (150, 193)
ay = (-136, -86)

score = -100
for i in range(0, 100):
    for j in range(0, 1000):
        x, y = 0, 0
        steps = 0
        vx = i
        vy = j
        max_y = 0
        while not (ay[0] <= y <= ay[1]):
            if steps >= 1500 or (vx == 0 and not (ax[0] <= x <= ax[1])):
                break
            x += vx
            y += vy
            if y > max_y:
                max_y = y
            if vx > 0:
                vx -= 1
            vy -= 1
            steps += 1
        if ax[0] <= x <= ax[1] and ay[0] <= y <= ay[1]:
            if max_y > score:
                score = max_y
                best = (i, j)
print(score, best)
