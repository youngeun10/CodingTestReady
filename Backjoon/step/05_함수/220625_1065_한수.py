n = int(input())


def hansu(n):
    cnt = 0

    for i in range(1, n):
        if i < 100:
            cnt += 1
        else:
            if i // 100 - (i // 10 - (i // 100) * 10) == (i // 10 - (i // 100) * 10) - i % 10:
                cnt += 1
    return cnt


print(hansu(n+1))