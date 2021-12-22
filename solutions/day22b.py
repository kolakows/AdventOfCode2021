from tqdm import tqdm

with open('input.txt') as f:
    data = f.read()
a, b = data.split('\n')[0].split()
steps = [[x for x in line.split()] for line in data.split('\n')]


def overlapping(cube1, cube2):
    for i in range(3):
        if not (cube1[i][0] <= cube2[i][1] and cube2[i][0] <= cube1[i][1]):
            return False
    return True


def cube_overlap(cube1, cube2):
    overlap = []
    for i in range(3):
        lend = max(cube1[i][0], cube2[i][0])
        rend = min(cube1[i][1], cube2[i][1])
        overlap.append((lend, rend))
    return tuple(overlap)


def cubes_excluding(cube, subc):
    cubes = []
    if cube[2][0] != subc[2][0]:
        cubes.append((cube[0], cube[1], (cube[2][0], subc[2][0] - 1)))
    if cube[2][1] != subc[2][1]:
        cubes.append((cube[0], cube[1], (subc[2][1] + 1, cube[2][1])))
    z = subc[2]
    if cube[0][0] != subc[0][0]:
        cubes.append(((cube[0][0], subc[0][0] - 1), cube[1], z))
    if cube[0][1] != subc[0][1]:
        cubes.append(((subc[0][1] + 1, cube[0][1]), cube[1], z))
    if cube[1][0] != subc[1][0]:
        cubes.append((subc[0], (cube[1][0], subc[1][0] - 1), z))
    if cube[1][1] != subc[1][1]:
        cubes.append((subc[0], (subc[1][1] + 1, cube[1][1]), z))
    return cubes


def volume(cube):
    sides = tuple((c[1] - c[0] + 1 for c in cube))
    return sides[0] * sides[1] * sides[2]


lit_cubes = []
for status, coords in tqdm(steps):
    bit = 1 if status == 'on' else 0
    coords = [tuple(map(int, c.split('=')[1].split('..'))) for c in coords.split(',')]
    x, y, z = ((min(*c), max(*c)) for c in coords)
    cube = (x, y, z)
    nlitcubes = []
    candidate_cubes = {cube}
    for lit_c in lit_cubes:
        for cc in candidate_cubes.copy():
            if overlapping(cc, lit_c):
                overlap = cube_overlap(cc, lit_c)
                if bit:
                    lit_cc = cubes_excluding(cc, subc=overlap)
                    candidate_cubes.remove(cc)
                    candidate_cubes.update(lit_cc)
                else:
                    left_lit = cubes_excluding(lit_c, subc=overlap)
                    nlitcubes += left_lit
            else:
                nlitcubes.append(lit_c)
    if bit:
        lit_cubes = list(candidate_cubes) + lit_cubes
    else:
        lit_cubes = nlitcubes

print(sum((volume(c) for c in lit_cubes)))
