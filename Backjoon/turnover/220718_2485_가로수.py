from sys import stdin as std
from math import gcd

n = int(std.readline())
ip = []
gap = []
for i in range(n):
    ip.append(int(std.readline()))
    if i > 0:
        gap.append(ip[i] - ip[i-1])

g = gcd(*gap)
for i in range(len(gap)):
    gap[i] = (gap[i] // g) - 1

print(sum(gap))

