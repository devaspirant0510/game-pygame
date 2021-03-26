from init import State,GameState
from startscreen import st_sc,se_sc,startscreen_event,lo_sc,selectscreen_event,hw_to_pl,ending
from mod1 import mod1_play,mod1_event_key,mod1_pause,play,mod1_pause_event,mod1_load
from set_mode import UP,DOWN,LEFT,RIGHT
from mod2 import mod2_set,mod2_set_event,mod2_stage5,mod2_stage4,mod2_stage3,mod2_stage2,mod2_stage1,stageplay,stageplay4,stageplay3,stageplay2,stageplay5
from mod2 import mod2_loading
from mod2_gui import mod2_suc_1,mod2_suc_2,mod2_suc_3,mod2_suc_4,mod2_suc_event,mod2_pause,mod2_pause_event
from mod3 import mod3_set,mod3_stage1,picplay1,picplay2,picplay,mod3_stage2,mod3_stage3,mod3_loading
from mod3_gui_screen import mod3_stage2_suc,mod3_stage1_suc,mod3_pause_screen,mod3_fail_stage1,mod3_fail_stage2,mod3_fail_stage3
from button import mod3_stage1btn,mod3_stage2btn,mod3_stage3btn
from mod3_key_event import mod3_suc_event,mod3_pause_event,mod3_fail1_event,mod3_fail2_event
from sound import fail,cheer2,cheer1
from event_class import nexon_free_font
from color import WHITE
from set_mode import screen
import mod3
import pygame
import random
import sys

def CheckQuit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def UpdateStartScreen():
    for event in pygame.event.get():
        CheckQuit(event)
        global State        
        if startscreen_event(event) == "press_playbtn":
            State = GameState.loadingscreen
            print("press_playbtn")
        elif startscreen_event(event) == "press_how_to_play_btn":
            State = GameState.howtoplay
            print("press_how_to_play_btn")

def UpdateSelectScreen():
    for event in pygame.event.get():
        CheckQuit(event)
        global State
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selectscreen_event() == "press_mod1btn":
                State = GameState.mod1
            elif selectscreen_event() == "press_mod2btn":
                State = GameState.mod2_loading
            elif selectscreen_event() == "press_mod3btn":
                State = GameState.mod3_loading

def UpdateMod3Set():
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mod3_stage1btn.isover(mousepos):
                State = GameState.mod3_stage_1
            if mod3_stage2btn.isover(mousepos):
                State = GameState.mod3_stage_2
            if mod3_stage3btn.isover(mousepos):
                State = GameState.mod3_stage_3

def UpdateMod1PauseScreen():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if mod1_pause_event(event) == 'press_homebtn':
            State = GameState.startscreen
        if mod1_pause_event(event) == 'press_playbtn':
            State = GameState.mod1
        if mod1_pause_event(event) == 'press_menubtn':
            State = GameState.selectscreen

def UpdateMod2Set():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if mod2_set_event(event) == "press_stage1":
            State = GameState.mod2_stage_1
        if mod2_set_event(event) == "press_stage2":
            State = GameState.mod2_stage_2
        if mod2_set_event(event) == "press_stage3":
            State = GameState.mod2_stage_3
        if mod2_set_event(event) == "press_stage4":
            State = GameState.mod2_stage_4
        if mod2_set_event(event) == "press_stage5":
            State = GameState.mod2_stage_5

        
def UpdateMod2Suc1():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if mod2_suc_event(event)=="press_play":
            State=GameState.mod2_stage_1
        if mod2_suc_event(event)=="press_next":
            stageplay.create()
            State=GameState.mod2_stage_2
        if mod2_suc_event(event)=="press_menu":
            stageplay.create()
            State=GameState.selectscreen
        if mod2_suc_event(event)=="press_restart":
            stageplay.create()
            State=GameState.mod2_stage_1

def UpdateMod2Suc2():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if mod2_suc_event(event)=="press_next":
            stageplay2.create()
            State=GameState.mod2_stage_3
        if mod2_suc_event(event)=="press_menu":
            stageplay2.create()
            State=GameState.selectscreen
        if mod2_suc_event(event)=="press_restart":
            stageplay2.create()
            State=GameState.mod2_stage_2

def UpdateMod2Suc3():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if mod2_suc_event(event)=="press_next":
            stageplay3.create()
            State=GameState.mod2_stage_4
        if mod2_suc_event(event)=="press_menu":
            stageplay3.create()
            State=GameState.selectscreen
        if mod2_suc_event(event)=="press_restart":
            stageplay3.create()
            State=GameState.mod2_stage_3


def UpdateMod2Suc4():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if mod2_suc_event(event)=="press_next":
            stageplay4.create()
            State=GameState.mod2_stage_5
        if mod2_suc_event(event)=="press_menu":
            stageplay4.create()
            State=GameState.selectscreen
        if mod2_suc_event(event)=="press_restart":
            stageplay4.create()
            State=GameState.mod2_stage_4


def UpdateMod2PauseScreen():
    for event in pygame.event.get():
        CheckQuit(event)

        global State

        #mo는 현재 모드
        if mo==1:#현재 스테이지가 1일때
            if mod2_pause_event(event)=="press_home":
                State=GameState.startscreen
                stageplay.create()
            if mod2_pause_event(event)=="press_menu":
                State=GameState.selectscreen
                stageplay.create()
            if mod2_pause_event(event)=="press_play":
                State=GameState.mod2_stage_1
        if mo==2:#현재 스테이지가 2일때
            if mod2_pause_event(event)=="press_home":
                State=GameState.startscreen
                stageplay2.create()
            if mod2_pause_event(event)=="press_menu":
                State=GameState.selectscreen
                stageplay2.create()
            if mod2_pause_event(event)=="press_play":
                State=GameState.mod2_stage_2
        if mo==3:#현재 스테이지가 3일때
            if mod2_pause_event(event)=="press_home":
                State=GameState.startscreen
                stageplay3.create()
            if mod2_pause_event(event)=="press_menu":
                State=GameState.selectscreen
                stageplay3.create()
            if mod2_pause_event(event)=="press_play":
                State=GameState.mod2_stage_3
        if mo==4:#현재 스테이지가 4일때
            if mod2_pause_event(event)=="press_home":
                State=GameState.startscreen
                stageplay4.create()
            if mod2_pause_event(event)=="press_menu":
                State=GameState.selectscreen
                stageplay4.create()
            if mod2_pause_event(event)=="press_play":
                State=GameState.mod2_stage_4
        if mo==5:#현재 스테이지가 5일때
            if mod2_pause_event(event)=="press_home":
                State=GameState.startscreen
                stageplay5.create()
            if mod2_pause_event(event)=="press_menu":
                State=GameState.selectscreen
                stageplay5.create()
            if mod2_pause_event(event)=="press_play":
                State=GameState.mod2_stage_5

def UpdateMod3Suc1():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mod3
        if mod2_suc_event(event) == "press_next":
            mod3.score = 300
            picplay1.create()
            State = GameState.mod3_stage_2
        if mod2_suc_event(event) == "press_menu":
            mod3.score = 300
            picplay1.create()
            State = GameState.selectscreen
        if mod2_suc_event(event) == "press_restart":
            mod3.score=300
            picplay1.create()
            State = GameState.mod3_stage_1

def UpdateMod3Suc2():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mod3
        if mod3_suc_event(event)=='press_next':
            mod3.score = 300
            picplay.create()
            State=GameState.mod3_stage_3
        if mod3_suc_event(event)=='press_menu':
            mod3.score = 300
            picplay.create()
            State=GameState.selectscreen
        if mod3_suc_event(event)=='press_restart':
            mod3.score = 300
            picplay.create()
            State=GameState.mod3_stage_2


def UpdateMod3PauseScreen():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mod3

        if ko==1:
            if mod3_pause_event(event)=="press_home":
                mod3.score = 300
                picplay1.create()
                State=GameState.startscreen
            if mod3_pause_event(event)=="press_play":

                State=GameState.mod3_stage_1
            if mod3_pause_event(event)=="press_menu":
                mod3.score = 300
                picplay1.create()
                State=GameState.selectscreen
        if ko==2:
            if mod3_pause_event(event)=="press_home":
                mod3.score = 300
                picplay.create()
                State=GameState.startscreen
            if mod3_pause_event(event)=="press_play":
                State=GameState.mod3_stage_2
            if mod3_pause_event(event)=="press_menu":
                mod3.score = 300
                picplay.create()
                State=GameState.selectscreen
        if ko==3:
            if mod3_pause_event(event)=="press_home":
                picplay2.create()
                mod3.score = 300
                State=GameState.startscreen
            if mod3_pause_event(event)=="press_play":
                State=GameState.mod3_stage_3
            if mod3_pause_event(event)=="press_menu":
                mod3.score = 300
                picplay2.create()
                State=GameState.selectscreen


def UpdateMod3Fail1():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mod3

        if mod3_fail1_event(event)=="retry":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay1.create()
            State=GameState.mod3_stage_1
        if mod3_fail1_event(event)=="menu":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay1.create()
            State=GameState.selectscreen
        if mod3_fail1_event(event)=="home":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay1.create()
            State=GameState.startscreen


def UpdateMod3Fail2():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mod3

        if mod3_fail1_event(event)=="retry":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay.create()
            State=GameState.mod3_stage_2
        if mod3_fail1_event(event)=="menu":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay.create()
            State=GameState.selectscreen
        if mod3_fail1_event(event)=="home":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay.create()
            State=GameState.startscreen


def UpdateMod3Fail3():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mod3

        if mod3_fail1_event(event)=="retry":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay2.create()
            State=GameState.mod3_stage_3
        if mod3_fail1_event(event)=="menu":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay2.create()
            State=GameState.selectscreen
        if mod3_fail1_event(event)=="home":
            fail.stop()
            pygame.mixer.music.play(-1)
            mod3.score=300
            picplay2.create()
            State=GameState.startscreen

def UpdateMod1():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if event.type == pygame.KEYDOWN:
            if mod1_event_key(event)==True:
                State=GameState.mod1_pause_screen


def UpdateMod2Stage1():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mo
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP,pygame.K_w]:
                stageplay.control(UP)
            if event.key in [pygame.K_DOWN,pygame.K_s]:
                stageplay.control(DOWN)
            if event.key in [pygame.K_LEFT,pygame.K_a]:
                stageplay.control(LEFT)
            if event.key in [pygame.K_RIGHT,pygame.K_d]:
                stageplay.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                mo=1
                State=GameState.mod2_pause_screen



def UpdateMod2Stage2():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mo
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP,pygame.K_w]:
                stageplay2.control(UP)
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                stageplay2.control(DOWN)
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                stageplay2.control(LEFT)
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                stageplay2.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                mo=2
                State=GameState.mod2_pause_screen


def UpdateMod2Stage3():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mo
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP,pygame.K_w]:
                stageplay3.control(UP)
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                stageplay3.control(DOWN)
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                stageplay3.control(LEFT)
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                stageplay3.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                mo=3
                State=GameState.mod2_pause_screen

def UpdateMod2Stage4():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mo
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP,pygame.K_w]:
                stageplay4.control(UP)
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                stageplay4.control(DOWN)
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                stageplay4.control(LEFT)
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                stageplay4.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                mo=4
                State=GameState.mod2_pause_screen


def UpdateMod2Stage5():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global mo
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP,pygame.K_w]:
                stageplay5.control(UP)
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                stageplay5.control(DOWN)
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                stageplay5.control(LEFT)
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                stageplay5.control(RIGHT)
            if event.key == pygame.K_ESCAPE:
                mo=5
                State=GameState.mod2_pause_screen




def UpdateMod3Stage1():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global ko
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w,pygame.K_UP]:
                picplay1.control(UP)
            if event.key in [pygame.K_a,pygame.K_LEFT]:
                picplay1.control(LEFT)
            if event.key in [pygame.K_s,pygame.K_DOWN]:
                picplay1.control(DOWN)
            if event.key in [pygame.K_d,pygame.K_RIGHT]:
                picplay1.control(RIGHT)
            if event.key ==  pygame.K_ESCAPE:
                State=GameState.mod3_pause_screen
                ko=1


def UpdateMod3Stage2():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global ko
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w,pygame.K_UP]:
                picplay.control(UP)
            if event.key in [pygame.K_a,pygame.K_LEFT]:
                picplay.control(LEFT)
            if event.key in [pygame.K_s,pygame.K_DOWN]:
                picplay.control(DOWN)
            if event.key in [pygame.K_d,pygame.K_RIGHT]:
                picplay.control(RIGHT)
            if event.key ==  pygame.K_ESCAPE:
                State=GameState.mod3_pause_screen
                ko=2

def UpdateMod3Stage3():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        global ko
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w,pygame.K_UP]:
                picplay2.control(UP)
            if event.key in [pygame.K_a,pygame.K_LEFT]:
                picplay2.control(LEFT)
            if event.key in [pygame.K_s,pygame.K_DOWN]:
                picplay2.control(DOWN)
            if event.key in [pygame.K_d,pygame.K_RIGHT]:
                picplay2.control(RIGHT)
            if event.key ==  pygame.K_ESCAPE:
                State=GameState.mod3_pause_screen
                ko=3


def UpdateHowToPlay():
    for event in pygame.event.get():
        CheckQuit(event)

        global State
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                State=GameState.startscreen


if __name__ == '__main__':
    x=-400
    ongame=True
    pygame.init()
    clock=pygame.time.Clock()
    while ongame:


        if State == GameState.startscreen:
            UpdateStartScreen()
            st_sc()
        elif State == GameState.selectscreen:
            UpdateSelectScreen()
            se_sc()
        elif State == GameState.mod3_set:
            UpdateMod3Set()
            mod3_set()
        elif State == GameState.mod1_pause_screen:
            UpdateMod1PauseScreen()
            mod1_pause()
        elif State == GameState.mod2_set:
            UpdateMod2Set()
            mod2_set()
        elif State == GameState.mod2_suc_1:
            UpdateMod2Suc1()
            mod2_suc_1()
        elif State == GameState.mod2_suc_2:
            UpdateMod2Suc2()
            mod2_suc_2()
        elif State==GameState.mod2_suc_3:
            UpdateMod2Suc3()
            mod2_suc_3()
        elif State==GameState.mod2_suc_4:
            UpdateMod2Suc4()
            mod2_suc_4()
        elif State==GameState.mod2_pause_screen:
            UpdateMod2PauseScreen()
            mod2_pause()
        elif State == GameState.mod3_suc1:
            UpdateMod3Suc1()
            mod3_stage1_suc(rank)
        elif State == GameState.mod3_suc2:
            UpdateMod3Suc2()
            mod3_stage2_suc(rank)
        elif State == GameState.mod3_pause_screen:
            UpdateMod3PauseScreen()
            mod3_pause_screen()
        elif State==GameState.mod3_fail1:
            UpdateMod3Fail1()
            mod3_fail_stage1()
        elif State==GameState.mod3_fail2:
            UpdateMod3Fail2()
            mod3_fail_stage2()
        elif State==GameState.mod3_fail3:
            UpdateMod3Fail3()
            mod3_fail_stage3()
        

        elif State==GameState.mod1:
            UpdateMod1()
            mod1_play()

        elif State==GameState.mod2_stage_1:
            UpdateMod2Stage1()
            if mod2_stage1()==True:
                State = GameState.mod2_suc_1

        elif State==GameState.mod2_stage_2:
            UpdateMod2Stage2()
            if mod2_stage2() == True:
                State = GameState.mod2_suc_2

        elif State==GameState.mod2_stage_3:
            UpdateMod2Stage3()
            if mod2_stage3() == True:
                State = GameState.mod2_suc_3

        elif State==GameState.mod2_stage_4:
            UpdateMod2Stage4()
            if mod2_stage4() == True:
                State = GameState.mod2_suc_4

        elif State==GameState.mod2_stage_5:
            UpdateMod2Stage5()
            if mod2_stage5() == True:
                State = GameState.ending_credit

        elif State==GameState.mod3_stage_1:
            UpdateMod3Stage1()
            cheer=random.choice([cheer1,cheer2])
            S=mod3_stage1()
            if S=='A':
                rank='A'
                cheer.play()
                State=GameState.mod3_suc1
            elif S=='B':
                rank = 'B'
                cheer.play()
                State=GameState.mod3_suc1
            elif S=='C':
                rank = 'C'
                cheer.play()
                State=GameState.mod3_suc1
            elif S=='D':
                pygame.mixer.music.stop()
                fail.play(1)
                rank = 'D'
                State=GameState.mod3_fail1
            elif S=='F':
                pygame.mixer.music.stop()
                fail.play(1)
                rank = 'F'
                State=GameState.mod3_fail1

        elif State==GameState.mod3_stage_2:
            UpdateMod3Stage2()
            cheer = random.choice([cheer1, cheer2])
            S = mod3_stage2()
            if S == 'A':
                rank = 'A'
                cheer.play()
                State = GameState.mod3_suc2
            elif S == 'B':
                rank = 'B'
                cheer.play()
                State = GameState.mod3_suc2
            elif S == 'C':
                rank = 'C'
                cheer.play()
                State = GameState.mod3_suc2
            elif S == 'D':
                pygame.mixer.music.stop()
                fail.play(1)
                rank = 'D'
                State = GameState.mod3_fail2
            elif S == 'F':
                pygame.mixer.music.stop()
                fail.play(1)
                rank = 'F'
                State = GameState.mod3_fail2
        elif State==GameState.mod3_stage_3:
            UpdateMod3Stage3()
            cheer = random.choice([cheer1, cheer2])
            S = mod3_stage3()
            if S == 'A':
                rank = 'A'
                cheer.play()
                State = GameState.ending_credit
            elif S == 'B':
                rank = 'B'
                cheer.play()
                State = GameState.ending_credit
            elif S == 'C':
                rank = 'C'
                cheer.play()
                State = GameState.ending_credit
            elif S == 'D':
                fail.play(1)
                rank = 'D'
                State = GameState.mod3_fail3
            elif S == 'F':
                fail.play(1)
                rank = 'F'
                State = GameState.mod3_fail3
        elif State==GameState.howtoplay:
            UpdateHowToPlay()
            hw_to_pl()
        elif State == GameState.mod2_loading:
            if mod2_loading()==True:
                State=GameState.mod2_set

        elif State == GameState.mod3_loading:
            if mod3_loading()==True:
                State=GameState.mod3_set
            
        elif State == GameState.ending_credit:
            screen.fill(0)
            if ending() == True:
                nexon_free_font("esc를 눌러 종료합니다. ", "", WHITE, 80, (50, 200), screen)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

        elif State == GameState.loadingscreen:
            print("GameState.loadingscreen")
            if lo_sc()==True:
                State = GameState.selectscreen

        pygame.display.flip()













