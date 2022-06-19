import numpy as np


def transform_image(array, shift):
    n = len(array)
    s = shift % n

    rt = [[0] * n for _ in range(n)]
    fl = [[0] * n for _ in range(n)]
    rl = [[0] * n for _ in range(n)]
    nis = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            rt[n - 1 - c][r] = array[r][c]
            fl[n - 1 - c][c] = array[r][c]
            rl[r][(c + s) % n - 1] = array[r][c]

            a = np.random.randint(-0.05, 0.05, size=1)

            nis[r][c] = array[r][c] + a

    dic = {'rotated': rt, 'flipped': fl, 'rolled': rl, 'noised': nis}

    return dic




