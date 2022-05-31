n, x = map(int, input().split())
n_arr = map(int, input().split())
for i in n_arr:
    if i < x:
        print(i, end=' ')

"""
a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b] ?
print(' '.join(score))
"""
