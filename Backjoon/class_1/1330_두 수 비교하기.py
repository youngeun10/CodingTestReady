a, b = map(int, input().split())

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")

"""
속도 -20ms
a, b = map(int, input().split())
print('>' if a > b else ('<' if a < b else '=='))


"""
