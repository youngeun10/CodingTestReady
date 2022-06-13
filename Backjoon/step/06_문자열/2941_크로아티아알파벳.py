import sys

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = sys.stdin.readline()
cnt = 0

for i in croa:
    print(i)
    if a in i:
        cnt += 1
print(cnt)

