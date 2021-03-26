import pygame
import sys
import mod3
from set_mode import UP,DOWN,LEFT,RIGHT

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
