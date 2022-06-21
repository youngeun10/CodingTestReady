import sys

n = int(sys.stdin.readline())
cnt = 1
a = 1
b = 1
chk = -1

while cnt != n:
    if cnt == 1:
        b += 1
    else:
        if chk == -1:
            a += 1
            b -= 1
        elif chk == 1:
            a -= 1
            b += 1

        if a == 1:
            chk = -1
            b += 1
        if b == 1:
            chk = 1
            a += 1
    cnt += 1
    print("%d/%d" % (a, b))

print("%d/%d" % (a, b))

