import time
import tkinter.ttk as ttk # 프로그레스 바가 들어있는 패키지
from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## progressbar 진행되는 상황을 보여주는 바
# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # mode='indeterminate' 언제 끝나는지 안정할 떄
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate') # mode='determinate' 끝나는 경우를 지정
# progressbar.start(10) # 진행바가 진행되서 10ms 마다 시작하게 설정
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지
    
# btn = Button(root, text='클릭', command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # 동작 때 마다 gui를 보이게 업데이트
        print(p_var2.get())
    
btn = Button(root, text='시작', command=btncmd2)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨