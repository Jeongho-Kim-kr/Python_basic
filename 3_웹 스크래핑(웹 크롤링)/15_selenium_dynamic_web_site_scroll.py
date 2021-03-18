from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup


## 구글무비(동적 사이트: 동작을 해야 다음 정보가 생성되는 사이트) 셀레니움으로 동작 후 그 페이지(lxml) 받아서 크롤링
## 크롬화면을 띄우지 않고 동작시키는 headless 기능은 16번 참조(처음 시험 동작은 15번으로 하고 반복 동작 시 16번으로 빠르게 실시)
browser = webdriver.Chrome(r'C:\Users\KJH\OneDrive - 인하대학교\0 정리\1 깃허브 업로드\chromedriver\chromedriver.exe')
browser.maximize_window()

## 스크롤 파트
url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
browser.get(url)

# 스크롤 내리기 가장 아래로 내리기 위해 반복 수행
# browser.execute_script('window.scrollTo(0, 1080)') # 1920 * 1080시 한 페이지 스크롤

# 최초 높이 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    # 페이지 가장 아래로 스크롤
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    # 2초에 로딩
    time.sleep(2)
    
    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight') # 현재 문서 높이를 가져와서 저장

    # 더이상 안내려 가서 현재높이와 이전높이가 같으면 종료
    if curr_height == prev_height:
        break
    
    # 현재 높이를 이전 높이에 저장
    prev_height = curr_height

print('스크롤 완료')



## 할인된 영화 정보 출력 파트
# 스크롤을 밑에까지 내린 현재 페이지 소스를 soup에 받아오기
soup = BeautifulSoup(browser.page_source, 'lxml')

# movies = soup.find_all('div', attrs = {'class':['ImZGtf mpg5gc', 'Vpfmgd']}) # 클래스를 찾을 때 리스트로 여러개 쓰면 두 조건 중 하나에 해당하는 내용을 가져옴
movies = soup.find_all('div', attrs = {'class':'Vpfmgd'})

print(len(movies)) # 순위에서 받아온 영화 수

for movie in movies:
    title = movie.find('div', attrs = {'class':'WsMG1c nnK0zc'}).get_text()
    # print(title) # 전체 영화 제목 출력

    # 할인 전 가격
    original_price = movie.find('span', attrs = {'class':'SUZt4c djCuy'})
    if original_price:
        original_price = original_price.get_text()
        # 오리지널 가격이(영화 할인중이어서) 있는 경우
    else:
        # print(title, '<할인되지 않은 영화 제외>')
        continue
        # 영화가 할인하지 않는 경우
    
    # 할인 된 가격
    discount_price = movie.find('span', attrs = {'class':'VfPpfd ZdBevf i5DZme'}).get_text()

    # 링크
    link = movie.find('a', attrs = {'class':'JC71ub'})['href']
    # 올바른 링크: https://play.google.com + link
    
    print(f'제목: {title}')
    print(f'할인 전 금액: {original_price}')
    print(f'할인 후 금액: {discount_price}')
    print('링크: ','https://play.google.com' + link)
    print('-'*100)

browser.quit()