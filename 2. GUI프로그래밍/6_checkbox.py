from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로



def btncmd():
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨