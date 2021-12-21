from dataclasses import dataclass


@dataclass
class Player:
    pos: int
    score: int = 0


p1, p2 = Player(6), Player(1)
active, other = p1, p2
d = 1
while other.score < 1000:
    mv = 3 * d + 3
    d += 3
    mv = mv % 10
    active.pos = (active.pos + mv) % 10
    if active.pos == 0:
        active.pos = 10
    active.score += active.pos
    active, other = other, active

print((d-1) * active.score)
