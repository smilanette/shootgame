from background import draw_background
import pygame
import sys
from game_parameters import *
import math
import random
from shooting import Shot
import time
from drawcannon1 import Cannonleft
from drawcannon2 import Cannonright
from drawingtower import Tower
from blockades import Blockades, blockades
from powerup import Powerup, health

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
running=True
background =screen.copy()
draw_background(background)
#balls
blueball = pygame.image.load("sprites_final/kenney_rolling-ball-assets/PNG/Default/ball_blue_small.png").convert()
blueball.set_colorkey((0, 0, 0))
redball = pygame.image.load("sprites_final/kenney_rolling-ball-assets/PNG/Default/ball_red_small.png").convert()
redball.set_colorkey((0, 0, 0))
stars=pygame.image.load("sprites_final/kenney_rolling-ball-assets/PNG/Default/star.png").convert()




#add pygame clock
clock = pygame.time.Clock()
#sounds
oofsound=pygame.mixer.Sound('sprites_final/hurt.wav')
#set turn
turn=1
#percent
percent_font=pygame.font.Font('sprites_final/Black_Crayon.ttf', 25)
angle_font=pygame.font.Font('sprites_final/Black_Crayon.ttf', 25)
#pre reqs
ball = Shot(ball_x, ball_y, percentm, anglem, startm)
cannon1 = Cannonleft(70, screen_height - tile_size - 25)
cannon2 = Cannonright(730, screen_height - tile_size-15)
tower=Tower(400,385)
angle1=20
angle2=20
percent1=28
percent2=28

#draw blockades
for _ in range(3):
    blockades.add(Blockades(random.randint(100, 600), random.randint(50, 225)))
for _ in range(1):
    health.add(Powerup(random.randint(100, 600), random.randint(50, 225)))

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
                if angle2<90:
                    angle2=angle2+1
            if event.key == pygame.K_DOWN:
                if angle2>0:
                    angle2=angle2-1
            if event.key == pygame.K_w:
                if angle1<90:
                    angle1=angle1+1
            if event.key == pygame.K_s:
                if angle1>0:
                    angle1=angle1-1
            if event.key==pygame.K_SPACE:
                if turn%2==0:
                    ball.image=blueball
                    ball.x=675
                    ball.y=425
                    ball.percent=percent2*-1
                    ball.angle=angle2*math.pi/180
                    turn=turn+1
                    ball.start=time.perf_counter()
                    print (turn)
                else:
                    ball.image=redball
                    ball.x = 100
                    ball.y = 425
                    ball.angle=angle1*math.pi/180
                    ball.percent=percent1
                    turn=turn+1
                    ball.start=time.perf_counter()
                    print (turn )

    # draw screen
    screen.blit(background, (0, 0))
    #draw blockades
    blockades.draw(screen)
    health.draw(screen)
    # draw lives
    stars.set_colorkey((0, 0, 0))
    for i in range(int(numlives1)):
        screen.blit(stars, (40+ (40*i), screen_height - tile_size+70))
    for i in range(int(numlives2)):
        screen.blit(stars, (650+ (40*i), screen_height - tile_size+70))
    # draw cannon and tower
    cannon1.drawcannonleft(screen)
    cannon2.drawcannonright(screen)
    tower.drawtower(screen)
    #draw ball
    ball.update()
    ball.draw(screen)

    #collisions:

    result1 = pygame.sprite.collide_rect(ball, cannon2)
    result2=pygame.sprite.collide_rect(ball, cannon1)
    result3=pygame.sprite.collide_rect(ball,tower)
    result4=pygame.sprite.spritecollide(ball, blockades, True)
    result5 = pygame.sprite.spritecollide(ball, health, True)
    if result3:
        ball.percent = 0
        ball.x = 330
        ball.y = 30
        ball.image = pygame.image.load("sprites_final/oof.png").convert()
        ball.image.set_colorkey((255, 255, 255))
        for block in blockades:
            blockades.remove(block)
        for i in range(3):
            blockades.add(Blockades(random.randint(100, 600), random.randint(50, 225)))
    if turn%2!=1:
        if result5:
            numlives1 = numlives1 + 1
            health.add(Powerup(random.randint(100, 600), random.randint(50, 225)))
        if result1:
            ball.percent=0
            ball.x=330
            ball.y=30
            ball.image = pygame.image.load("sprites_final/criticalhit.png").convert()
            ball.image.set_colorkey((255, 255, 255))
            for block in blockades:
                blockades.remove(block)
            for i in range(3):
                blockades.add(Blockades(random.randint(100, 600), random.randint(50, 225)))
            numlives2=numlives2-1
            print ('collide')
    if turn%2!=0:
        if result5:
            numlives2=numlives2+1
            health.add(Powerup(random.randint(100, 600), random.randint(50, 225)))
        if result2:
            ball.percent=0
            ball.x=330
            ball.y=30
            ball.image=pygame.image.load("sprites_final/criticalhit.png").convert()
            ball.image.set_colorkey((255, 255, 255))
            for block in blockades:
                blockades.remove(block)
            for i in range(3):
                blockades.add(Blockades(random.randint(100, 600), random.randint(50, 225)))
            numlives1=numlives1-1
            print ('collide')
    if result4:
        ball.percent = 0
        ball.x = 330
        ball.y = 30
        ball.image = pygame.image.load("sprites_final/oof.png").convert()
        ball.image.set_colorkey((255, 255, 255))
        for block in blockades:
            blockades.remove(block)
        for i in range(3):
            blockades.add(Blockades(random.randint(100, 600), random.randint(50, 225)))
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
