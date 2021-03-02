import tkinter.messagebox as msgbox # 메시지 박스 패키지
from tkinter import * # GUI생성 패키지

root = Tk()
root.title('New GUI') # 이름
root.geometry('640x480') # 가로 * 세로

## messagebox. 팝업으로 텍스트를 띄우기
# 기차 예매 시스템
def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다.') # 알림 팝업 생성

def warn():
    msgbox.showwarning('경고', '해당 좌석은 매진되었습니다.') # 경고 팝업 생성

def error():
    msgbox.showerror('에러', '결제 오류가 발생했습니다.') # 에러 팝업 생성

def okcancel():
    msgbox.askokcancel('확인 / 취소', '해당 좌석은 유아동반석입니다. 예매하시겠습니까?') # 사용자에게 확인, 취소 두 버튼으로 이후 진행 여부를 물어보는 팝업 생성

def retrycancel():
    response = msgbox.askretrycancel('재시도 / 취소', '일시적인 오류입니다. 다시 시도하겠습니까?') # 사용자에게 재시도, 취소 두 버튼으로 재시도를 물어보는 팝업 생성
    if response == 1: # 재시도
        print('예')
    elif response == 0: # 취소
        print('아니요')

def yesno():
    msgbox.askyesno('예 / 아니요', '해당 좌석은 역방향입니다. 예매하시겠습니까?') # 사용자에게 예, 아니요 두 버튼으로 맞는지 물어보는 팝업 생성

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message='예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?') # 사용자에게 예, 아니요, 취소 세 버튼으로 이게 맞는지, 아니면 진행 하는지를 물어보는 팝업 생성
    # 네: 저장 후 종료
    # 아니요: 저장 하지 않고 종료
    # 취소: 프로그램 종료 취소(현재 화면에서 계속 작업)
    print('응답: ',response) # True, False, None -> 예 1, 아니요 0, 그외 None (1, 0, None 순서로 값을 부여한다)
    if response == 1: # 네
        print('예')
    elif response == 0: # 아니요
        print('아니요')
    else:
        print('취소')

Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()

Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니요').pack()
Button(root, command=yesnocancel, text='예 아니요 취소').pack()

root.mainloop() # 메인 루프가 계속 돌아야 지속됨