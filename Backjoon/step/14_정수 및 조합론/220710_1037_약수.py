import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

if len(a) == 1:
    print(a[0]**2)
else:
    print(a[0] * a[len(a)-1])