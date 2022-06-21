alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
cnt = 0

for i in alpha:
    if i in s:
        cnt += s.count(i)
        s = s.replace(i, "-")

cnt += len(s.replace('-', ''))
print(cnt)