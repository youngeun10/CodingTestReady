import sys
n = int(sys.stdin.readline())
result = []

def chairman(a, b):
    if a < 0 or b < 0:
        return 0
    if a == 0:
        return b
    else:
        return chairman(a, b-1) + chairman(a-1, b)


for i in range(n):
    result.append(chairman(int(sys.stdin.readline()), int(sys.stdin.readline())))

for i in result:
    print(i)
