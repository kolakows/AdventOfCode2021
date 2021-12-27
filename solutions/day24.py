import functools
import numpy as np

with open('input.txt') as f:
    instructions = f.read().split('inp w\n')[1:]

z_reduce = []
steps = []
for block in instructions:
    block = block.split('\n')
    c4 = int(block[3].split()[2])
    z_reduce.append(c4)
    c5 = int(block[4].split()[2])
    c15 = int(block[14].split()[2])
    steps.append((c4, c5, c15))
max_z_reduce = [np.prod(z_reduce[i:]) for i in range(14)]


def calc_step(z, n, consts):
    c4, c5, c15 = consts
    if z % 26 + c5 != n:
        z = (26*z) // c4 + n + c15
    else:
        z = z // c4
    return z


n = 14 * [0]


@functools.lru_cache(maxsize=None)
def run_block(z, i):
    if i == 14:
        if z == 0:
            return True
        else:
            return False
    if z // max_z_reduce[i] > 0:
        return False
    # for j in range(9, 0, -1): # part 1
    for j in range(1, 10):
        n[i] = j
        zz = calc_step(z, n[i], steps[i])
        if run_block(zz, i+1):
            return True
    return False


print(run_block(0, 0))
print(n)
