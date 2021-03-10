import requests
from bs4 import BeautifulSoup


## 구글무비 크롤링(서버에 원하는 국적 언어 사이트)
url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    'Accept-Language':'ko-KR,ko'
    } # 'Accept-Language':'ko-KR,ko' 한국어로 된 페이지를 요청


res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs = {'class':'ImZGtf mpg5gc'})
print(len(movies))

# with open('movie.html', 'w', encoding= 'utf8')as f: # 가져온 소스 html로 저장
#     # f.write(res,text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find('div', attrs = {'class':'WsMG1c nnK0zc'}).get_text()
    print(title)