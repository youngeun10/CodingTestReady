apart = []
for i in range(15):
    tmp = [1, ]
    for j in range(1, 15):
        if i == 0:
            tmp.append(j+1)
        else:
            tmp.append(tmp[j-1] + apart[i-1][j])
    apart.append(tmp)

from sys import stdin as std

n = int(std.readline())
for i in range(n):
    a = int(std.readline())
    b = int(std.readline())

    print(apart[a][b-1])


