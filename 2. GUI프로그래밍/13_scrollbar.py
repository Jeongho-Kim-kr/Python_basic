from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## Scrollbar 스크롤 바
frame = Frame(root) # 프레임 정의(스크롤이 동작할 프레임을 지정한다)
frame.pack()

scrollbar = Scrollbar(frame) # 스크롤바를 listbox와 같은 프레임에 정의
scrollbar.pack(side='right', fill='y') # 오른쪽에 y축을 채워서 스크롤바 생성

# 스크롤 y와 listbox y축 동기화
# yscrollcommand 스크롤을 listbox에 매핑
# scrollbar.config(command=listbox.yview) 스크롤에 listbox를 매핑
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand = scrollbar.set)
for i in range(1, 32): # 1 ~ 31일
    listbox.insert(END, str(i) + '일') # 1일, 2일, ...
listbox.pack(side='left') # 왼쪽에 listbox생성

scrollbar.config(command=listbox.yview) # 리스트 박스 상하 움직임을 스크롤에 매핑

root.mainloop() # 메인 루프가 계속 돌아야 지속됨