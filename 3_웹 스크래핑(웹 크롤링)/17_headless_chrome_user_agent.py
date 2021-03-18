from selenium import webdriver


## headless chrome모드로 동작할 때 user agent는 headlesschrome을 포함하게 되고 서버선 이걸 막을 수 있다.
## 그렇기 떄문에 아래 useragent 옵션을 추가해야 한다.
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36') # user-agent에 headless크롬이 남지 않게 직접 지정해주는 옵션

browser = webdriver.Chrome(r'C:\Users\KJH\OneDrive - 인하대학교\0 정리\1 깃허브 업로드\chromedriver\chromedriver.exe', options=options) # 위에서 저장한 heawdless 옵션이 들어감
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
browser.quit()

# 보통 useragent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36
# 실행 결과 HeadlessChrome이 추가된 useragent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/88.0.4324.182 Safari/537.36