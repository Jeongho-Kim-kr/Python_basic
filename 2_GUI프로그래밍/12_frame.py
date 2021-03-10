from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## Frame 틀, LabelFrame 제목이 있는 틀, pack으로 위치 지정
Label(root, text='메뉴를 선택해 주세요').pack(side='top') # 상측에 레이블 위치
Button(root, text='주문하기').pack(side='bottom') # 하측에 버튼 위치

# 메뉴 프레임
frame_burger = Frame(root, relief='solid', bd=1) # relief 태두리모양, bd 태두리 두께
frame_burger.pack(side='left', fill='both', expand=True) # 왼쪽에 상하(fill), 좌우(expand) 채워서 배치

Button(frame_burger, text='햄버거').pack() # 이 버튼은 frame_burger 안에 넣는다
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

# 음료 프레임
frame_drink = LabelFrame(root, text='음료') # 제목이 있는 테두리
frame_drink.pack(side='right', fill='both', expand=True) # 오른쪽에 상하(fill), 좌우(expand) 채워서 배치

Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨