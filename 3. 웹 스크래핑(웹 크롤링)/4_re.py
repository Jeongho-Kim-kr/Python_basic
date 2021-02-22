## 정규식 내용 요약(w3school.com, python.re 검색)
# 1. p = re.compile('원하는 형태')
# 2. m = p.match('비교할 문자열'): 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search('비교할 문자열'): 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall('비교할 문자열'): 일치하는 모든 것을 '리스트' 형태로 반환

# 원하는 형식: 정규식
# . (예 ca.e): 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (예 ^de): 문자열의 시작 > desk, destination (o) | fade (x)
# $ (예 se$): 문자열의 끝 > case, base (o) | sedan (x)


## 정규식 기본 1

# 정규식의 예시
# 주민등록번호
# 901201-1111111

# 이메일 주소
# nadocoding@gmail.com

# 차량번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1

import re
# ca?e 한자리를 모름

p = re.compile('ca.e') # re.complie: 변수에 문자열 조건을 넣어줌
# . (예 ca.e): 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (예 ^de): 문자열의 시작 > desk, destination (o) | fade (x)
# $ (예 se$): 문자열의 끝 > case, base (o) | sedan (x)

def print_match(m):
    if m:
        print(m.group()) # .group: 매칭을 확인, 매칭이 되면 출력 아님 에러
    else:
        print('매칭되지 않음')

m = p.match('case') # 변수.match(내용): 내용이 문자열 조건에 맞으면 변수에 추가
print_match(m) # 매칭되어 if구문이 출력

m = p.match('caffe')
print_match(m) # 매칭되지 않아 else구문이 출력

m = p.match('careless') # match: 주어진 문자열의 처음부터 일치하는지 확인
print_match(m) # 처음부분이 매치 되므로 뒤에 뭐가 있어도 if구문이 출력


## 정규식 기본 2
import re
p = re.compile('ca.e')

def print_match(m):
    if m:
        print('m.group():', m.group()) # 일치하는 문자열 반환
        print('m.string():', m.string) # 입력받은 문자열
        print('m.start():', m.start()) # 일치하는 문자열의 시작 index
        print('m.end():', m.end()) # 일치하는 문자열의 끝 index
        print('m.span():', m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print('매칭되지 않음')

m = p.search('careless') # search: 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

m = p.search('good care') # search: 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst = p.findall('careless') # findall: 일치하는 모든 것을 리스트 형태로 반환
print(lst)

lst = p.findall('good care')
print(lst)

lst = p.findall('good care cafe')
print(lst) # care, cafe가 출력