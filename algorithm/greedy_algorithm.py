""" 잔돈이 1260원 있을 때 잔돈의 최소 개수 구하기 """
change = 1260
cnt = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    q, r = divmod(change, coin)
    cnt = cnt + q
    change = r

print(cnt)

