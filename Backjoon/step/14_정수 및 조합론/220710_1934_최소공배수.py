import sys


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a * b // gcd(a, b))
