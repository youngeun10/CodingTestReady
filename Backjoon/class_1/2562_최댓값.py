"""
memory : 30840
time : 72
"""

arr = list(int(input()) for _ in range(9))

print(max(arr))
print(arr.index(max(arr))+1)

"""
memory : 29284
time : 52

l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)

"""