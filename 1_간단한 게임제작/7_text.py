import pygame # 게임 제작 패키지


## 게임 내 텍스트 추가
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('New Game') # 게임 이름

# FPS
clock = pygame.time.Clock() # 초당 프레임 설정

# 배경 이미지 불러오기
background = pygame.image.load('1 깃허브 업로드/Python_basic/1_간단한 게임제작/background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('1 깃허브 업로드/Python_basic/1_간단한 게임제작/character.png')
character_size = character.get_rect().size # 이미지의 크기를 구함
character_width = character_size[0] # [0]이미지의 가로 크기
character_height = character_size[1] # [1]이미지의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 생성되는 x포지션, 화면 가로의 절반 크기에 해당하는 곳에 위치(좌표 위치는 이미지의 가장 왼쪽 위가 된다)
character_y_pos = screen_height - character_height # 생성되는 y 포지션, 화면 세로 크기 가장 아래에 위치(좌표 위치는 이미지의 가장 왼쪽 위가 된다)

# 이동할 좌표변수
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# 적 enemy 캐릭터
enemy = pygame.image.load('1 깃허브 업로드/Python_basic/1_간단한 게임제작/enemy.png')
enemy_size = enemy.get_rect().size # 이미지의 크기를 구함
enemy_width = enemy_size[0] # [0]이미지의 가로 크기
enemy_height = enemy_size[1] # [1]이미지의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 생성되는 x포지션, 화면 가로의 절반 크기에 해당하는 곳에 위치(좌표 위치는 이미지의 가장 왼쪽 위가 된다)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 생성되는 y 포지션, 화면 세로 크기 가장 아래에 위치(좌표 위치는 이미지의 가장 왼쪽 위가 된다)

# 게임 내 타이머 텍스트, 변수 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)
total_time = 10 # 게임 총 시간
start_ticks = pygame.time.get_ticks() # 시작 시각 정보를(tick, ms단위) 받아옴

# 이벤트 루프(이벤트가 항상 실행되어야 창이 꺼지지 않음)(반드시 필요)
running = True # 게임이 진행중인가?
while running:
    # 초당 프레임수
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    # print('fps: ' +str(clock.get_fps())) # 초당 프레임 수 확인

    # 상태바 나가기 x(quit) 누를 시 running False로 변경해 게임 유지시키는 루프 나가기
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 이벤트가 pygame.QUIT(창이 닫히는 이벤트)이면
            running = False # 위 while 루프가 종료되게 함(pygame이 종료됨)

        # 캐릭터 키보드 이동기능
        if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 땠는지 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # 방향키로 이동한 x좌표, 프레임을 곱해 이동 속도, 위치값을 보정
    character_y_pos += to_y * dt # 방향키로 이동한 x좌표, 프레임을 곱해 이동 속도, 위치값을 보정

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect() # 캐릭터의 초기 위치 좌표 가져오기
    character_rect.left = character_x_pos # 캐릭터의 좌측 현재 좌표 업데이트
    character_rect.top = character_y_pos # 캐릭터의 위 현재 좌표 업데이트

    enemy_rect = enemy.get_rect() # 적의 초기 위치 좌표를 가져오기
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크(충돌시 게임 오버)
    if character_rect.colliderect(enemy_rect): # 적 위치와 캐릭터 위치가 겹쳤는가?
        print('충돌했어요')
        running = False # 충돌 했으니 게임을 오버를 위해 게임 동작 루프 탈출

    # 배경화면, 캐릭터 이미지 불러오기(줄 순서대로 위에 표시됨)
    # screen.fill((0,0,255)) # 배경 RGB설정
    screen.blit(background, (0,0)) # 백그라운드 이미지 불러오기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 이미지 불러오기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 이미지 불러오기

    # 게임 내 타이머 텍스트 넣기, 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 현제 시각 정보 - 시작 시각 정보 / 1000, 경과시간(ms)을 1000으로 나눠서 초(s)단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 시간, True, 글자 색상
    screen.blit(timer, (10,10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print('타임아웃')
        running = False

    # 게임 디스플레이 상황 업데이트
    pygame.display.update() # 게임화면을 계속 업데이트 하기(화면 불러올때 필수)

# 잠시 대기
pygame.time.delay(2000) # 2초 대기

# pygame 종료
pygame.quit()