import sys

n = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

if 1 in arr:
    arr.remove(1)

for i in arr:
    tmp = 0
    for x in range(2, i):
        if i % x == 0:
            tmp += 1
    if tmp == 0:
        cnt += 1
print(cnt)