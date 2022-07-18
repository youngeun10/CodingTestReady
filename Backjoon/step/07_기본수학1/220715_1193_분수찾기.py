x = int(input())
sum = 0
n = 1

while sum < x:
    sum += n
    n += 1

if n % 2 == 0:
    a = 1 + (sum - x)
    b = (n - 1) - (sum - x)
else:
    b = 1 + (sum - x)
    a = (n - 1) - (sum - x)

print("%d/%d" % (a, b))