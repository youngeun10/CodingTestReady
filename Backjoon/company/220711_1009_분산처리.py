import sys

t = [1, 4, 4, 2, 1, 1, 4, 4, 2]
n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    a = a % 10
    c = t[a-1] if b % t[a-1] == 0 else b % t[a-1]

    print((a ** c) % 10) if a != 0 else print("10")
