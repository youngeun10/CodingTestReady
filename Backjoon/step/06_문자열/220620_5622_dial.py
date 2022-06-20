dial = {"ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6, "MNO": 7, "PQRS": 8, "TUV": 9, "WXYZ": 10}

s = input()
result = 0

for a in s:
    for i in dial.keys():
        for x in i:
            if x == a:
                result += dial[i]

print(result)
