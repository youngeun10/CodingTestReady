a = input()
b = input()

for i in range(0, 10):
    a = a.replace(str(i), "")


if a.find(b) < 0:
    print("0")
else:
    print("1")

