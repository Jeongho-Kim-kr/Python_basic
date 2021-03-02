from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## Radiobutton 선택 시 지정한 value를 반환(객관식 항목 선택 시), 그룹은 반환하는 variable로 묶인다
Label(root, text='메뉴를 선택하세요').pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var) # 라디오 버튼 위젯,
btn_burger2 = Radiobutton(root, text='치즈버거', value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='치킨버거', value=3, variable=burger_var)

btn_burger1.select() # 기본으로 자동 선택 처리

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text='음료를 선택하세요').pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
btn_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=drink_var)

btn_drink1.select() # 기본값

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) # 음료 중 선택된 값을 출력
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨