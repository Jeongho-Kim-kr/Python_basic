from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## Checkbutton 체크하는 항목 0, 1의 값을 반환(True, False 기능시)
chkvar = IntVar() # chkvar에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chkvar) # 체크박스 위젯, variable에 값을(0: 체크 해제, 1: 체크) 반환한다.
# chkbox.select() # 기본으로 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack() # 체크박스를 프로그램에 추가함

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일동안 보지 않기', variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 체크 해제, 1: 체크
    print(chkvar2.get())
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨