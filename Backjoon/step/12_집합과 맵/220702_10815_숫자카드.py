import sys

n = int(sys.stdin.readline())
sg = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cmp = list(map(int, sys.stdin.readline().split()))

sg.sort()

def bin_search(arr, key):
    pl = 0
    pr = len(arr)-1

    while True:
        pc = (pl + pr) // 2
        if arr[pc] == key:
            return 1
        elif arr[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            return 0


for i in cmp:
    print(bin_search(sg, i), end=' ')

