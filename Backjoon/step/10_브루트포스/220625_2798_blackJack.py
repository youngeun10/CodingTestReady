import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


def blackJack(a, m):
    result = 0
    for i in range(0, len(a)-2):
        for j in range(i+1, len(a)-1):
            for k in range(j+1, len(a)):
                if result < a[i] + a[j] + a[k] <= m:
                    result = a[i] + a[j] + a[k]
    return result


print(blackJack(arr, s))
