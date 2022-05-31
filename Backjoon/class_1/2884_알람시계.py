h, m = map(int, input().split())
if m >= 45:
    m -= 45
else:
    m += 15
    h -= 1
    if h == -1: h = 23
print(h, m)

"""
a,b=map(int,input().split())
c=a*60+b-45
print(c//60%24, c%60)
"""
