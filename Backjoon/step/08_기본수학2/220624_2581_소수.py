import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

result = []


def isPrime(a):
    if a < 2:
        return False

    for i in range(2, a):
        if a % i == 0:
            return False
    return True


for i in range(n, m + 1):
    if isPrime(i):
        result.append(i)


if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))