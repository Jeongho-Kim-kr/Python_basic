from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup


## 15번 코드에서 셀레니움을 크롬을 띄우지 않고 백그라운드에서 동작(화면이 나오지 않아 더 동작이 빠름)
## headless로 동작을 확인하기 힘드므로 원하는 지점에 browser.get_screenshot_as_file('google_movie.png')코드 추가시 해당 지점에서 스크린 샷을 저장 가능
## browser.quit()로 동작을 꺼줘야 한다.
# 백그라운드에서 크롬 실행 옵션을 options변수에 저장 아래 webdriver.Chrome()에 options=에 추가해주면 동작
options = webdriver.ChromeOptions() # 크롬 옵션기능을 options로
options.headless = True # webdriver.ChromeOptions.headless = True (크롬 백그라운드)
options.add_argument('window-size=1920x1080') # 백그라운드서 동작하는 브라우저 크기를 지정
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36') # user-agent에 headless크롬이 남지 않게 직접 지정해주는 옵션

browser = webdriver.Chrome(r'C:\Users\KJH\OneDrive - 인하대학교\0 정리\1 깃허브 업로드\chromedriver\chromedriver.exe', options=options) # 위에서 저장한 heawdless 옵션이 들어감
browser.maximize_window()

url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
browser.get(url)

## 스크롤 파트
# 스크롤 내리기 가장 아래로 내리기 위해 반복 수행
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
browser.get_screenshot_as_file('google_movie.png') # headless로 안보이므로 동작하는 스크린 샷을 저장해서 확인



## 할인된 영화 정보 출력 파트
# 스크롤을 밑에까지 내린 현재 페이지 소스를 soup에 받아오기
soup = BeautifulSoup(browser.page_source, 'lxml')

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