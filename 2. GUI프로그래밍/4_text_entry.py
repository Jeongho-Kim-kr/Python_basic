from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

txt = Text(root, width=30, height=5) # 텍스트를 넣을 수 있는 위젯
txt.pack() # 텍스트를 프로그램에 추가함
txt.insert(END, '글자를 입력하세요') # '글자를 입력하세요' 글자를 텍스트 위젯에 추가함

e = Entry(root, width=30) # 한줄짜리 텍스트를 넣을 수 있는 위젯
e.pack() # 엔트리를 프로그램에 추가함
e.insert(0, '한 줄만 입력 가능해요') # 현재는 값이 비어 있으므로 END를 써도 동일하다

def btncmd():
    # 내용 출력
    print(txt.get('1.0', END)) # txt.get은 txt에 정의된 텍스트 위젯에서 ('1.0', END 즉 1행 0열에서 끝까지 전부)범위의 텍스트를 가져온다
    print(e.get()) # 엔트리의 텍스트를 가져옴

    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨