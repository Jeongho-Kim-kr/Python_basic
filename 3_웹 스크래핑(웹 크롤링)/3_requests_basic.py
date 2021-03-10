import requests # 웹의 데이터(html)을 전부 긁어오는 패키지


## requests 기본
## 빠르지만 동적 웹 페이지(움직임에 따라 데이터가 변하는 사이트)스크래핑은 불가
## 웹 페이지(html) 전부를 읽어와서 Beautifulsoup4에 넘긴다.
## 주어진 url을 통해 받아온 html에 원하는 정보가 있을 때 좋다. res.raise_for_status()
## 웹에서 거부시(오류에 requests가 뜬다) requests(headers='')에 user agent string검색해 나온 user agent 추가

res = requests.get('http://google.com') # 해당 url의 html을 받아서 res에 저장
res.raise_for_status() # 문제가 생기면 오류를 내는 가장 많이 사용하는 오류확인 코드 위 코드랑 쌍으로 씀

## 오류확인 방법
# 1 print('응답코드 :', res.status_code) # 200 이면 정상

# 2 if res.status_code == requests.codes.ok:
#       print('정상입니다')
#   else:
#       print('문제가 생겼습니다. [에러코드 ', res.satus_code, ']') 

print(len(res.text)) ## 페이지 내 스크롤한 텍스트 길이
print(res.text)

with open('requests_test1.html', 'w', encoding='utf8') as f:
    f.write(res.text)