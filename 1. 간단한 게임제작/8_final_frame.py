import pygame # 게임 제작 패키지


## 최종 프레임(주석은 7번 참고)
################################################ (반드시 초기 설정)
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('New Game')

clock = pygame.time.Clock()
################################################

##### 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)


##### 이벤트 루프(이벤트가 항상 실행되어야 창이 꺼지지 않음)(반드시 필요)
running = True
while running:
    dt = clock.tick(60)

    ##### 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##### 3. 게임 캐릭터 위치 정의

    ##### 4. 충돌 처리

    ##### 5. 화면에 그리기

    pygame.display.update()

pygame.quit()