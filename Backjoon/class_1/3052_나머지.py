arr = []
for i in range(0, 10):
    a = int(input()) % 42
    if arr.count(a) == 0:
        arr.append(a)
print(len(arr))

"""
b = [int(input())%42 for i in range(10)]
print(len(set(b)))
"""