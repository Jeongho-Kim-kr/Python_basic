import pygame # 게임 제작 패키지


## 게임 배경 이미지 로드
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('New Game') # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load('1 깃허브 업로드/Python_basic/1_간단한 게임제작/background.png')

# 이벤트 루프(이벤트가 항상 실행되어야 창이 꺼지지 않음)(반드시 필요)
running = True # 게임이 진행중인가?
while running:
    # 상태바 나가기 x(quit) 누를 시 running False로 변경해 게임 유지시키는 루프 나가기
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 이벤트가 pygame.QUIT(창이 닫히는 이벤트)이면
            running = False # 위 while 루프가 종료되게 함(pygame이 종료됨)

    # 배경화면, 캐릭터 이미지 불러오기(줄 순서대로 위에 표시됨)
    # screen.fill((0,0,255)) # 배경 RGB설정
    screen.blit(background, (0,0)) # 백그라운드 이미지 불러오기
    
    # 게임 디스플레이 상황 업데이트
    pygame.display.update() # 게임화면을 계속 업데이트 하기(화면 불러올때 필수)

# pygame 종료
pygame.quit()