import sys

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr.count(0) == 3:
        break
    else:
        arr.sort()
        print("right") if arr[2]**2 == arr[0]**2 + arr[1]**2 else print("wrong")

    