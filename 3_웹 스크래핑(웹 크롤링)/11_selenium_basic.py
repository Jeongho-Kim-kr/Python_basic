from selenium import webdriver # 셀레니움서 웹브라우저를 제어하는 패키지
from selenium.webdriver.common.keys import Keys # 셀레니움에서 키보드 입력 기능을 가져옴 Keys서 K는 대문자


## 셀레니움(브라우저 자동화) 기본
## 느리지만 동적 웹 페이지(움직임에 따라 데이터가 변하는 사이트) 스크래핑에 유용
## 웹 페이지를 동작해 원하는 상태로 만든 후 requests가 현재 페이지의 html을 전부를 읽어와서 Beautifulsoup4에 넘긴다.
## 로그인, 원하는 결과에 대한 필터링 등 어떤 동작을 해야 하는 경우 chromedriver.exe를 제어하여 해당 동작을 실행

## .find_element_by_id('') id로 찾기 (elements로 하면 모든 element를 가져온다)
## .find_element_by_class_name('') class name으로 찾기 (elements로 하면 모든 element를 가져온다)
## .find_element_by_link_text('') 링크 text로 찾기 (elements로 하면 모든 element를 가져온다)
## .find_element_by_xpath('') xpath로 찾기 (elements로 하면 모든 element를 가져온다)
## .click() 클릭
## .sent_keys() 글자 입력
## .clear() 글자 지우기

## 페이지가 넘어가는 로딩을 기다리는 기능은 13번 참조

## 스크롤을 내리는 기능은 15번 참조
## selenium with python에서 더 공부 가능

browser = webdriver.Chrome('./1 깃허브 업로드/python_basic/chromedriver/chromedriver.exe')
browser.get('http://naver.com') # 해당 주소로 이동

elem = browser.find_element_by_class_name('link_login') # 해당 클래스(로그인) 선택
elem.click() # 위에서 선택한 원소 클릭

browser.back() # 브라우저 뒤로 이동
browser.forward() # 브라우저 앞으로 이동
browser.back()

elem = browser.find_element_by_id('query') # 해당 클래스(검색창) 선택
elem.send_keys('파이썬') # .send_keys() 다음 글자를 키보드 입력
elem.send_keys(Keys.ENTER) # 엔터

elem = browser.find_elements_by_tag_name('a') # a태그를 모두 가져옴
elem
for e in elem:
    e.get_attribute('href') # a태그를 가져온 elem에서 href를 e에 집어넣음

# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료
