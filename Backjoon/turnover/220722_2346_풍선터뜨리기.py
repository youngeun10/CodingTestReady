from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque(list(map(int, stdin.readline().split())))
num = 0
result = [1]

for _ in range(n):


    arr.remove(arr[num])




