import pygame
import random
from PyQt5.QtWidgets import * 

#######################################################
pygame.init()   #게임초기화
#######################################################

#화면크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면타이틀
pygame.display.set_caption("게임")

clock = pygame.time.Clock()
########################################################

#배경만들기
background = pygame.image.load("background.png")

#캐릭터
character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 30
to_y = 0

#똥
ddong = pygame.image.load("enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width-ddong_width)
ddong_y_pos = 0
ddong_speed = 10

ddong2 = pygame.image.load("enemy.png")
ddong2_size = ddong2.get_rect().size
ddong2_width = ddong2_size[0]
ddong2_height = ddong2_size[1]
ddong2_x_pos = random.randint(0, screen_width-ddong_width)
ddong2_y_pos = 0
ddong2_speed = 20

ddong3 = pygame.image.load("enemy.png")
ddong3_size = ddong3.get_rect().size
ddong3_width = ddong3_size[0]
ddong3_height = ddong3_size[1]
ddong3_x_pos = random.randint(0, screen_width-ddong_width)
ddong3_y_pos = 0
ddong3_speed = 40

score = 0

#이벤트루프
running = True
while running:
    dt = clock.tick(30) #초당 프레임
    #print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get(): #이벤트 종류 체크
        if event.type == pygame.QUIT: #창이 닫히는 이벤트
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 캐릭터 위치 정의
    character_x_pos += to_x

    #똥 떨어졌을 때
    if ddong_y_pos > screen_height:
        score += 1
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width-ddong_width)

    #똥2 떨어졌을 때
    if ddong2_y_pos > screen_height:
        score += 1
        ddong2_y_pos = 0
        ddong2_x_pos = random.randint(0, screen_width-ddong2_width)

    #똥3  떨어졌을 때
    if ddong3_y_pos > screen_height:
        score += 1
        ddong3_y_pos = 0
        ddong3_x_pos = random.randint(0, screen_width-ddong3_width)

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed
    ddong2_y_pos += ddong2_speed
    ddong3_y_pos += ddong3_speed

    #충돌
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    ddong2_rect = ddong2.get_rect()
    ddong2_rect.left = ddong2_x_pos
    ddong2_rect.top = ddong2_y_pos

    ddong3_rect = ddong3.get_rect()
    ddong3_rect.left = ddong3_x_pos
    ddong3_rect.top = ddong3_y_pos

    if character_rect.colliderect(ddong_rect):
        print("으악! 똥 맞았다")
        print("피한 똥 개수 : " , score)
        running = False
        
    elif character_rect.colliderect(ddong2_rect):
        print("으악! 똥 맞았다")
        print("피한 똥 개수 : " , score)
        running = False
        
    elif character_rect.colliderect(ddong3_rect):
        print("으악! 똥 맞았다")
        print("피한 똥 개수 : " , score)
        running = False

    #화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(ddong, (ddong_x_pos,ddong_y_pos))
    screen.blit(ddong2, (ddong2_x_pos,ddong2_y_pos))
    screen.blit(ddong3, (ddong3_x_pos,ddong3_y_pos))

    pygame.display.update() #게임화면 계속 새로고침


def alert(self):
    QMessageBox.about(self,"Game Over",score)

#pygame.time.delay(2000) # 종료 전 2초 대기
pygame.quit()