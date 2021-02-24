import requests
from bs4 import BeautifulSoup


## 날씨, 헤드라인 뉴스, it 뉴스, 오늘의 영어회화 스크래핑
def create_soup(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def scrape_weather():
    print('[오늘의 날씨]')
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
    soup = create_soup(url)

    # 구름많음, 어제보다 00˚ 높아요
    cast = soup.find('p', attrs = {'class':'cast_txt'}).get_text()
    # 현재 00˚C (최저 00˚ / 최고 00˚)
    curr_temp = soup.find('p', attrs = {'class':'info_temperature'}).get_text().replace('도씨', '') # 현재 온도
    min_temp = soup.find('span', attrs={'class':'min'}).get_text() # 최저 온도
    max_temp = soup.find('span', attrs={'class':'max'}).get_text() # 최고 온도
    # 오전 강수확률 00% / 오후 강수확률 00%
    morning_rain_rate = soup.find('span', attrs={'class':'point_time morning'}).get_text().strip() # 오전 강수확률
    afternoon_rain_rate = soup.find('span', attrs={'class':'point_time afternoon'}).get_text().strip() # 오후 강수확률
    # 미세먼지 00㎍/㎥보통
    # 초미세먼지 00㎍/㎥보통
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm10 = dust.find_all('dd')[0].get_text() # 미세먼지
    pm25 = dust.find_all('dd')[1].get_text() # 초미세먼지

    # 출력
    print(cast)
    print('현재 {} (최저 {} / 최고 {})'.format(curr_temp, min_temp, max_temp))
    print('오전 {} / 오후 {}'.format(morning_rain_rate, afternoon_rain_rate))
    print()
    print('미세먼지 {}'.format(pm10))
    print('초미세먼지 {}'.format(pm25))
    print()


def scrape_headline_news():
    print('[해드라인 뉴스]')
    url = 'https://news.naver.com'
    soup = create_soup(url)
    
    news_list = soup.find('ul', attrs={'class':'hdline_article_list'}).find_all('li', limit=3)
    for index, news in enumerate(news_list):
        title = news.find('a').get_text().strip()
        link = url + news.find('a')['href']
        print('{}. {}'.format(index+1, title))
        print('  (링크): {}'.format(link))
    print()


if __name__ == '__main__':
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 해드라인 뉴스 정보 가져오기