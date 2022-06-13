import sys
import statistics as stt

n = int(sys.stdin.readline())
score = [list(map(int, sys.stdin.readline().split())) for i in range(0, n)]
result = []

for i in score:
    print(stt.mean(i[2:len(i)-1]))
