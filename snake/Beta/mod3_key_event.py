import pygame
import sys
import mod3
from set_mode import UP,DOWN,LEFT,RIGHT
from button import sunextbtn,sumenubtn,surestartbtn,playbtn,menubtn,homebtn
from button  import  mod3_stage1btn,mod3_stage3btn,mod3_stage2btn
def mod3_suc_event(event):
    mousepos=pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if sunextbtn.isover(mousepos):
            return "press_next"
        if surestartbtn.isover(mousepos):
            return "press_restart"
        if sumenubtn.isover(mousepos):
            return "press_menu"
def mod3_pause_event(event):
    mousepos=pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
        if playbtn.isover(mousepos):
            return "press_play"
        if menubtn.isover(mousepos):
            return "press_menu"
        if homebtn.isover(mousepos):
            return "press_home"
def mod3_stage1_event_key():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w,pygame.K_UP]:
                mod3.picplay1.control(UP)
            if event.key in [pygame.K_a,pygame.K_LEFT]:
                mod3.picplay1.control(LEFT)
            if event.key in [pygame.K_s,pygame.K_DOWN]:
                mod3.picplay1.control(DOWN)
            if event.key in [pygame.K_d,pygame.K_RIGHT]:
                mod3.picplay1.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                return True
def mod3_stage2_event_key():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w,pygame.K_UP]:
                mod3.picplay.control(UP)
            if event.key in [pygame.K_a,pygame.K_LEFT]:
                mod3.picplay.control(LEFT)
            if event.key in [pygame.K_s,pygame.K_DOWN]:
                mod3.picplay.control(DOWN)
            if event.key in [pygame.K_d,pygame.K_RIGHT]:
                mod3.picplay.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                return True
def mod3_stage3_event_key():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w,pygame.K_UP]:
                mod3.picplay2.control(UP)
            if event.key in [pygame.K_a,pygame.K_LEFT]:
                mod3.picplay2.control(LEFT)
            if event.key in [pygame.K_s,pygame.K_DOWN]:
                mod3.picplay2.control(DOWN)
            if event.key in [pygame.K_d,pygame.K_RIGHT]:
                mod3.picplay2.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                return True
def mod3_fail1_event(event):
    mousepos=pygame.mouse.get_pos()
    if event.type== pygame.MOUSEBUTTONDOWN:
        if surestartbtn.isover(mousepos):
            return "retry"
        if sumenubtn.isover(mousepos):

            return "menu"
        if sunextbtn.isover(mousepos):
            return "home"
def mod3_fail2_event(event):
    mousepos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if surestartbtn.isover(mousepos):
            return "retry"
        if sumenubtn.isover(mousepos):
            return "menu"
        if sunextbtn.isover(mousepos):
            return "home"
def mod3_fail3_event(event):
    mousepos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if surestartbtn.isover(mousepos):
            return "retry"
        if sumenubtn.isover(mousepos):
            return "menu"
        if sunextbtn.isover(mousepos):
            return "home"