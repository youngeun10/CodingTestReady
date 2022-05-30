n = int(input())
result = []
for i in range(0, n):
    arr = list(input())
    tmp = []
    for j in arr:
        if j == 'X':
            tmp.append(0)
        elif j == 'O':
            tmp.append(1) if len(tmp) == 0 else tmp.append(tmp[-1]+1)
    result.append(sum(tmp))
for i in result: print(i)

# memory : 30840    time : 76
"""
import sys
N = int(sys.stdin.readline())
for i in range(N):
    quiz_result = sys.stdin.readline()
    accum = 1
    score = 0
    for q in quiz_result:
        if q is 'O':
            score += accum
            accum += 1
        else:
            accum = 1
    print(score)
"""
