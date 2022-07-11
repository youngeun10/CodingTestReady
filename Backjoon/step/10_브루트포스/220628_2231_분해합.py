a = input()
result = int(a)
tmp = list(a)

for i in tmp:
    result += int(i)

print(result)