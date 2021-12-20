import numpy as np

with open('input.txt') as f:
    data = f.read()

alg, img = data.split('\n\n')

coding = {
    '.': '0',
    '#': '1',
}

alg = [coding[s] for s in alg]
img = [[coding[s] for s in line] for line in img.split('\n')]


def filter(win, alg):
    return alg[int(''.join(win.flatten()), 2)]


pad_symbol = '0'
img = np.array(img)
rel_size = img.shape
pad_size = 2

for k in range(50):
    img_shape = img.shape
    img = np.pad(img, pad_size, constant_values=pad_symbol)
    transformed = img.copy()
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            win = img[i-1:i+2, j-1:j+2]
            transformed[i, j] = filter(win, alg)
    pad_symbol = alg[int(9 * pad_symbol, 2)]
    transformed = transformed[1: img.shape[0] - 1, 1: img.shape[1] - 1]
    img = transformed
print(np.sum(img == '1'))
