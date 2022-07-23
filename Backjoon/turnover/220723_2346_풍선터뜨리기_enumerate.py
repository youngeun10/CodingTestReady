from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque(enumerate(map(int, stdin.readline().split())))
result = []

for _ in range(n):
    index, n = arr.popleft()
    result.append(index+1)
    if n > 0:
        arr.rotate(-1 * (n-1))
    else:
        arr.rotate(-1 * n)
print(*result)