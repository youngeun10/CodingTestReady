""" 46. [비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기
a = int(input())
print(a << 1)
"""

""" 47. [비트 시프트 연산] 2의 거듭제곱 배로 곱해 출력하기."""
a, b = map(int, input().split())
b = 1 << b
print(a*b)
