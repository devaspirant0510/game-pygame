import pygame
from image import surestart,wintext,sumenu,mod2sucgui,mod2suctable,sunext
from mod3 import picplay,picplay1,picplay2
from set_mode import screen
from event_class import nexon_free_font
def mod3_stage1_suc():
    pygame.init()
    screen.blit(mod2sucgui,(260,100))
    screen.blit(mod2suctable,(360,200))
    screen.blit(wintext,(370,20))
    screen.blit(surestart,(300,560))
    screen.blit(sumenu,(500,560))
    screen.blit(sunext,(700,560))

    picplay1.create()
    pygame.display.flip()
def mod3_stage2_suc():
    screen.blit(mod2sucgui,(260,100))
    screen.blit(mod2suctable,(360,200))
    screen.blit(wintext,(370,20))
    screen.blit(surestart,(300,560))
    screen.blit(sumenu,(500,560))
    screen.blit(sunext,(700,560))
    picplay.create()
    pygame.display.flip()
