n = int(input())
cnt = 0

for i in range(n):
    words = input().upper()
    arr = []

    for j in range(len(words)):
        if arr:
            print(words[j])
            if words[j] == arr[-1]:
                arr.pop()
            else:
                arr.append(words[j])
        else:
            arr.append(words[j])
    if not arr:
        cnt += 1
print(cnt)