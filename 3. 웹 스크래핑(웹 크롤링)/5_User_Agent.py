## User Agent: 유저가 사람임을 인식 시키는 코드
## User Agent 가 없으면 웹 사이트에서 침입으로 인색해 차단할 가능성이 있음

# User Agent string을 검색해서 자신의 user agent를 가져옴
import requests
url = 'http://nadocoding.tistory.com'

# user agent를 입력
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}

# requests.get에 url뿐 아니라 user agent를 넣어줘서 실제 검색할 때와 같은 조건으로 웹 스크래핑을 해옴
res = requests.get(url, headers = headers)
res.raise_for_status()

with open('requests_test2.html', 'w', encoding='utf8') as f:
    f.write(res.text)