import sys
cnt = 1
n = int(sys.stdin.readline())
ip = [list(map(int, sys.stdin.readline().split())) for x in range(0, n)]

for i in ip:
    print("Case #%d: %d + %d = %d" %(cnt, i[0], i[1], sum(i)))
    cnt += 1
