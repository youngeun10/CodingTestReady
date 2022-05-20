""" 63. [3항연산] 정수 2개 입력받아 큰 값 출력하기.
a, b = map(int, input().split())
print(a) if a > b else print(b)
"""

""" 64. [3항연산] 정수 3개 입력받아 가장 작은 값 출력하기. 
a, b, c = map(int, input().split())
print(a) if (a < b) & (a < c) else (print(b) if b < c else print(c))
# 깨달은 점 : 비트 연산자 (&, |)가 비교 연산자(>, <) 보다 우선순위가 높다!
"""

