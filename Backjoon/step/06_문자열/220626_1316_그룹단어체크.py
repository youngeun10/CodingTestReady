# import sys
#
# n = int(sys.stdin.readline())
# arr = []
# result = 0
#
# for i in range(n):
#     arr.append(sys.stdin.readline())
#
#
# def checker(a):
#     r = []
#     for i in range(len(a)):
#         if i == 0:
#             r.append(a[i])
#         else:
#             if a[i] != a[i-1]:
#                 if a[i] in r:
#                     return False
#                 else:
#                     r.append(a[i])
#     return True
#
#
# for j in arr:
#     result += checker(j)
# print(result)


result = 0
for i in range(int(input())):
    word = input()
    print(sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.find):
        print(sorted(word, key=word.find))
        result += 1
print(result)