import pygame
import time
from image import homescreen,background,loadingbar,loadingem,loadingtext,howtoplay,endcredit,mod1,mod2,tt,mod3
from set_mode import screen,SCREEN_HEIGHT,SCREEN_WIDTH
from event_class import nexon_free_font
from button import gameplaybtn,howtoplaybtn,mod3btn,mod2btn,mod1btn
from sound import loading
from color import WHITE,BLACK
from sound import endingsound
import sys
from init import State,GameState
def st_sc():
    pygame.init()
    screen.blit(homescreen, (0, 0))
    pygame.display.flip()
def startscreen_event(event):
    mousepos=pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if gameplaybtn.isover(mousepos):
            return "press_playbtn"
        if howtoplaybtn.isover(mousepos):
            return "press_how_to_play_btn"
x=-400
def lo_sc():
    global x
    pygame.init()
    for i in range(0, SCREEN_WIDTH, 256):
        for j in range(0, SCREEN_HEIGHT, 256):
            screen.blit(background, (i, j))
    screen.blit(loadingem, (250, 443))
    screen.blit(loadingtext, (500, 390))

    screen.blit(loadingbar, (x, 445))

    x += 20
    for i in range(-15, SCREEN_HEIGHT, 256):
        screen.blit(background, (0, i))
    if x > 268:
        screen.blit(loadingbar, (268, 445))
        x = 268
        loading.play()
        time.sleep(1)
        x = -400
        return True


    pygame.display.flip()

def se_sc():
    pygame.init()
    for i in range(0,SCREEN_WIDTH,256):
        for j in range(0,SCREEN_HEIGHT,256):
            screen.blit(tt,(i,j))
    pygame.draw.rect(screen, WHITE, (100, 25, 1000, 400))
    screen.blit(mod1,(100,25))
    nexon_free_font("ArcadeMod", "", BLACK, 40, (100, 25), screen)

    pygame.draw.rect(screen, WHITE, (100, 450, 450, 400))
    screen.blit(mod2, (100, 450))
    nexon_free_font("StageMod", "", BLACK, 40, (100, 450), screen)
    pygame.draw.rect(screen, WHITE, (650, 450, 450, 400))
    screen.blit(mod3,(650,450))
    nexon_free_font("PerfectMod", "", BLACK, 40, (650, 450), screen)
    pygame.display.flip()
def hw_to_pl():
    screen.blit(howtoplay,(0,0))
    pygame.display.flip()

def selectscreen_event():
    pygame.init()
    mousepos = pygame.mouse.get_pos()
    if mod1btn.isover(mousepos):
        return "press_mod1btn"
    if mod2btn.isover(mousepos):
        return "press_mod2btn"
    if mod3btn.isover(mousepos):
        return "press_mod3btn"
y=-2000
def ending():
    global y
    pygame.mixer.music.stop()
    endingsound.play()
    y-=3
    screen.blit(endcredit,(0,y))
    if y <-9000:

        return True

    pygame.display.flip()





