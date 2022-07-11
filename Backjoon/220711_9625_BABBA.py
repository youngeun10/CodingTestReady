def F(n):
    r = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        r[i] = r[i-1] + r[i-2]
    return r

k = int(input())
result = F(k)
print(result[k-1], result[k])