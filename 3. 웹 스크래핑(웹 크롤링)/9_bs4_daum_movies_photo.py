import requests
from bs4 import BeautifulSoup


## Daum포털 상위 영화 포스터 이미지 다운
for year in range(2015, 2020): # 2015 ~ 2019년
    url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'.format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')

    images = soup.find_all('img', attrs = {'class':'thumb_img'})

    for idx, image in enumerate(images): # 인덱스 순서로
        # print(image['src'])
        image_url = image['src']
        if image_url.startswith('//'): # image_url 원소가 //로 시작한다면 true
            image_url = 'https:' + image_url
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open('movie_{}_{}.jpg'.format(year, idx + 1), 'wb') as f: # 이미지 이름
            f.write(image_res.content)

        if idx >= 4: # 상위 5개 파일만 가져옴
            break
