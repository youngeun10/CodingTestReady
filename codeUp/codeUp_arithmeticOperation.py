""" 32. 정수 1개 입력받아 부호바꾸기
n = int(input())
print(-n)
"""

""" 33. 문자 1개 입력받아 다음 문자 출력하기 
a = ord(input()) + 1
print(chr(a))
"""

""" 34. 정수 2개 입력받아 차 계산하기 
a, b = map(int, input().split())
print(a-b)
"""

""" 35. 실수 2개 입력받아 곱 계산 
a, b = map(float, input().split())
print(a*b)
"""

""" 36. [산술연산] 단어 여러번 출력하기 
s, n = input().split()
print(s*int(n))
"""

""" 37. [산술연산] 문자 여러번 출력하기 (줄바꿈으로 숫자와 문자입력 구분)
n = int(input())
s = input()
print(s*n)
"""

""" 38. [산술연산] 거듭제곱 구하기. 
a, b = map(int, input().split())
print(a**b)
"""

""" 39. [산술연산] 
a, b = map(float, input().split())
print(a**b)
"""

""" 40. [산술연산] 몫 구하기 
a, b = map(int, input().split())
print(a//b)
"""

""" 41. [산술연산] 2개의 정수를 입력받아 나머지 계산.
a, b = map(int, input().split())
print(a % b)
"""

""" 42. [산술연산] 실수 1개 입력받아 소숫점이하 자리 변환하기. 
n = float(input())
print("%.2f" %n)
"""

""" 43. [산술연산] 실수 2개를 입력받아 나누고 소숫점 세번째 자리까지 출력.
a, b = map(float, input().split())
str = "{:.3f}".format(a/b)
print(str)
"""

""" 44. [산술연산] 정수 2개 입력받아 자동 계산하기. 
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a // b)
print(a % b)
result = "{:.2f}".format(a/b)
print(result)
"""

""" 45. [산술연산] 정수 3개 입력받아 합과 평균 구하기. 
a, b, c = map(int, input().split())
sum = a+b+c
print(sum, "{:.2f}".format(sum/3))
"""

