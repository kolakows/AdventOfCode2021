

ax = (150, 193)
ay = (-136, -86)

c = 0
for i in range(0, 200):
    for j in range(-140, 1000):
        x, y = 0, 0
        steps = 0
        vx = i
        vy = j
        max_y = 0
        while True:
            if steps >= 3000 \
                    or (vx == 0 and not (ax[0] <= x <= ax[1])) \
                    or (ax[0] <= x <= ax[1] and ay[0] <= y <= ay[1]):
                break
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            steps += 1
        if ax[0] <= x <= ax[1] and ay[0] <= y <= ay[1]:
            c += 1
print(c)
