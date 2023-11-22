from background import draw_background
import pygame
import sys
from game_parameters import *
import math
import random
from shooting import Shot
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
running=True
background =screen.copy()
draw_background(background)
#add pygame clock
clock = pygame.time.Clock()
#set turn
turn=1
#percent
percent_font=pygame.font.Font('sprites_final/Black_Crayon.ttf', 25)
angle_font=pygame.font.Font('sprites_final/Black_Crayon.ttf', 25)
#draw ball
#ball = Shot(80,430)
#draw screen
#screen.blit(background, (0, 0))
#pygame.display.flip()
ball = Shot(ball_x, ball_y, percentm, anglem)
angle1=0
angle2=0
percent1=0
percent2=0
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if percent2<100:
                    percent2=percent2+1
            if event.key == pygame.K_LEFT:
                if percent2>0:
                    percent2=percent2-1
            if event.key == pygame.K_d:
                if percent1<100:
                    percent1=percent1+1
            if event.key == pygame.K_a:
                if percent1>0:
                    percent1=percent1-1
            #angle
            if event.key == pygame.K_UP:
                if angle2<100:
                    angle2=angle2+1
            if event.key == pygame.K_DOWN:
                if angle2>0:
                    angle2=angle2-1
            if event.key == pygame.K_w:
                if angle1<100:
                    angle1=angle1+1
            if event.key == pygame.K_s:
                if angle1>0:
                    angle1=angle1-1
            if event.key==pygame.K_SPACE:
                if turn%2==0:
                    ball.x=675
                    ball.y=425
                    ball.percent=percent2*-1
                    ball.angle=angle2*math.pi/180
                    turn=turn+1
                    print (turn)
                else:
                    ball.x = 100
                    ball.y = 425
                    ball.angle=angle1*math.pi/180
                    ball.percent=percent1
                    turn=turn+1
                    print (turn )


        #print (event)
    # draw screen
    screen.blit(background, (0, 0))
    #draw ball
    #ball = Shot(ball_x, ball_y)
    ball.update()
    ball.draw(screen)
    #draw percent
    percent_text1 = percent_font.render(f"Percent: {str(percent1)}", True, (0, 50, 182))
    percent_text2 = percent_font.render(f"Percent: {str(percent2)}", True, (0, 50, 182))
    screen.blit(percent_text1, (40, 525))
    screen.blit(percent_text2, (650, 525))
    #draw angle
    angle_text1 = angle_font.render(f"Angle: {str(angle1)}", True, (0, 50, 182))
    angle_text2 = angle_font.render(f"Angle: {str(angle2)}", True, (0, 50, 182))
    screen.blit(angle_text1, (40, 545))
    screen.blit(angle_text2, (650, 545))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
