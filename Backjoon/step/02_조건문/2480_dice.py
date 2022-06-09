a, b, c = map(int, input().split())

if a == b and b == c:
    result = 10000 + b * 1000
elif a == b and b != c:
    result = 1000 + b * 100
elif a == c and b != a:
    result = 1000 + c * 100
elif c == b and b != a:
    result = 1000 + c * 100
else:
    result = max(a, b, c) * 100
print(result)
