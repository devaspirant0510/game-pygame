import pygame
from image import surestart,wintext,sumenu,mod2sucgui,mod2suctable,sunext,background,pauseheader,home,menu,losetext,suhome
import image
from sound import cheer1,cheer2
from color import BLACK,RED,ORANGE,YELLOW
from event_class import nexon_free_font
from mod3 import picplay,picplay1,picplay2,score
from set_mode import screen
import random
from  sound import fail
def mod3_pause_screen():
    pygame.init()
    for i in range(0,1400,256):
        for j in range(0,900,256):
            screen.blit(background,(i,j))
    screen.blit(pauseheader,(350,50))
    screen.blit(image.play,(200,350))
    screen.blit(home,(500,350))
    screen.blit(menu,(800,350))
    pygame.display.flip()
def mod3_fail_stage1():
    screen.blit(mod2sucgui,(260,100))
    screen.blit(mod2suctable,(360,200))
    nexon_free_font("Failed...","",BLACK,100,(390,300),screen)
    screen.blit(losetext,(370,20))
    screen.blit(surestart,(300,560))
    screen.blit(sumenu,(500,560))
    screen.blit(suhome,(700,560))


    picplay1.create()
    pygame.display.flip()
def mod3_fail_stage2():
    screen.blit(mod2sucgui,(260,100))
    screen.blit(mod2suctable,(360,200))
    nexon_free_font("Failed...", "", BLACK, 100, (390, 300), screen)
    screen.blit(losetext,(370,20))
    screen.blit(surestart,(300,560))
    screen.blit(sumenu,(500,560))
    screen.blit(sunext,(700,560))

    picplay1.create()
    pygame.display.flip()
def mod3_fail_stage3():
    screen.blit(mod2sucgui,(260,100))
    screen.blit(mod2suctable,(360,200))
    nexon_free_font("Failed...", "", BLACK, 100, (390, 300), screen)
    screen.blit(losetext,(370,20))
    screen.blit(surestart,(300,560))
    screen.blit(sumenu,(500,560))
    screen.blit(sunext,(700,560))

    picplay1.create()
    pygame.display.flip()
def mod3_stage1_suc(rank):

    if rank== 'A':
        color=RED
    elif rank=='B':
        color=ORANGE
    elif rank =='C':
        color=YELLOW
    screen.blit(mod2sucgui,(260,100))
    screen.blit(mod2suctable,(360,200))
    screen.blit(wintext,(370,20))
    screen.blit(surestart,(300,560))
    screen.blit(sumenu,(500,560))
    screen.blit(sunext,(700,560))
    nexon_free_font("등급 : ","",BLACK,30,(420,340),screen)
    nexon_free_font("",rank,color,250,(500,220),screen)


    picplay1.create()
    pygame.display.flip()
def mod3_stage2_suc(rank):
    if rank== 'A':
        color=RED
    elif rank=='B':
        color=ORANGE
    elif rank =='C':
        color=YELLOW
    screen.blit(mod2sucgui,(260,100))
    screen.blit(mod2suctable,(360,200))
    screen.blit(wintext,(370,20))
    screen.blit(surestart,(300,560))
    screen.blit(sumenu,(500,560))
    screen.blit(sunext,(700,560))
    nexon_free_font("등급 : ","",BLACK,30,(420,340),screen)
    nexon_free_font("",rank,color,250,(500,220),screen)
    picplay.create()
    pygame.display.flip()
