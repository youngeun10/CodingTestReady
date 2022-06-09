a, b = map(int, input().split())
c = int(input())

b = b + c
a = a + (b // 60)
b = b % 60

if a >= 24:
    print(a-24, b)
else:
    print(a, b)

