import itertools
import numpy as np
from itertools import permutations
from tqdm import tqdm


with open('input.txt') as f:
    data = f.read()
scanners = [block.splitlines()[1:] for block in data.split('\n\n')]
scanners = [[tuple(map(int, line.split(','))) for line in scanner] for scanner in scanners]


def rotations(beacons):
    for x, y, z in permutations([0, 1, 2]):
        for sx, sy, sz in itertools.product([-1, 1], repeat=3):
            rotation_matrix = np.zeros((3, 3))
            rotation_matrix[0, x] = sx * 1
            rotation_matrix[1, y] = sy * 1
            rotation_matrix[2, z] = sz * 1
            if np.linalg.det(rotation_matrix) == 1:
                yield [np.matmul(rotation_matrix, b) for b in beacons]


def match(candidate, beacons):
    for b in beacons:
        for c in candidate:
            candidate_origin = np.subtract(b, c)
            zero_relative_beacons = [tuple(np.add(ca, candidate_origin)) for ca in candidate]
            common = set.intersection(set(zero_relative_beacons), set(beacons))
            if len(common) >= 12:
                return set(zero_relative_beacons) - set(beacons)
    return None


beacons = scanners[0]
sc_not_matched = list(range(1, len(scanners)))
while sc_not_matched:
    for i in tqdm(sc_not_matched.copy()):
        for rotated_beacons in rotations(scanners[i]):
            not_matched = match(rotated_beacons, beacons)
            if not_matched:
                sc_not_matched.remove(i)
                beacons += not_matched
                break
print(len(beacons))
