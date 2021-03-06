import time
import keyboard # 키보드를 눌를 시 원하는 동작을 지정하는 패키지
from PIL import ImageGrab

## 키보드를 누를 시 스크린샷 프로그램
def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save('image{}.png'.format(curr_time)) # image_20200601_102030.png

keyboard.add_hotkey('F9', screenshot) # 어떤 키를 누를 때 어떤 동작을 실행할 지 지정
# keyboard.add_hotkey('a', screenshot)
# keyboard.add_hotkey('ctrl+shift+s', screenshot)

keyboard.wait('esc') # 사용자가 esc를 누를 떄까지 프로그램 수행