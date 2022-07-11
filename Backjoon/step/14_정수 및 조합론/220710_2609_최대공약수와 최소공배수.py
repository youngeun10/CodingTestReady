import sys

a, b = map(int, sys.stdin.readline().split())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


print(gcd(a, b))
print(a*b//gcd(a, b))