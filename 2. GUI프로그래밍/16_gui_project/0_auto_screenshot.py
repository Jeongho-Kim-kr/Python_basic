import time
from PIL import ImageGrab # 이미지 관련 패키지

## 합칠 이미지를 얻기 위한 자동 스크린 샷 프로그램
time.sleep(5) # 5초 대기: 사용자가 준비하는 시간

for i in range(1, 11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save('image{}.png'.format(i)) # 파일로 저장 (image1.png ~ image10.png)
    time.sleep(2) # 2초 단위