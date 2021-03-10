import requests # 웹의 데이터를 html 텍스트로 전부 긁어오는 패키지
from bs4 import BeautifulSoup # html 객체에 접근해 주는 패키지


## Beautifulsoup4 기본 1
## requests에서 받아온 html에서 원하는 데이터를 find하고 추출, 편집(웹스크래핑)

## .find() 조건에 맞는 첫번째 element
## .find_next_sibling 다음 형제 찾기 (siblings로 하면 다음 모든 형제)
## .find_previous_sibling 이전 형제 찾기 (siblings로 하면 이전 모든 형제)
## .find_all() 조건에 맞는 모든 element를 리스트로
## .find_all('', limit=숫자) 리미트를 걸어 찾는 횟수 지정 가능
## .find_all('div', attrs = {'class':['ImZGtf mpg5gc', 'Vpfmgd'], 'id':'dust'}, text = '미세먼지') # find에서 여러 조건을 걸어 만족하는 원소를 찾는다. class조건이 []리스트 인데 이때는 둘중 하나를 만족하면 찾게 된다.

## soup['href'] 해당 속성값을 가져옴
## soup.get_text() 텍스트만 가져옴
## soup.strip() 불필요한 공백 제거

url = 'https://comic.naver.com/webtoon/weekday.nhn' # 네이버 웹툰
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') # 변수 soup은 requests로 res에 저장한 웹의 엘리먼트 모두를 bs4가 이용 가능하게 저장하세 된다.

print(soup.title) # 네이버 웹툰 타이틀
print(soup.title.get_text()) # 네이버 웹툰 타이틀의 텍스트
print(soup.a) # soup 객체에서 처음 발견되는 a element 반환
print(soup.a.attrs) # a element의 속성 정보를 출력
print(soup.a['href']) # a element의 href 속성 '값'정보를 출력

print(soup.find('a', attrs={'class':'Nbtn_upload'}))
print(soup.find(attrs={'class':'Nbtn_upload'})) # 해당 조건을 부여해 검색

print(soup.find('li', attrs={'class':'rank01'})) # 웹툰 rank01을 가져오기

rank1 = soup.find('li', attrs={'class':'rank01'})
print(rank1.a) # 웹툰 rank01에서 a element만 가져오기
print(rank1.a.get_text()) # 랭크01의 텍스트 내용


## Beautifulsoup4 기본 2
# 형제 엘리먼트 가져오기
rank2 = rank1.next_sibling.next_sibling # 변수.next_sibling 다음 형제 엘리먼트 가져오기(여기선 다음 랭킹내용)
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text()) # 랭크03의 텍스트

rank2 = rank3.previous_sibling.previous_sibling # 변수.previous_sibling 이전 형제 엘리먼트 가져오기(여기선 이전 랭킹내용)
print(rank2.a.get_text())

print(rank1.parent) # 변수.parent 부모의 모든 값을 가져오기

rank2 = rank1.find_next_sibling('li') # 변수.find_next_sibling('조건') 다음 조건을 가진 다음 형제 엘리먼트를 가져오기
print(rank2.a.get_text())

rank2 = rank3.find_previous_sibling('li') # 변수.find_previous_sibling('조건') 다음 조건을 가진 이전 형제 엘리먼트를 가져오기
print(rank2.a.get_text())

# 중요
print(rank1.find_next_siblings('li')) # rank1 이후의 다음 조건을 가진 모든 형제 엘리먼트를 가져옴