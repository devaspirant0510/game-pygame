from sound import success
import pygame
from color import BLACK
import image
from event_class import nexon_free_font
from image import mod2sucgui,mod2suctable,sumenu,sunext,surestart,wintext,background,home,menu,pauseheader,lock
from button import menubtn,playbtn,homebtn,surestartbtn,sunextbtn,sumenubtn
from set_mode import screen
from mod2 import stageplay
from init import lockevent
def mod2_suc_1():
    lockevent[0]=True
    screen.blit(mod2sucgui, (260, 100))
    screen.blit(mod2suctable, (360, 200))
    screen.blit(lock,(530,300))
    nexon_free_font("스테이지 잠금 해제", "", BLACK, 30, (460, 250), screen)
    screen.blit(wintext, (370, 20))
    screen.blit(surestart, (300, 560))
    screen.blit(sumenu, (500, 560))
    screen.blit(sunext, (700, 560))

    stageplay.create()
    pygame.display.flip()
def mod2_suc_2():
    lockevent[1]=True
    screen.blit(mod2sucgui, (260, 100))
    screen.blit(mod2suctable, (360, 200))
    screen.blit(lock,(530,300))
    nexon_free_font("스테이지 잠금 해제", "", BLACK, 30, (460, 250), screen)
    screen.blit(wintext, (370, 20))
    screen.blit(surestart, (300, 560))
    screen.blit(sumenu, (500, 560))
    screen.blit(sunext, (700, 560))
    stageplay.create()
    pygame.display.flip()
def mod2_suc_3():
    lockevent[2]=True
    screen.blit(mod2sucgui, (260, 100))
    screen.blit(mod2suctable, (360, 200))
    screen.blit(lock,(530,300))
    nexon_free_font("스테이지 잠금 해제", "", BLACK, 30, (460, 250), screen)
    screen.blit(wintext, (370, 20))
    screen.blit(surestart, (300, 560))
    screen.blit(sumenu, (500, 560))
    screen.blit(sunext, (700, 560))
    stageplay.create()
    pygame.display.flip()
def mod2_suc_4():
    lockevent[3]=True
    screen.blit(mod2sucgui, (260, 100))
    screen.blit(mod2suctable, (360, 200))
    screen.blit(lock,(530,300))
    nexon_free_font("스테이지 잠금 해제", "", BLACK, 30, (460, 250), screen)
    screen.blit(wintext, (370, 20))
    screen.blit(surestart, (300, 560))
    screen.blit(sumenu, (500, 560))
    screen.blit(sunext, (700, 560))
    stageplay.create()
    pygame.display.flip()
def mod2_pause():
    pygame.init()
    for i in range(0,1400,256):
        for j in range(0,900,256):
            screen.blit(background,(i,j))
    screen.blit(pauseheader,(350,50))
    screen.blit(image.play,(200,350))
    screen.blit(home,(500,350))
    screen.blit(menu,(800,350))
    pygame.display.flip()
def mod2_pause_event(event):
    mousepos=pygame.mouse.get_pos()
    if event.type== pygame.MOUSEBUTTONUP:
        if playbtn.isover(mousepos):
            return "press_play"
        if menubtn.isover(mousepos):
            return "press_menu"
        if homebtn.isover(mousepos):
            return "press_home"

def mod2_suc_event(event):

    mousepos=pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
        if sumenubtn.isover(mousepos):
            print(mousepos)
            success.play()
            return "press_menu"
        if surestartbtn.isover(mousepos):
            print(mousepos)
            success.play()
            return "press_restart"
        if sunextbtn.isover(mousepos):
            print(mousepos)
            success.play()
            return "press_next"
    pygame.display.flip()