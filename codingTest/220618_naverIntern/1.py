import numpy as np


def transform_image(array, shift):
    n = len(arr)
    rt = [[0] * n for _ in range(n)]
    fl = [[0] * n for _ in range(n)]
    rl = [[0] * n for _ in range(n)]
    nis = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            rt[n - 1 - c][r] = arr[r][c]

    dic = {'rotated': rt, 'flipped': fl, 'rolled': rl, 'noised': nis}

    return dic


def rotated(arr):
    n = len(arr)
    result = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            result[n - 1 - c][r] = arr[r][c]

    print(result)
    return result


def flipped(arr):
    n = len(arr)
    result = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            result[n - 1 - c][c] = arr[r][c]
    return result


def rolled(arr, s):
    n = len(arr)
    result = [[0] * n for _ in range(n)]

    s = s % n

    for r in range(n):
        for c in range(n):
            result[r][(c + s) % n - 1] = arr[r][c]
    print(result)
    return result


def noised(arr):
    n = len(arr)
    result = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            a = np.random.randint(-0.05, 0.05, size=1)
            result[r][c] = result[r][c] + a
    print(result)
    return result



