import pygame, os
import random  

#######################################################
pygame.init()   #게임초기화
#######################################################

#화면크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

#화면타이틀
pygame.display.set_caption("팡게임")

clock = pygame.time.Clock()
########################################################

current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path,'images')

#배경만들기
background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이 위에 캐릭터 두려고 씀

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동방향
character_to_x = 0

#캐릭터 이동속도
character_speed = 5

#무기만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한번에 여러발 발사 가능
weapons = []

weapon_speed = 10


#이벤트루프
running = True
while running:
    dt = clock.tick(30) #초당 프레임
    #print("fps: " + str(clock.get_fps()))
    
    #이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #이벤트 종류 체크
        if event.type == pygame.QUIT: #창이 닫히는 이벤트
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #캐릭터 왼쪽
                character_to_x -= character_speed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #캐릭터 왼쪽
                    character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width/2)
                weapon_y_pos = character_y_pos 
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                character_to_x = 0

    # 캐릭터 위치 정의
    character_x_pos += character_to_x
    
    if character_x_pos < 0:
        character_x_pos = 0  
    elif character_x_pos > screen_width - character_width :
        character_x_pos =  screen_width - character_width
    
    #무기위치
    weapons = [[w[0],w[1]-weapon_speed] for w in weapons] #무기 위치를 위로 올림
    
    
    #4. 충돌처리
  

    #5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(stage,(0,screen_height-stage_height))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos, weapon_y_pos))

    pygame.display.update() #게임화면 계속 새로고침
 
#pygame.time.delay(2000) # 종료 전 2초 대기
pygame.quit()





