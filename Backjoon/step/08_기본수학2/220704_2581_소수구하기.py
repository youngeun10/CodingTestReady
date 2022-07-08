import sys


def isPrime(a):
    if a < 2:
        return False

    for i in range(2, a):
        if a % i == 0:
            return False
    return True


n, m = map(int, sys.stdin.readline().split())

for i in range(n, m+1):

    if i % 2 != 0:
        if isPrime(i):
            print(i)


