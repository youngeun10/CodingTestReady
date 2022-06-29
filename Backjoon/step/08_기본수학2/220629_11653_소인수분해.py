n = int(input())
i = 2
result = []

while i <= n:
    if n % i == 0:
        result.append(i)
        n = n // i
        i = 2
    else:
        i += 1

for i in result:
    print(i)