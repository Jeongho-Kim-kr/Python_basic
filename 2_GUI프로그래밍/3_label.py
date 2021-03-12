from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## Label 프로그램에 텍스트, 사진 등을 추가
label1 = Label(root, text='안녕하세요') # 레이블(들어가는 그래픽 이경우 text)
label1.pack() # 레이블을 프로그램에 추가함

photo = PhotoImage(file='1 깃허브 업로드/Python_basic/2_GUI프로그래밍/img.png')
label2 = Label(root, image=photo) # 이미지 추가
label2.pack()

def change():
    label1.config(text='또 만나요') # 레이블 내 내용 수정

    global photo2 # 전 프로그램에서 쓰기 위해 전역변수 선언
    photo2 = PhotoImage(file='1 깃허브 업로드/Python_basic/2_GUI프로그래밍/img2.png')
    label2.config(image=photo2)
btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨