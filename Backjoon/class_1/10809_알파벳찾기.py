s = list(input())
arr = [-1 for i in range(0, 26)]
for i in s:
    arr[ord(i)-ord('a')] = s.index(i)
for i in arr: print(i, end=' ')

"""
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')
"""