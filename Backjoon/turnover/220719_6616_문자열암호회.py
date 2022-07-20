from sys import stdin as std
from collections import deque

while True:
    n = int(std.readline())

    if n == 0:
        break
    else:
        s = std.readline()
        s = s.upper()
        s = s.replace(' ', '')
        s = deque(s)
        s.remove('\n')
        result = deque([0] * len(s))
        cnt = 0
        for i in range(n):

            for j in range((len(s)//n) + 1):
                if len(s) > i+(n*j):
                    result[i+(n*j)] = s[cnt]
                    cnt += 1
                else:
                    continue
        print(*result, sep='')