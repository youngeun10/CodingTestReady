from sys import stdin as std

n, k = map(int, std.readline().split())
arr = [i for i in range(2, n+1)]
cnt = 1

for i in range(n):
    t = arr[0]
    for j in range(1, (n // arr[0]) + 1):

        if t * j in arr:
            if cnt == k:
                print(t * j)
                quit()
            arr.remove(t * j)
            cnt += 1
        else:
            continue