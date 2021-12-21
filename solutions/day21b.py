import functools


def inc_pos(pos, inc):
    pos = (pos + inc) % 10
    if pos == 0:
        pos = 10
    return pos


@functools.lru_cache(maxsize=None)
def winning_universes(scores, positions, active, scoring):
    for i in range(2):
        if scores[i] <= 0:
            if i == scoring:
                return 1
            else:
                return 0
    univs = 0
    for val, count in zip(dice_val, dice_val_counts):
        pos = inc_pos(positions[active], val)
        score = scores[active] - pos
        nscores = list(scores)
        npositions = list(positions)
        npositions[active] = pos
        nscores[active] = score
        univs += count * winning_universes(tuple(nscores), tuple(npositions), 1-active, scoring)
    return univs


dice_val = [3, 4, 5, 6, 7, 8, 9]
dice_val_counts = [1, 3, 6, 7, 6, 3, 1]
positions = (6, 1)
scores = (21, 21)

print(winning_universes(scores, positions, 0, 0))
print(winning_universes(scores, positions, 0, 1))
