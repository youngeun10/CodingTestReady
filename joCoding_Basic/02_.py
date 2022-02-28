a = 3
b = 4

print(a)

print(type(a))

# 몫이 나오는 값
print(a//b)

# 나머지
print(a % b)

# 한 줄 띄기
string = 'Life is too short \n You need python'
print(string)

# 여러 번 출력하기
c = "Python"
print(c * 10)

# 인덱싱
print(string[0])
# 거꾸로 단어의 인덱싱
print(string[-1])

# 문자열 자료형 = 문자열변수명[이상:미만:간격]
print(string[:8:2])

# 거꾸로 단어 읽기
print(string[::-1])

# 포맷팅
d = "이름 : {name} / 나이: {age} " .format(name="이시영", age=15)
print(d)

# 정해진 형식에 변수에 값 넣기
f = 3.141592
e = "%.5f" % f
print(e)

# 문자열 개수 세기 = 변수명.count('[개수 셀 문자]')
print(string.count('o'))

# 문자열의 위치 찾기 = 변수명.find('[찾을 문자]') * 해당 문자가 없을 경우 -1 반환 (같은 내용은 index로 사용시 해당 문자가 없을 경우 오류발생)
print(string.find('too'))

# 문자열 삽입 = [삽입할 문자/문자열].join([원본 문자])
g = ','
print(g.join('abcd'))

# 대소문자 변경 - upper, lower

# 공백 지우기 - strip / lstrip / rstrip
h = '   hello   '
print(h + 'a')
print(h.lstrip() + 'a')
print(h.rstrip() + 'a')
print(h.strip() + 'a')

# 문자열 교체 - 문자열이 담긴 변수명.replace([바꿀 문자열], [대체로 넣을 문자열])
print(string.replace('Life', 'Your leg'))

# 문자열 잘라서 배열에 저장 - 문자열변수명.split()
print(string.split())