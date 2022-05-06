
result_list = []
n, l = map(int, input().split())


def print_list(result):
    if 1 < len(result) <= 100:
        print(result)
    else:
        print('-1')

def part_sum(st, cnt):
    sum = 0
    for i in range(0,cnt):
        sum = sum + st + i

    return sum




print_list(result_list)
