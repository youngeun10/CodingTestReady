""" 65. [선택실행구조] 정수 3개 입력받아 짝수만 출력하기.
arr = list(map(int, input().split()))

for i in arr:
    if i % 2 == 0:
        print(i)
"""

""" 66. [선택실행구조] 정수 3개 입력받아 짝/홀 출력하기. 
arr = list(map(int, input().split()))

for i in arr:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
"""

""" 67. [선택실행구조] 정수 1개 입력받아 분류하기
num = int(input())

if num < 0:
    print("A") if num % 2 == 0 else print("B")
else:
    print("C") if num % 2 == 0 else print("D")
"""

""" 68. [선택실행구조] 점수 입력받아 평가 출력하기. 
num = int(input())
if 90 <= num <= 100:
    print("A")
elif 70 <= num:
    print("B")
elif 40 <= num:
    print("C")
else:
    print("D")
"""

""" 69. [선택실행구조] 평가 입력받아 다르게 출력하기. 
c = input()
if c == 'A':
    print("best!!!")
elif c == 'B':
    print("good!!")
elif c == 'C':
    print("run!")
elif c == 'D':
    print("slowly~")
else:
    print("what?")
"""

""" 70. [선택실행구조] 월 입력받아 계절 출력하기 """
n = int(input())
if (n // 3 == 4) | (n // 3 == 0):
    print("winter")
elif n // 3 == 1:
    print("spring")
elif n // 3 == 2:
    print("summer")
elif n // 3 == 3:
    print("fall")
