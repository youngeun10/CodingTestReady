scala = list(map(int, input().split()))
asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]
print("ascending") if scala == asc else (print("descending") if scala == des else print("mixed"))

# memory : 30840 time : 68

"""
print({"2345678":"ascending","7654321":"descending"}.get(input()[2::2],"mixed"))
"""