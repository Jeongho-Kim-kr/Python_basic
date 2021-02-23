from selenium import webdriver # 셀레니움서 웹브라우저를 제어하는 패키지
from selenium.webdriver.common.keys import Keys # 셀레니움에서 키보드 입력 기능을 가져옴 Keys서 K는 대문자


## 셀레니움(브라우저 자동화) 기본
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
