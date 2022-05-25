n = int(input())
score = list(map(int, input().split()))
result = []

for i in score:
    result.append(i*100/max(score))

print(round(sum(result)/len(result), 6))


