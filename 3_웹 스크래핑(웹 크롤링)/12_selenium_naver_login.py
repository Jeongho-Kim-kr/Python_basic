from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # 시간과 관련한 동작 패키지(time.sleep())


## 네이버 로그인(셀레니움 기본 응용)
browser = webdriver.Chrome(r'C:\Users\KJH\OneDrive - 인하대학교\0 정리\1 깃허브 업로드\chromedriver\chromedriver.exe')

# 1. 네이버 이동
browser.get('http://naver.com') # 해당 주소로 이동

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login') # 해당 클래스(로그인) 선택
elem.click() # 위에서 선택한 원소 클릭

# 3. id, pw 입력
browser.find_element_by_id('id').send_keys('naver_id')
browser.find_element_by_id('pw').send_keys('naver_pw')

# 4. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

# 5. id를 새로 입력
time.sleep(2)
browser.find_element_by_id('id').clear() # 로그인창에 전 내용 지우기
browser.find_element_by_id('id').send_keys('my_id')

# 6. html 정보 출력(페이지 소스 전부)
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료