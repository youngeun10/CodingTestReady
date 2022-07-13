def f0(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 0
    return f0(n-1) + f0(n-2)

def f1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return f1(n-1) + f1(n-2)

t = int(input())
for i in range(t):
    n = int(input())
    print(f0(n), f1(n))
