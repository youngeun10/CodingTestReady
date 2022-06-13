a = [i + 1 for i in range(0, 10000)]


def d(n):
    if n >= 1000:
        result = n + int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]) + int(str(n)[3])
    elif n >= 100:
        result = n + int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2])
    elif n >= 10:
        result = n + int(str(n)[0]) + int(str(n)[1])
    elif n > 0:
        result = 2 * n
    return result


for i in range(0, 10000):
    if d(i + 1) <= 10000 and d(i + 1) in a:
        a.remove(d(i + 1))

for i in a:
    print(i)
