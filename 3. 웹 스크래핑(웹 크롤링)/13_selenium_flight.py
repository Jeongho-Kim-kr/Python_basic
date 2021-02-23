from selenium import webdriver

# 해당 조건이 될때까지 기다리게 만드는데 필요한 패키지들
from selenium.webdriver.support.ui import WebDriverWait # 웹을 기다리게 만드는 함수
from selenium.webdriver.support import expected_conditions as EC # 셀레니움에서 해당 조건이 되면 TRUE가 되는 함수, as EC로 이름이 EC로 지정되어 EC로 불러올 수 있음
from selenium.webdriver.common.by import By # 조건을 명시하기 위해 필요한 함수(By.XPATH, By.ID, By.CLASS_NAME, By.LINK_TEXT 등)


## 네이버 항공권(로딩이 있을 때 해결법)
browser = webdriver.Chrome('./1 깃허브 업로드/python_basic/chromedriver/chromedriver.exe')
browser.maximize_window() # 창 최대화

url ='https://flight.naver.com/flights/'
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text('가는날 선택').click() # 다음 텍스트를 락인하고 클릭

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text('27')[0].click() # [0] 이번달 달력에서 선택
# browser.find_elements_by_link_text('28')[0].click() # [0] 이번달 달력에서 선택

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text('27')[1].click() # [1] 다음달 달력에서 선택
# browser.find_elements_by_link_text('28')[1].click() # [1] 다음달 달력에서 선택

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text('27')[0].click() # [0] 이번달 달력에서 선택
browser.find_elements_by_link_text('28')[1].click() # [1] 다음달 달력에서 선택

# 제주도 선택(xpath를 이용해 지정)
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 항공권 검색이 끝날때 까지 기다리게 만들기
# WebDriverWait(지정 브라우저, 시간): 브라우저를 기다리게함 시간이 지나면 다음 코드를 실행함
# .until(): true이면 기다리지 않고 바로 다음 조건을 실행함
# expected_conditions.presence_of_element_located((By.XPATH, 'xpath')) 모든 곳에서 해당 조건이 있으면 TRUE 여기선 By.XPATH로 다음 xpath가 있는 조건
# 조건은 By.XPATH, By.ID, By.CLASS_NAME, By.LINK_TEXT 등 사용 가능
# 결국 최대 10초를 기다리는데 다음 xpath가 위치하면 기다리는걸 멈추고 다음 코드를 실행
# 보통 조건이 충족 안하면 끝내기 위해 try:목적하는 동작함수 - finally:종료 로 감싼다
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    # 성공했을 시 동작
    print(elem.text) # 첫번쨰 결과 출력
finally:
    browser.quit()