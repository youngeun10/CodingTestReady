s = input().upper()
arr = []
for i in s:
    cnt = 0
    for j in range(0, len(arr)):
        if i == arr[j]:
            cnt += 1
    if cnt == 0:
        arr.append(i)
x = 0

for i in arr:
    if x < s.count(i):
        x = s.count(i)
        p = i
    elif x == s.count(i):
        p = '?'

print(p)

"""
n = input()
n = n.upper()
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
  result.append(n.count(i))
if result.count(max(result)) > 1:
  print("?")
else:
  print(alpa[result.index(max(result))])

"""

