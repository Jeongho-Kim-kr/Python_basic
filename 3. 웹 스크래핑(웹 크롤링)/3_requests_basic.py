import requests # 웹의 데이터를 html 텍스트로 전부 긁어오는 패키지

res = requests.get('http://google.com')
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