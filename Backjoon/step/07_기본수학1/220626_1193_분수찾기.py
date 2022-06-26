n = int(input())

l = 1
r = 1
s = 1

if n != 1:
    for i in range(n - 1):
        if s == 1 and l == 1:
            r += 1
            s = -1
        elif s == 1 and l != 1:
            l -= 1
            r += 1
        elif s == -1 and r == 1:
            l += 1
            s = 1
        elif s == -1 and r != 1:
            r -= 1
            l += 1

print("%d/%d" % (l, r))
