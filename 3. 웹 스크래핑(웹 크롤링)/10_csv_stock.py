import csv # csv파일을 이용하게 해주는 패키지
import requests
from bs4 import BeautifulSoup


## 네이버금용 코스피 상위종목 csv 저장
url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok='

filename = '시가총액1-200.csv'
f = open(filename, 'w', encoding = 'utf-8-sig', newline= '') # newline=''이면 불필요한 줄바꿈을 안하게 해준다.
writer = csv.writer(f) # csv 파일 만들기

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
# split('\t')으로 인해 탭으로 구분해서 리스트에 넣음
# ['N', '종목명', ...] list형
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    data_rows = soup.find('table', attrs = {'class':'type_2'}).find('tbody').find_all('tr')
    for row in data_rows:
        columns = row.find_all('td')
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data) # 데이터를 writer에 한열씩 넣음