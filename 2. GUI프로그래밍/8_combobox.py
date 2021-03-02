import tkinter.ttk as ttk # 콤보박스가 들어있는 패키지
from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## combobox 선택할 수 있는 목록을 생성함(접혀있음)
values = [str(i) + '일' for i in range(1,32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # height 한번에 보여지는 항목 수
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly') # 메뉴 읽기만 가능하게
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())
    
btn = Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨