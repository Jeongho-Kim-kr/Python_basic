## 점프 투 파이썬 https://wikidocs.net/book/1
## 파이썬 기본 문법 https://www.youtube.com/watch?v=kWiCuklohdY (나도코딩 파이썬 기본)
## 목차

## 숫자형
## 문자형
## 참 / 거짓
## 변수
## quiz 1 변수형식 활용
## 연산자
## 수식
## 숫자처리함수
## 랜덤 함수
## 퀴즈 2 랜덤 추출
## 문자열
## 슬라이싱(필요한 부분만 잘라오기)
## 문자열 처리 함수
## 문자열 포맷
## 탈출문자
## 퀴즈3 변수내 인덱스(주소) 활용
## 리스트
## 사전
## 튜플
## 집합(set) 중복 안됨, 순서 없음
## 자료구조의 변경
## 퀴즈 4 랜덤 추출, range로 숫자 생성
## if 조건문
## for 반복문
## while 반복문
## continue와 break
## enumerate(인덱스와 함수값 사용)
## 이중 for문 즉시 탈출(고급)
## for문 활용. 변수에 함수 반복 적용
## 퀴즈5 for, if
## 함수(입금, 출금 예시)
## 함수(기본값 설정)
## 함수(키워드값: 키워드=으로 정의하면 순서가 안맞아도 호출 가능하다)
## 함수(가변인자)
## 함수(지역변수, 전역변수 / 함수내와 밖은 서로 변수를 공유하지 않음 그러므로 외부의 변수를 사용하려면 'global 변수(전역변수)'를 함수 내부에 정의해 줘야 함)
## 퀴즈 6 함수
## 표준 입출력(입출력 형식 수정하기, 꾸미기)
## 다양한 출력포멧
## 파일 입출력(불러오기, 내보내기)
## pickle(사용하는 데이터를 파일 형태로 저장)
## with(pickle이나 여러 파일을 읽거나 쓰고 닫음)
## 퀴즈 7 파일
## 클래스
## 클래스(__init__)(위에서 만든 Unit 클래스 이용)
## 클래스(멤버 변수: 밖에서도 한 변수에게만 이용과 추가 가능)(위에서 만든 Unit 클래스 이용)
## 클래스(메소드: 클래스에 함수를 넣어 변수에 내장하는 방법)
## 클래스(상속)
## 클래스(다중 상속)
## 클래스(메소드 오버라이딩: 자식 클래스가 부모 클래스 메소드 함수를 가져와서 덧씌워 사용)
## pass
## 클래스(super: 부모 클래스 변수 상속받는 다른 방법, 다중 상속시 사용 불가)
## 클래스(isinstance: 여러 변수 중 해당 클래스로 만든 변수를 지정 검색), 클래스 종합 정리(클래스를 이용한 스타크래프트)
## 퀴즈8(클래스)
## 예외처리(try, except)
## 예외처리(원하지 않는 상황에서 일부러 에러 발생시키기)(try, raise, except)
## 예외처리(사용자 정의)(class, try, raise, except)
## 예외처리(finally: try구문이 잘 작동 하던지 오류로 except로 빠지던지, except로 정의되지 않은 오류로 프로그램이 작동 안하던지 모든 게 끝난 후 작동하는 구문)
## 퀴즈9(예외처리)
## 모듈
## 패키지: 모듈들을 모아둔 폴더
## __all__(패키지의 디폴트 모듈 사용 지정)
## 모듈 직접 실행(__name__을 모듈에 넣어서 확인 가능 'thailand.py'모듈 확인)
## 패키지, 모듈 위치 확인(inspect 패키지)
## pip install(패키지 설치하기, pypi를 이용해 패키지를 검색)
## 내장함수(구글에 'list of python builtins'를 검색해 확인 가능)
## 외장함수(import해서 이용, 구글에서 'list of python modules'를 검색해 확인 가능)
## 퀴즈10(모듈, 패키지)(quiz10.py확인)


## 숫자형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))


## 문자형
print('풍선')
print("나비")
print('ㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
print('ㅋ'*9)


## 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))


## 변수
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 강아지의 이름은 연탄이예요')
print('연탄이는 4살이며, 산책을 아주 좋아해요')
print('연탄이는 어른일까요? Ture')

print('우리집 ' + animal + '의 이름은 ' + name + '예요')

hobby = '낮잠'
# print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 아주 좋아해요')
print(name, '는 ', age, '살이며, ', hobby, '을 아주 좋아해요') # 이 경우 형식을 str로 변환 안해도 되지만 변수간 띄어쓰기가 생긴다
print(name + '는 어른일까요? ' + str(is_adult))


## quiz 1 변수형식 활용
station = '사당'
print(station + '행 열차가 들어오고 있습니다.')
station = '신도림'
print(station + '행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station + '행 열차가 들어오고 있습니다.')


## 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3 = 8
print(2%5) # 나머지 구하기 2
print(5//3) # 몫 구하기 1

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3) # 앞뒤가 같으면 True
print(3 + 4 == 7) # True
print(1 != 3) # 앞뒤가 다르면 True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # and 교집합 True
print((3 > 0) & (3 < 5)) # and 교집합 Ture

print((3 > 0) or (3 > 5)) # or 합집합 Ture
print((3 > 0) | (3 > 5)) # or 합집합 Ture


## 수식
number = 2 + 3 * 4 # 14
number = number + 2 # 16
number += 2 # 18 (number = number + 2)
number *= 2 # 36 (number = number * 2)
number /= 2 # 18
number -= 2 # 16
number %= 5 # 1


## 숫자처리함수
print(abs(-5)) # 5 절댓값
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 12 최댓값
print(min(5, 12)) # 5 최솟값
print(round(3.14)) # 3 반올림

from math import * # 매스 라이브러리
print(floor(4.99)) # 4 내림
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 제곱근


## 랜덤 함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10 + 1)) # 0 ~ 10 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성


## 퀴즈 2 랜덤 추출
from random import *
date = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월 ' + str(date) + '일로 선정되었습니다.')


## 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


## 슬라이싱(필요한 부분만 잘라오기)
jumin = "990120-1234567" # 주민번호
print("성별 : " + jumin[7]) # 맨앞에 위치는 0번째
print("연 : " + jumin[0:2]) # 0 ~ 2 직전위치 까지(0, 1위치)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전위치 까지
print("뒤 7자리 : " + jumin[7:])
print('뒤 7자리 (뒤에서부터) :' + jumin[-7:]) # -들어가면 역방향으로 감


## 문자열 처리 함수
python = 'Python is Amazing'
print(python.lower()) # 모든문자 소문자
print(python.upper()) # 모든문자 대문자
print(python[0].isupper()) # 해당위치 대문자 판단
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 변수 변환 해당 글자를 찾아 2번째 문자로 변경

index = python.index('n') # 첫번째 해당 변수를 찾아 해당 위치로 변환
print(index)
index = python.index('n', index + 1) # 첫번째 변수 위치 이후에 해당 변수를 찾아 위치로 변환
print(index)

print(python.find('n')) # index: 위치로 변환, find: 찾아 위치로 변환
print(python.count('n')) # 몇변 들어갔는지 count


## 문자열 포맷
print('나는 %d살입니다.' % 20)
print('나는 %s을 좋아해요.' % '파이썬')
print('Apple은 %c로 시작해요.' %'A')
print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color = '빨간'))
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')


## 탈출문자
print('백문이 불여일견\n 백견이 불여일타') # \n : 줄바꿈
print('저는 "나도코딩" 입니다.') # 저는 "나도코딩"입니다.
print("저는 \"나도코딩\"입니다.") # \는 다음 부호를 문장내에 사용 ex) \\: 문장내에서 \
print('Red Apple\r Pine') # \r: 커서를 맨 앞으로 이동 이때는 \r이후 앞으로 가서 Pine을 Red 에 덮어씀
print('Redd\bApple') # \b: 백스페이스(한글자 삭제)
print('Red\tApple') # \t: 탭


## 퀴즈3 변수내 인덱스(주소) 활용
url = 'http://naver.com'
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print('{} 의 비밀번호는 {} 입니다.'.format(url, password))


## 리스트
subway = ['유재석', '조세호', '박명수']
print(subway)
print(subway.index('조세호'))

subway.append('하하') # 리스트 마지막 위치에 추가
print(subway)
subway.insert(1, '정형돈') # 리스트 0과 1 사이 위치에 추가

print(subway.pop()) # 가장 뒤에 있는 변수를 빼냄
print(subway)

subway.append('유재석')
print(subway)
print(subway.count('유재석')) # 변수 갯수 새기

num_list = [5,2,3,1,4]
num_list.sort() # 리스트내 정렬
print(num_list)

num_list.reverse() # 리스트내 역정렬
print(num_list)

num_list.clear() # 리스트내 지우기
print(num_list)

mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list) # 두 리스트 합치기
print(num_list)


## 사전
cabinet = {3:'유재석', 100:'김태호'} # 중괄호 시 변수에 키를 부여할 수 있음 
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) # print(cabinet[5]) 이면 오류가 나지만 .get이용시 none이 출력된다.
print(cabinet.get(5, '사용 가능')) # .get을 이용해 키에 해당하는 변수 바로 지정
print(3 in cabinet) # True
print(4 in cabinet) # False

cabinet = {'A-3':'유재석', 'B-100':'김태호'} # 문자도 키로 지정 가능
print(cabinet)
cabinet['A-3'] = '김종국' # 유재석이 빠지고 김종국이 해당키로 업데이트
cabinet['C-20'] = '조새호'
del cabinet['A-3'] # 해당 키 삭제
print(cabinet.keys()) # 들어있는 키를 확인
print(cabinet.values()) # 들어있는 값을 확인
print(cabinet.items()) # 키:값 으로 출력
cabinet.clear() # 초기화


## 튜플
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])
# menu.add("생선까스") 튜플은 .add로 추가 불가

(name, age, hobby) = ('김종국', 20, '코딩') # 한번에 정의 가능
print(name, age, hobby)


## 집합(set) 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

print(java & python) # 교집합
print(java.intersection(python)) # 교집합

print(java | python) # 합집합
print(java.union(python)) # 합집합

print(java - python) # 차집합
print(java.difference(python)) # 차집합

python.add('김태호') # 집합에 원소 추가
java.remove('김태호')# 집합에 원소 제거


## 자료구조의 변경
menu = {'커피', '우유', '주스'}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


## 퀴즈 4 랜덤 추출, range로 숫자 생성
users = range(1, 21) # 1부터 21직전까지 숫자를 생성
users = list(users)
print(users)

from random import *
shuffle(users)
print(users)

winners = sample(users, 4)

print('-- 당첨자 발표 --')
print('치킨 당첨자: {}'.format(winners[0]))
print('커피 당첨자: {}'.format(winners[1:]))
print('-- 축하합니다 --')


## if 조건문
weather = input('오늘 날씨는 어때요? ')
if weather == '비':
    print('우산을 챙기세요')
elif weather == "미세먼지":
    print('마스크를 챙기세요')
else:
    print('준비물 필요 없어요')

temp = int(input('기온은 어때요? '))
if 30 <= temp:
    print('너무 더워요. 나가지 마세요')
elif 10 <= temp and temp <30:
    print('괜찮은 날씨에요')
elif 0 <= temo <10:
    print('외투를 챙기세요')
else:
    print('너무 추워요. 나가지 마세요')


## for 반복문
for wating_no in range(1, 6):
    print('대기번호 : {0}'.format(wating_no))

starbucks = ['아이언맨', '토르', '그루트']
for customer in starbucks:
    print('{0}, 커피가 준비되었습니다.'.format(customer))


## while 반복문
customer = '토르'
index = 5
while index >= 1:
    print('{0}, 커피가 준비 되었습니다. {1}번 남았어요.'.format(customer, index))
    index -= 1
    if index == 0:
        print('커피는 페기처분 되었습니다.')

## customer = '아이언맨'
## index = 1
## while True:
##     print('{0}, 커피가 준비 되었습니다. 호출 {1}회.'.format(customer, index))
##     index += 1
## 무한 루프시 Ctrl + C를 눌러서 강제종료

customer = '토르'
person = 'Unknown'
while person != customer:
    print('{0}, 커피가 준비 되었습니다.'.format(customer))
    person = input('이름이 어떻게 되세요?')
    print('커피 맛있게 드세요')


## continue와 break
absent = [2, 5] # 결석
no_book = [8] # 책을 안가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print('오늘 수업 여기까지. {0}는 교무실로 따라와.'.format(student))
        break
    print('{0}, 책을 읽어봐'.format(student))


## enumerate(값의 순서를 이용할 때 사용, 해당 변수의 인덱스 값과 element 값을 앞의 벨류에 넣는다.)
lst = ['가', '나', '다']

for lst_idx, lst_val in enumerate(lst): # lst안의 인덱스(순서)와 값이 들어감
    print(lst_idx, lst_val) # 해당 elemnt의 인덱스값, 값 순서로 출력


## 이중 for문 즉시 탈출(고급)
balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

# 이때 break는 안에 있는 for문만 탈출하므로 44만 출력 안하고 탈출 하지만 다시 위의 for문을 실행해 ball 4 와 안의 weapon이 출력된다
for ball_idx, ball_val in enumerate(balls):
    print('ball:', ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print('weapons: ', weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print('공과 무기가 충돌')
            break

# for문 즉시 탈출 문제 해결책
# 따라서 안의 for에서 즉시 탈출을 명시하고 싶으면 안쪽 for문이 동작하지 않을 때(break) 넘어가는 else를 이용한다(안쪽 for문이 제대로 동작하면 else에 도착할 일이 없이 잘 작동된다). else에는 continue가 있어 else에 오게 되면 이후 break를 받고 전체가 종료된다.
for ball_idx, ball_val in enumerate(balls):
    print('ball:', ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print('weapons: ', weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print('공과 무기가 충돌')
            break
    else:
        continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
    print('바깥 for 문 break')
    break # 안쪽 for 문에서 break를 만나면 여기로 진입 가능. 2중 for문을 한번에 탈출

# 구조
for 바깥조건:
    바깥동작
    for 안쪽조건:
        안쪽 동작
        if 충돌조건:
            break
    else:
        continue
    break


## for문 활용. 변수에 함수 반복 적용
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ['Iron man', 'Thor', 'Groot']
students = [len(i) for i in students] # 길이로 변환
print(students)

students = ['Iron man', 'Thor', 'Groot']
students = [i.upper()for i in students] # 대문자로 변환
print(students)


## 퀴즈5 for, if
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))


## 함수(입금, 출금 예시)
def open_account():
    print('새로운 계좌가 생성되었습니다.')

def deposit(balance, money): # 입금
    print('입금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print('출금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance - money))
        return balance - money
    else:
        print('잔액이 부족합니다. 잔액은 {0} 원입니다.'.format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    if balance >= (money + commission):
        print('출금이 완료되었습니다. 수수료 {0} 원이며, 잔액은 {1} 원입니다.'.format(commission, balance - money - commission))
        return commission, balance - money - commission
    else:
        print('잔액이 부족합니다. 수수료 {0} 원이며, 잔액은 {1} 원입니다.'.format(commission, balance))
        return commission, balance

account = open_account()
balance = 0
balance = deposit(balance, 3000)
balance = withdraw(balance, 2000)
balance = withdraw_night(balance, 1000)


## 함수(기본값 설정)
def profile(name, age, main_lang):
    print('이름: {0}\t나이: {1}\t주 사용 언어: {2}'\
        .format(name, age, main_lang))

profile('유재석', 20, '파이썬')
profile('김태호', 25, '자바')

# 같은 학교 같은 학년 같은 반 같은 수업 일시 기본값을 지정

def profile(name, age = 17, main_lang = '파이썬'): # 전달받지 않을 시 기본값을 사용
    print('이름: {0}\t나이: {1}\t주 사용 언어: {2}'\
        .format(name, age, main_lang))

profile('유재석')
profile('김태호')


## 함수(키워드값: 키워드=으로 정의하면 순서가 안맞아도 호출 가능하다)
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = '유재석', main_lang = '파이썬', age = 20)
profile(main_lang = '자바', age = 25, name = '김태호')


## 함수(가변인자)
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print('이름: {0}\t 나이: {1}\t'.format(name, age), end = " ") # end = " "을 넣으면 다음 출력이 한줄에 같이 나옴
    print(lang1, lang2, lang3, lang4, lang5)

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#')
profile('김태호', 25, 'Kotlin', 'Swift', '', '', '')

def profile(name, age, *language): ## *로 인자의 갯수를 가변해 늘리거나 줄임
    print('이름: {0}\t 나이: {1}\t'.format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#', 'javaScript')
profile('김태호', 25, 'Kotlin', 'Swift')


## 함수(지역변수, 전역변수 / 함수내와 밖은 서로 변수를 공유하지 않음 그러므로 외부의 변수를 사용하려면 'global 변수(전역변수)'를 함수 내부에 정의해 줘야 함)
gun = 10 # 전역변수
def checkpoint(soldiers): # 경계근무
    gun = 20 # 지역변수(함수는 내부에 정의를 필요로함)
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print('전체 총: {0}'.format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print('남은 총: {0}'.format(gun))


gun = 10
def checkpoint(soldiers):
    global gun # 전역공간에 있는 gun 사용(일반적으로 사용 x)
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print('전체 총: {0}'.format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print('남은 총: {0}'.format(gun))

# 가장 좋은 함수 내 변수 처리
gun = 10
def checkpoint_ret(gun, soldiers): # 값을 받고 리턴함 사용시는 변수에 덮어씌움(전역변수 사용보다 바람직한 방법)
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

gun = checkpoint_ret(gun, 2) # 외부에서 gun 값을 받아 함수에 적용 후 리턴값을 변수에 저장(일반적 방법)


## 퀴즈 6 함수
def std_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = '남자'
weight = round(std_weight(height / 100, gender), 2)
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))


## 표준 입출력(입출력 형식 수정하기, 꾸미기)
print('Python', 'Java', sep = ", ") # sep는 seperate로 값 사이에 넣을 값을 정할 수 있음
print('Python', 'Java', sep = " vs ", end = "? ") # 끝에 들어갈 내용을 정하고 뒤 출력을 같이 한 줄에 출력
print('무엇이 더 재밌을까요')

import sys
print('Python', 'Java', file = sys.stdout) # 표준 출력으로 출력
print('Python', 'Java', file = sys.stderr) # 표준 에러로 출력

scores = {'수학':0, '영어':50, '코딩':100} # 시험성적
for subject, score in scores.items():
    # print(subject, score) # 정렬 안한 출력
    print(subject.ljust(8), str(score).rjust(4), sep=':') # 문자열을 정렬하는데 내부 숫자 만큼 공간을 확보함 r과 l이 있음

# 은행 대기 순번표 같이 앞을 정형화 되게 숫자 자리수를 정하기
# 001, 002, 003, ...
for num in range(1, 21):
    print('대기번호: ' + str(num).zfill(3))

answer = input('아무 값이나 입력하세요: ') # 입력받는 변수는 무조건 문자형
print('입력하신 값은 ' + answer + '입니다.') # 입력받은 변수가 문자형이므로 숫자를 입력받아도 +로 출력이 됨


## 다양한 출력포멧
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print('{0: >10}'.format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print('{0: >+10}'.format(500))
print('{0: >+10}'.format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print('{0:_<10}'.format(500))
# 3자리 마다 콤마를 찍어주기
print('{0:,}'.format(1000000000000))
# 3자리 마다 콤마를 찍어주고, 부호 구분
print('{0:+,}'.format(1000000000000))
print('{0:+,}'.format(-1000000000000))
# 3자리 마다 콤마를 찍어주고, 부호 구분, 자릿수 확보, 빈자리는 ^로 채워주기
print('{0:^<+30,}'.format(-1000000000000))
# 소수점 출력
print('{0:f}'.format(5/3))
# 소수점을 둘째 자리수 까지만 표시
print('{0:.2f}'.format(5/3))


## 파일 입출력(불러오기, 내보내기)
score_file = open('score.txt', 'w', encoding='utf8') # w는 새파일 쓰기, utf8 한글읽는 형식
print('수학: 0', file = score_file)
print('영어: 50', file = score_file)
score_file.close()

score_file = open('score.txt', 'a', encoding='utf8') # a는 append로 덮어쓰기
score_file.write('과학: 80')
score_file.write('\n코딩: 100') #.write는 띄어쓰기가 안됨
score_file.close()

# 읽어오기 1
score_file = open('score.txt', 'r', encoding='utf8') # r은 읽어오기
print(score_file.read())
score_file.close()

# 읽어오기 2
score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline(), end='')
print(score_file.readline())
score_file.close()

# 읽어오기 3(while이용)
score_file = open('score.txt', 'r', encoding='utf8') # 몇줄일 지 모를 때 반복문으로 한줄 씩 모두 읽기
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end='')
score_file.close()

# 읽어오기 4(for로 한줄씩 가져오는걸 반복, 가장 좋은 방법)
score_file = open('score.txt', 'r', encoding='utf8')
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()


## pickle(사용하는 데이터를 파일 형태로 저장)
import pickle
profile_file = open('profile.pickle', 'wb') # wb 쓰기에 pickle데이터 형태인 바이너리 타입지정
profile = {'이름':'박명수', "나이":30, "취미":['축구', "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # 변수에 있는 정보를 file에 저장
profile_file.close()

profile_file = open('profile.pickle', 'rb') # rb 바이너리 읽어오기
profile = pickle.load(profile_file) # file에 있는 정보를 변수에 불러오기
print(profile)
profile_file.close()


## with(pickle이나 여러 파일을 읽거나 쓰고 닫음)
with open('study.txt', 'w', encoding = 'utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')

with open('study.txt', 'r' encoding='utf8') as study_file:
    print(sudy_file.read())

import pickle
with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))


## 퀴즈 7 파일
for i in range(1,51):
    with open(str(i)+'주차.txt', 'w', encoding='utf8') as tmp_week:
        tmp_week.write('- {0} 주차 주간보고 -'.format(i))
        tmp_week.write('\n부서:')
        tmp_week.write('\n이름:')
        tmp_week.write('\n업무 요약:')


## 클래스(스타크래프트 유닛이 예시)
# 클래스 미사용 시
# 마린: 공격 유닛
name = '마린'
hp = 40
damage = 5
print('{} 유닛이 생성되었습니다.'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp, damage))

# 탱크: 공격 유닛
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{0} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))

def attack(name, location, damage):
    print('{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format( \
        name, location, damage))

attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)

# 같은 종류 유닛을 여럿 생성시 클래스 이용
class Unit: # 일반 유닛 클래스(중요)
    def __init__(self, name, hp, damage): # 클래스서 self는 클래스위치의 변수를 의미하며, 항상 들어가야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)


## 클래스(__init__)(위에서 만든 Unit 클래스 이용)
# __init__은 클래스의 기본 골격 함수이고 __init__으로 정의한 모든 변수를 보내줘야 결과를 내보낸다
# marine1 = Unit('마린')
# marine2 = Unit('마린', 40) # 둘다 변수가 적어서 오류가 난다.


## 클래스(멤버 변수: 밖에서도 한 변수에게만 이용과 추가 가능)(위에서 만든 Unit 클래스 이용)
# self.변수서 변수가 멤버 변수이다.
wraith1 = Unit('레이스', 80, 5) # 스타 레이스 유닛 생성
print('유닛 이름: {0}, 공격력: {1}'.format(wraith1.name, wraith1.damage)) # 클래스 밖에서도 멤버 변수를 쓸 수 있다.

wraith2 = Unit('빼앗은 레이스', 80, 5)
wraith2.clocking = True # 이 변수에게 멤버 변수로 밖에서 내용 추가(전체 클래스가 아니라 이 변수에게만 적용)

if wraith2.clocking == True:
    print('{0}는 현재 클로킹 상태 입니다.'.format(wraith2.name))

if wraith1.clocking == True:
    print('{0}는 현재 클로킹 상태 입니다.'.format(wraith1.name)) # 이 변수에는 해당 멤버 변수가 없어 오류가 난다.


## 클래스(메소드: 클래스에 함수를 넣어 변수에 내장하는 방법)
class AttackUnit: # 공격유닛 클래스(중요)
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location): # attack이란 함수로 클래스로 만든 변수에 내장되어 변수.attack으로 호출한다
        print('{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'\
            .format(self.name, location, self.damage)) # name과 damage는 클래스 내부의 것을 쓰고 location은 외부에서 받아 사용하므로 self.이 앞에 없다.
        
    def damaged(self, damage):
        print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -=damage
        print('{0}: 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0}: 파괴되었습니다.'.format(self.name))

# 파이어뱃: 공격 유닛
firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시') # AttackUnit클래스로 만든 변수에 내장된 attack 함수를 호출

# 공격을 2번 받고 파괴된다고 가정
firebat1.damaged(25) # AttackUnit클래스로 만든 변수에 내장된 damaged 함수를 호출
firebat1.damaged(25)


## 클래스(상속)
# 공격유닛 클래스에 일반유닛 클래스 내용을 상속
class Unit: ## 상속하는 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # Unit에서 self.name과 self.hp 골격을 상속받아 만든 AttackUnit 클래스(자식 클래스)
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit의 __init__함수와 변수 상속을 명시 
        self.damage = damage


## 클래스(다중 상속)
# Unit - AttackUnit - FlyableAttackUnit
# Flyable - FlyableAttackUnit 둘을 상속
class Unit: # 일반 유닛 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # 일반유닛 클래스를 상속받은 공격 유닛 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

class Flyable: # 공중 유닛 클래스
    def __init__(self, flying_speed):
        self.fyling_speed = flying_speed
    
    def fly(self, name, location):
        print('{0}: {1} 방향으로 날아갑니다. [속도 {2}]'\
            .format(name, location, self.fyling_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공격 유닛과 공중 유닛 클래스 둘을 상속받아 합친 공중 공격 유닛 클래스
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리: 공중 공격유닛
valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시')


## 클래스(메소드 오버라이딩: 자식 클래스가 부모 클래스 메소드 함수를 가져와서 덧씌워 사용)
# 자식 클래스에서 매소드 오버라이딩 시 메소드 이름이 겹치면 부모에게 상속받은 메소가 아니라 오버라이딩(수정) 된 매소드가 호출된다.
class Unit: # 일반 유닛 클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0}: {1} 방향으로 이동합니다. [속도 {2}]'\
            .format(self.name, location, self.speed))

class AttackUnit(Unit): # 공격 유닛 클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

class Flyable: # 공중 유닛 클래스
    def __init__(self, flying_speed):
        self.fyling_speed = flying_speed
    
    def fly(self, name, location):
        print('{0}: {1} 방향으로 날아갑니다. [속도 {2}]'\
            .format(name, location, self.fyling_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공중 공격 유닛 클래스
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # Flyable에 공중 speed 내용이 있으므로 지상 speed에는 0을 넣어 준다.
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 부모 클래스에 있는 fly함수 매소드를 자식 클래스에 오버라이딩해서 상속받은 함수 기능에 덧씌움
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

# 벌쳐: 지상 공격 유닛
vulture = AttackUnit('벌쳐', 80, 10, 20)

# 배틀크루져: 공중 공격 유닛
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
# battlecruiser.fly(battlecruiser.name, '9시') # FlyableAttackUnit 자식 클래스에 Flyable 부모 클래스의 메소드를 오버라이딩 하지 않았다면 fly를 계속 사용해 지상유닛 move와 햇갈린다.
battlecruiser.move('9시') # 메소드 오버라이딩으로 fly를 move로 변경하고 메시지 출력도 추가 되었다.


## pass
def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass # 해당 내용을 넘어감

game_start()
game_over()
game_start()


## 클래스(super: 부모 클래스 변수 상속받는 다른 방법, 다중 상속시 사용 불가)
class Unit: # 일반 유닛 클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

class BuildingUnit(Unit): # 건물 유닛 클래스
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) 보통 상속받을 때 초기화
        super().__init__(name, hp, 0) # super로 초기화 시 상속 내용서 self를 초기화 안함
        self.location = location

# 다중 상속 시 super는 맨처음 상속받는 클래스만 상속
class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit, Flyable): # 처음 부모 클래스 Unit 만 상속
    def __init__(self):
        super().__init__()
        # Unit.__init__(self)
        # Flyable.__init__(self)

dropship = FlyableUnit()


## 클래스(isinstance: 여러 변수 중 해당 클래스로 만든 변수를 지정 검색), 클래스 종합 정리(클래스를 이용한 스타크래프트)
# 게임에 필요한 클래스 정의
from random import *

class Unit: # 일반 유닛 클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성되었습니다.'.format(name))

    def move(self, location):
        print('{0}: {1} 방향으로 이동합니다. [속도 {2}]'\
            .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -=damage
        print('{0}: 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0}: 파괴되었습니다.'.format(self.name))

class AttackUnit(Unit): # 공격 유닛 클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print('{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'\
            .format(self.name, location, self.damage))

class Marine(AttackUnit): # 공격 유닛 마린 클래스
    def __init__(self): # 상속 받지만 변수는 지정해 주므로 self만 정의
        AttackUnit.__init__(self, '마린', 40, 1, 5)
    
    def stimpack(self): # 유닛 기능 스팀팩
        if self.hp > 10:
            self.hp -= 10
            print('{0}: 스팀팩을 사용합니다. (HP 10 감소)'.format(self.name))
        else:
            print('{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다.'.format(self.name))

class Tank(AttackUnit): # 공격 유닛 탱크 클래스
    seize_developed = False # 유닛 기능 시즈모드 개발여부(False가 디폴트)

    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35)
        self.seize_mode = False # 밑에서 시즈모드 변수를 써야 하므로 정의
    
    def set_seize_mode(self): # 유닛 기능 시즈모드
        if Tank.seize_developed == False: # 시즈모드 미개발 일때
            return

        if self.seize_mode == False: # 시즈모드가 아닐때
            print('{0}: 시즈모드로 전환합니다.'.format(self.name))
            self.damage *= 2
            self.seize_mode = True
        
        else:
            print('{0}: 시즈모드를 해제합니다.'.format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Flyable: # 공중 유닛 클래스
    def __init__(self, flying_speed):
        self.fyling_speed = flying_speed
    
    def fly(self, name, location):
        print('{0}: {1} 방향으로 날아갑니다. [속도 {2}]'\
            .format(name, location, self.fyling_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공중 공격 유닛 클래스
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit): # 공중 공격 유닛 레이스 클래스
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False # 유닛 기능 클로킹
    
    def clocking(self): # 유닛 기능 클로킹
        if self.clocked == True:
            print('{0}: 클로킹 모드 해제합니다.'.format(self.name))
            self.clocked = False
        else:
            print('{0}: 클로킹 모드 설정합니다.'.format(self.name))
            self.clocked = True

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('Player: gg')
    print('[Player] 님이 게임에서 퇴장하셨습니다.')

# 실제 게임 진행
game_start() # 게임 시작

m1 = Marine() # 마린 3기 생성
m2 = Marine()
m3 = Marine()

t1 = Tank() # 탱크 2기 생성
t2 = Tank()

w1 = Wraith() # 레이스 1기 생성

attack_units = [] # 유닛 일괄 관리(리스트 생성)
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units: # 전 유닛 이동
    unit.move('1시')

Tank.seize_developed = True # 탱크 시즈모드 개발
print('[알림] 탱크 시즈 모드 개발이 완료되었습니다.')

for unit in attack_units: # 공격 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
    if isinstance(unit, Marine): # 여러 변수 중 해당 클래스로 만든 변수를 지정 검색
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units: # 전 유닛 공격
    unit.attack('1시')

for unit in attack_units: # 공격 중 유닛 피해
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)

game_over() # 게임 종료


## 퀴즈8 (클래스)
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
    
houses = []
house1 = House('강남', '아파트', '매매', '10억', '2010년')
house2 = House('마포', '오피스텔', '전세', '5억', '2007년')
house3 = House('송파', '빌라', '월세', '500/50', '2000년')

houses.append(house1)
houses.append(house2)
houses.append(house3)

print('총 {0}대의 매물이 있습니다.'.format(len(houses)))
for house in houses:
    house.show_detail()


## 예외처리(try, except)
try:
    print('나누기 전용 계산기입니다.')
    nums = []
    nums.append(int(input('첫 번째 숫자를 입력하세요: ')))
    nums.append(int(input('두 번째 숫자를 입력하세요: ')))
    nums.append(int(nums[0] / nums[1]))
    print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
except ValueError: # 변수형식 에러가 발생하면 아래 값을 실행한다.
    print('에러! 잘못된 값을 입력하였습니다.')
except ZeroDivisionError as err: # 0으로 나누면 아래 값을 실행
    print(err) # 위 에러 알람을 프린트
except:
    print('알 수 없는 에러가 발생하였습니다.')


## 원하지 않는 상황에서 일부러 에러 발생시키기(try, raise, except)
try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요:'))
    num2 = int(input('두 번째 숫자를 입력하세요:'))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # raise를 이용해서 벨류 에러로 넘긴다.
    print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
except ValueError:
    print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')


## 예외처리(사용자 정의)(class, try, raise, except)
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요:'))
    num2 = int(input('두 번째 숫자를 입력하세요:'))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError('입력값: {0}, {1}'.format(num1, num2))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
    print(err)


## 예외처리(finally: try구문이 잘 작동 하던지 오류로 except로 빠지던지, except로 정의되지 않은 오류로 프로그램이 작동 안하던지 모든 게 끝난 후 작동하는 구문)
class BigNumberError(Exception): # Exception을 상속받아 에러 코드로 만든다.
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요:'))
    num2 = int(input('두 번째 숫자를 입력하세요:'))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError('입력값: {0}, {1}'.format(num1, num2))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
    print(err)
finally:
    print('계산기를 이용해 주셔서 감사합니다.')


## 퀴즈9(예외처리)
class SoldOutError(Exception): # Exception을 상속받아 에러 코드로 만든다.
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print('[남은 치킨: {0}]'.format(chicken))
        order = int(input('치킨 몇 마리 주문하시겠습니까?'))
        if order > chicken:
            print('재료가 부족합니다.')
        elif order <= 0:
            raise ValueError
        else:
            print('[대기번호 {0}] {1} 마리 주문이 완료되었습니다.'.format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력하였습니다.')
    except SoldOutError:
        print('재고가 소진되어 더 이상 주문을 받지 않습니다.')
        break


## 모듈
# 모듈은 같은 워크스페이스에 있어야 사용 가능
import theater_module_ex # 저장된 파일을 모듈로 호출
theater_module_ex.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module_ex.price_morning(4) # 4 명이서 조조 할인 영화 보러 갔을 때
theater_module_ex.price_soldier(5) # 5 명이서 군인 할인 영화 보러 갔을 때

import theater_module_ex as mv # 모듈을 mv 이름으로 호출
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module_ex import * # 모듈을 파일에 적용해 그대로 사용
price(3) # from import로 위치가 필요 없음
price_morning(4)
price_soldier(5)

from theater_module_ex import price, price_morning # 모듈에서 내가 원하는 함수만 호출
price(3)
price_morning(4)
price_soldier(5) # 사용 불가

from theater_module_ex import price_soldier as price # 모듈 내 함수를 price 이름으로 호출
price(5) # 이 price는 price_soldier이다.


## 패키지: 모듈들을 모아둔 폴더
import travel_package_ex.thailand # import에서는 모듈과 패키지명만 들어올 수 있다.
trip_to = travel_package_ex.thailand.ThailandPackage()
trip_to.detail()

# import travel_package_ex.thailand.ThailandPackage # 모듈 내 함수나 클래스를 바로 써서 오류가 난다

from travel_package_ex.thailand import ThailandPackage # from import는 모듈 내 클래스, 함수를 바로 호출 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel_package_ex import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()


## __all__(패키지의 디폴트 모듈 사용 지정)
# 패키지가 디폴트 모듈 지정을 안해두면 'from 패키지 import *'은 어떤 모듈을 가져올 지 모르기 때문에 아무것도 안가져 온다.
# 대신 패키지 내 __init__파일이 __all__ = ['모듈', '모듈', ...]을 지정하면 그 모듈이 호출됨
# travel_package_ex\__init__.py의 내용확인
from travel_package_ex import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

trip_to = vietnam.VietnamPackage() # 이건 패키지가 경로 지정을 안해서 호출이 안됨
trip_to.detail()


## 모듈 직접 실행(__name__을 모듈에 넣어서 확인 가능 'thailand.py'모듈 확인)
from travel_package_ex import *
trip_to = thailand.ThailandPackage()
trip_to.detail()


## 패키지, 모듈 위치 확인(inspect 패키지)
import inspect
import random
from travel_package_ex import *
print(inspect.getfile(random))
print(inspect.getfile(thailand))


## pip install(패키지 설치하기, pypi를 이용해 패키지를 검색)
# Terminal에 pip install '패키지'입력 시 설치
# 설치 후 from '패키지' import '모듈' 로 적용
# Terminal에 pip list입력 시 설치된 패키지 목록 확인
# Terminal에 pip show '패키지'입력 시 패키지 정보 확인
# Terminal에 pip install --upgrade '패키지'입력 시 패키지 업그레이드
# Terminal에 pip uninstall '패키지'입력 시 패키지 삭제


## 내장함수(구글에 'list of python builtins'를 검색해 확인 가능)

# 예시들
# input: 사용자 입력을 받는 함수
language = input('무슨 언어를 좋아하세요?')
print('{0}은 아주 좋은 언어입니다!'.format(language))

# dir: 어떤 객체를 너겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir()) # random 이 추가됨
import pickle
print(dir()) # pickle 이 추가됨

print(dir(random)) # random 안에 있는 변수, 함수

lst = [1, 2, 3]
print(dir(lst)) # lst안에 있는 변수, 함수

name = 'Jim'
print(dir(name))


## 외장함수(import해서 이용, 구글에서 'list of python modules'를 검색해 확인 가능)

# 예시들
# glob: 경로 내의 폴더 / 파일 목록 조회(윈도우에 적용하는 dir())
import glob
print(glob.glob('*.py')) # 확장자가 py인 모든 파일

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현제 디렉토리

folder = 'sample_dir'
if os.path.exists(folder):
    print('이미 존재하는 폴더입니다.')
    os.rmdir(folder) # 폴더 삭제
    print(folder, '폴더를 삭제하였습니다.')
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, '폴더를 생성하였습니다.')

print(os.listdir()) # 현제 디렉토리에 있는 파일

# time: 시간 관련 함수
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S')) # 시간출력 형식 변경

import datetime
print('오늘 날짜는', datetime.date.today())

# timedelta: 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜
td = datetime.timedelta(days = 100) # 100일지정
print('우리가 만난지 100', today + td) # 오늘 + td(100)일 후


## 퀴즈10(모듈, 패키지)(quiz10.py확인)
import quiz10
quiz10.sign()