n = int(input())
arr = []
for i in range(0, n):
    arr.append(map(int, input().split(maxsplit=1)))

for i in arr:
    print(sum(i))

