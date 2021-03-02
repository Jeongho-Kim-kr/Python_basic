from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## Menu 상단 메뉴바(버튼, radio버튼, 체크박스를 메뉴바에 추가 가능, 버튼을 누를 시 함수로 연결)
def create_new_file():
    print('새 파일을 만듭니다.')

menu = Menu(root) # 상단 메뉴바 정의(root아래 기능)

# File 메뉴
menu_file = Menu(menu, tearoff=0) # 상단 메뉴바 menu에서 선택할 수 있는 menu_file을 추가(root 아래 menu 아래 기능)
menu_file.add_command(label='New File', command=create_new_file) # menu_file에 기능목록 추가(가능은 command함수)
menu_file.add_command(label='New Window')
menu_file.add_separator() # 메뉴 아래 구분선
menu_file.add_command(label='Open File...')
menu_file.add_separator()
menu_file.add_command(label='Save All', state='disable') # state='disable' 해당 기능목록을 추가는 하지만 비활성화
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.quit) # command=root.quit root를 종료함
menu.add_cascade(labe='File', menu=menu_file) # 위에서 만든 menu_file과 그 아래 기능목록을 상단 menu에 추가

# Edit메뉴(빈 값)
menu.add_cascade(label='Edit')

# Language 메뉴 추가(radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='Java')
menu_lang.add_radiobutton(label='C++')
menu.add_cascade(label='Language', menu=menu_lang)

# View 메뉴(check 버튼)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu.add_cascade(label='View', menu=menu_view)


root.config(menu=menu) # 상단 메뉴바를 menu로 선언


root.mainloop() # 메인 루프가 계속 돌아야 지속됨