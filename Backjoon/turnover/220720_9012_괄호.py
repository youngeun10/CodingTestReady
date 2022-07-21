import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().strip()
    stack = deque([])
    chk = 0
    for i in a:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                print("NO")
                chk = 1
                break
            else:
                stack.pop()

    if len(stack) == 0 and chk == 0:
        print("YES")
    elif len(stack) > 0:
        print("NO")