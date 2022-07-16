def ant(tx, tw):
    result = [0] * (2 * tw)
    tmp = 1
    for i in range(2 * tw):
        result[i] = tx
        if tx == tw:
            tmp = -1
        elif tx == 0:
            tmp = 1
        tx += tmp
    return result


w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x = ant(x, w)
y = ant(y, h)

print(x[t % (2*w)], y[t % (2*h)])
