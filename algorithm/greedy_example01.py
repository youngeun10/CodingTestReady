"""
    n : 배열의 크기
    m : 숫자가 더해지는 횟수
    k : 연속으로 몇 개를 받을 것 인지.

"""
# n, m, k = list(map(int, input().split()))
# n_array = list(map(int, input().split()))
n, m, k = 5, 8, 3
n_array = [2, 4, 5, 4, 6]
n_array.sort(reverse=True)

result = 0
print(m)
print(k)

for i in range(m):
    for first in range(k):
        result = result + n_array[0]
        m = m - 1
    result = result + n_array[1]
    m = m - 1

print(result)
