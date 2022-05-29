num = int(input())
val = list(input().split() for _ in range(num))

for a in val:
    n = int(a[0])
    arr = list(a[1])

    for i in arr:
        print(i*n, end='')
    print()

# memory : 30840 kb
# time : 68 ms

"""
memory : 29056
time : 52

t=int(input())
for i in range(t):
 a,b=input().split()
 for j in b:
  print(int(a)*j, end='')
 print()

"""