import sys
t = int(sys.stdin.readline())
for i in range(0, t):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        print(h*100 + (n//h))
    else:
        print((n % h)*100 + (n//h)+1)