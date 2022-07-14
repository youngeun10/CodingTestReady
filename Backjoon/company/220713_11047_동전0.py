import sys

n, p = map(int, sys.stdin.readline().split())
coins = []
result = 0

for j in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

for i in coins:

    if p == 0:
        break
    else:
        result += p // i
    p %= i

print(result)


