import sys

n = int(sys.stdin.readline())
tmp = n
cnt = 1

while True:
    if tmp < 10:
        tmp = tmp * 11
    else:
        tmp = (tmp % 10) * 10 + (tmp // 10 + tmp % 10) % 10

    if tmp == n:
        print(cnt)
        break
    else:
        cnt += 1
        