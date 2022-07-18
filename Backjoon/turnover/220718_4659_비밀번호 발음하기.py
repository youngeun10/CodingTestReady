while True:
    v = 'aeiou'
    c = 'bcdfghjklmnpqrstvwxyz'

    t = input()

    if t == 'end':
        break

    # 모음 포함
    vc = []
    for i in v:
        vc.append(t.count(i))
    if sum(vc) == 0:
        print(f'<{t}> is not acceptable.')
        continue

    # 모음/자음 연속 3개
    v_cnt = 0
    c_cnt = 0
    chk = 0
    for i in t:
        if i in v:
            v_cnt += 1
        else:
            v_cnt = 0
        if i in c:
            c_cnt += 1
        else:
            c_cnt = 0
        if v_cnt == 3 or c_cnt == 3:
            chk = 1
            break

    if chk == 1:
        print(f'<{t}> is not acceptable.')
        continue

    # 같은 글자 연속
    v = v.replace('e', '')
    v = v.replace('o', '')
    v = v + c
    for i in v:
        if i*2 in t:
            chk = 1
            break

    if chk == 1:
        print(f'<{t}> is not acceptable.')
        continue

    print(f'<{t}> is acceptable.')