import sys

n = int(sys.stdin.readline()) - 1
x = 0

while n >= 1:
    x += 1
    n -= 6 * x
print(x+1)

