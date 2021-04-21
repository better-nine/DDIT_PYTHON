import pygame 
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