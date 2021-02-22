import requests
from bs4 import BeautifulSoup


## 네이버 웹툰 전체목록 가져오기
url = 'https://comic.naver.com/webtoon/weekday.nhn' # 네이버 웹툰
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('a', attrs={'class':'title'}) # class 속성이 title인 모든 'a' elements를 반환
for cartoon in cartoons:
    print(cartoon.get_text()) # 모든 텍스트를 프린트


## 웹툰 쿠베라 화수 타이틀, 링크 가져오기
url = 'https://comic.naver.com/webtoon/list.nhn?titleId=131385' # 네이버 웹툰
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs={'class': 'title'})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href']
# print(title)
# print('https://comic.naver.com' + link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(title, link)


## 웹툰 쿠베라 평점정보, 평균
total_rates = 0
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    total_rates += float(rate)
print('전체 점수: ', total_rates)
print('평균 점수: ', total_rates / len(cartoons))