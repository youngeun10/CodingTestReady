""" 71. [반복실행구조] 0 입력될 때까지 무한 출력하기
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        print(n)
"""

""" 72. [반복실행구조] 정수 1개 입력받아 카운트다운 출력하기. 
n = int(input())
while n > 0:
    print(n)
    n -= 1
"""

""" 73. [반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2 
n = int(input())
while n > 0:
    n -= 1
    print(n)
"""

""" 74. [반복실행구조] 문자 1개 입력받아 알파벳 출력하기 
n = ord(input())
arr = []
while ord('a') <= n:
    arr.append(chr(n))
    n -= 1

for i in range(0, len(arr)):
    print(arr.pop(), end=' ')
"""

""" 75. [반복실행구조] 정수 1개 입력받아 그 수 까지 출력하기1 """
n = int(input())
for i in range(0, n+1):
    print(i)
