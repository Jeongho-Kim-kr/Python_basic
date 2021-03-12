from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름

## Button 누를 수 있는 버튼(누를 시 동작하는 함수를 지정 가능)
btn1 = Button(root, text = '버튼1') # 버튼을 정의, root아래 기능이므로 root를 명시한다.
btn1.pack() # 버튼을 프로그램에 추가함(모든 위젯은 .pack으로 집어 넣어야 한다)

btn2 = Button(root, padx=5, pady=10, text='버튼2222222222') # padx, pady는 버튼 내에 여백을 확보(유동크기, 넘어가면 버튼 크기가 커짐)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4444444444') # width, height는 버튼 크기 자체를 설정(고정크기, 넘어가면 글자가 짤림)
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow', text='버튼=5') # fg 폰트색, bg 버튼색
btn5.pack()

photo = PhotoImage(file='1 깃허브 업로드/Python_basic/2_GUI프로그래밍/img.png') # PhotoImage 사진 파일 불러오기
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print('버튼이 클릭되었어요')
btn7 = Button(root, text='동작하는 버튼', command=btncmd) # command 버튼이 클릭될 때 동작할 함수
btn7.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨