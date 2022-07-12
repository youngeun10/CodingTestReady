import sys
n = int(sys.stdin.readline())
arr = [0] * n

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    arr.append((a, b))
    # a[i] = list(map(str, sys.stdin.readline().split()))

arr.sort(key=lambda x: x[0])

print(arr)
