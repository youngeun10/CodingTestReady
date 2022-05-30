n = int(input())
result = []
for i in range(0, 5):
    arr = list(input())
    tmp = list(range(len(arr)))
    for j in arr:
        print(j)
        # if arr[j] == 'X':
        #     tmp.append(0)
        # elif arr[j] == 'O':
        #     tmp.append(1) if j == 0 else tmp.append(arr[j-1]+1)
    result.append(sum(tmp))
print(result)

