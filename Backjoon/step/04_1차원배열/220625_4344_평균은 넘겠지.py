import sys

n = int(sys.stdin.readline())


def func(a, avg):
    cnt = 0

    for i in a:
        if i > avg:
            cnt += 1

    return format(round(cnt / len(a) * 100, 3), ".3f")


for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    print(func(arr[1:], sum(arr[1:]) / len(arr[1:]))+'%')



