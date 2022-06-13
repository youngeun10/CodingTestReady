import sys

n = int(sys.stdin.readline())
result = []

for i in range(0, n):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for i in range(0, n):
    print("Case #%d: %d" %(i+1, result[i]))