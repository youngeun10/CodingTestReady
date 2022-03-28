"""
    push X : 정수 x를 스택에 넣는 연산
    pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size : 스택에 들어있는 정수의 개수를 출력한다.
    empty : 스택이 비어있으면 1 아니면 0을 출력한다.
    top : 스택의 가장 위에있는 정수를 출력한다. 정수가 없을 경우 -1을 출력한다.

    # 1
        주어지는 명령의 수 입력
    # 2
        N개의 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
"""

num = int(input())
stack = []
result = []


def empty():
    if len(stack) == 0:
        result.append("1")
    else:
        result.append("0")


def pop_top():
    if len(stack) == 0:
        result.append("-1")
    else:
        result.append(stack[-1])
        if arr[0] == "pop":
            stack.pop()


for i in range(num):
    arr = list(input().split())

    if arr[0] == "push":
        stack.append(arr[1])
    elif arr[0] == "size":
        result.append(len(stack))
    elif arr[0] == "empty":
        empty()
    else:
        pop_top()

for i in result:
    print(i)








