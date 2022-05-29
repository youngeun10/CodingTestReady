# memory : 30840kb
# time : 72ms

n = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

a, b, c = list(int(input()) for _ in range(3))

arr = list(str(a*b*c))

for i in arr:
    n[i] += 1

for i in n.values():
    print(i)

"""
memory : 29056
time : 52

a = int(input())
b = int(input())
c = int(input())

d = list(map(int, (str(a * b * c))))

for i in range(10):
    print(d.count(i))
"""
