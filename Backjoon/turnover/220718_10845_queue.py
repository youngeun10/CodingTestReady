import sys

n = int(sys.stdin.readline())
q = []

for i in range(n):
    str = sys.stdin.readline().split()

    if str[0] == "push":
        q.append(str[1])
    elif str[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.pop(0)
    elif str[0] == "size":
        print(len(q))
    elif str[0] == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif str[0] == 'front':
        print(-1) if len(q) == 0 else print(q[0])
    elif str[0] == 'back':
        print(-1) if len(q) == 0 else print(q[-1])
