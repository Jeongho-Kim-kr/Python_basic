import os
from tkinter import * # GUI생성 패키지

root = Tk()
root.title('제목 없음 - Windows 메모장') # 이름
root.geometry('640x480') # 가로 * 세로


## 메모장 만들기
# 메뉴
filename = 'mynote.txt'

def open_file(): # 텍스트 파일 열기 함수
    if os.path.isfile(filename):
        with open('mynote.txt', 'r', encoding='utf8') as file:
            txt.delete('1.0', END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file(): # 텍스트 파일 저장 함수
    with open(filename, 'w', encoding='utf8') as file:
        file.write(txt.get('1.0', END)) # 모든 내용을 가져와서 저장

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기', command=open_file)
menu_file.add_command(label='저장', command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)
menu.add_cascade(labe='파일', menu=menu_file)

menu.add_cascade(labe='편집')
menu.add_cascade(labe='서식')
menu.add_cascade(labe='보기')
menu.add_cascade(labe='도움말')

root.config(menu=menu) # 메뉴 지정


# 스크롤바(텍스트 외에 아무것도 없으므로 root자체를 프레임으로 함)
scrollbar = Scrollbar(root) # 매핑할 스크롤바
scrollbar.pack(side='right', fill='y')


# 본문 텍스트 박스
txt = Text(root,yscrollcommand=scrollbar.set) # 스크롤바 매핑한 텍스트박스
txt.pack(side='left',fill='both', expand=True)
scrollbar.config(command=txt.yview) # 스크롤바 동작


root.mainloop() # 메인 루프가 계속 돌아야 지속됨