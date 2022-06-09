import sys

result = []
for i in range(0, int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for i in result:
    print(i)

