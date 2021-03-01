from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

listbox = Listbox(root, selectmode='extended', height=0) # 여러 값의 리스트 목록을 제공하는 위젯, selectmode가 single이면 한개만 선택 가능 extended면 여러개 같이 선택 가능, height 크기 만큼 위젯 크기를 지정 0이면 모두 보이는 크기
# listbox = Listbox(root, selectmode='single', height=3)
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박') # 인덱스가 없어도 마지막에 잘 추가
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0) # 맨 앞 항목을 삭제
    # listbox.delete(END) # 맨 뒤에 항목을 삭제

    # 갯수 확인
    # print('리스트에는', listbox.size(), '개가 있어요')

    # 항목 확인(시작 idx, 끝 idx)
    # print('1번째부터 3번쨰까지의 항목: ', listbox.get(0,2))

    # 선택된 항목 확인(인덱스를 반환)
    print('선택된 항목: ', listbox.curselection())
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨