from set_mode import screen,UP,DOWN,PIXEL_SIZE,SCREEN_WIDTH,SCREEN_HEIGHT
from image import backkey,head,dead,background,loadingtext,tile,loadingem,loadingbar,backnum,mod2background,num1,num2,num3,num4,num5,headerbtn,load
from sound import deadso4,deadso1,deadso2,deadso3,cheer1,cheer2,loading,locksound,success
from button import modstage5btn,modstage4btn,modstage3btn,modstage2btn,modstage1btn
from mod1 import Player
from image import lock,finish,finishr,finish3,finish5,finishb
from color import BLUE,GRAY,BLACK,WHITE,GREEN
from event_class import nexon_free_font,namu_free_font
import random
import time
import pygame
from init import lockevent
x=-400
def mod2_loading():
    global x
    pygame.init()
    for i in range(0, SCREEN_WIDTH, 256):
        for j in range(0, SCREEN_HEIGHT, 256):
            screen.blit(background, (i, j))

    screen.blit(loadingtext, (500, 390))

    screen.blit(load, (x, 445))

    x += 20
    print(x)
    for i in range(-15, SCREEN_HEIGHT, 256):
        screen.blit(background, (0, i))
    if x > 265:
        screen.blit(load, (260, 445))
        x = 260

        time.sleep(1)
        x = -400
        return True
    pygame.display.flip()
def mod2_set():
    screen.blit(mod2background, (-100, -100))
    screen.blit(headerbtn,(250,30))
    namu_free_font("stage mod","",BLACK,140,(320,50),screen)
    screen.blit(backkey, (1000, 700))
    screen.blit(backnum,(40,381))
    screen.blit(backnum, (278, 381))
    screen.blit(backnum, (510, 381))
    screen.blit(backnum, (740, 381))
    screen.blit(backnum, (979, 381))
    screen.blit(num1,(110,431))
    screen.blit(num2,(338,431))
    screen.blit(num3,(570,431))
    screen.blit(num4,(800,431))
    screen.blit(num5,(1039,431))

    if lockevent[0]==False and lockevent[1]==False and lockevent[2]==False and lockevent[3]==False:
        screen.blit(lock,(313,401))
        screen.blit(lock,(545,401))
        screen.blit(lock, (775, 401))
        screen.blit(lock, (1014, 401))
    if lockevent[0]==True and lockevent[1]==False and lockevent[2]==False and lockevent[3]==False:
        screen.blit(lock,(545,401))
        screen.blit(lock, (775, 401))
        screen.blit(lock, (1014, 401))
    if lockevent[0]==True and lockevent[1]==True and lockevent[2]==False and lockevent[3]==False:
        screen.blit(lock, (775, 401))
        screen.blit(lock, (1014, 401))
    if lockevent[0]==True and lockevent[1]==True and lockevent[2]==True and lockevent[3]==False:
        screen.blit(lock, (1014, 401))


    pygame.display.flip()

def mod2_stage1():
    pygame.init()
    screen.fill(GRAY)
    fp1 = finishpoint(1040, 140, 160, 20, screen)
    cheer = random.choice([cheer2, cheer1])
    for i in range(0,1200,128):
        for j in range(0,900,128):
            screen.blit(background,(i,j))
    nexon_free_font("stage 1", "", BLACK, 30, (340, 20), screen)
    stageplay.draw(screen)
    stageplay.head()
    stageplay.move()
    wall1 = Wall(140, 200, 60, 700)
    crash_wall(stageplay, wall1)
    wall2 = Wall(200, 200, 140, 700)
    crash_wall(stageplay, wall2)
    wall3 = Wall(340, 340, 140, 600)
    crash_wall(stageplay, wall3)

    wall4 = Wall(480, 480, 140, 600)
    crash_wall(stageplay, wall4)
    wall8 = Wall(480, 0, 140, 140)
    crash_wall(stageplay, wall8)
    wall5 = Wall(620, 620, 140, 700)
    crash_wall(stageplay, wall5)
    wall9 = Wall(620, 0, 140, 280)
    crash_wall(stageplay, wall9)
    wall6 = Wall(760, 760, 440, 700)
    crash_wall(stageplay, wall6)
    wall10 = Wall(760, 0, 140, 420)
    crash_wall(stageplay, wall10)
    wall11 = Wall(900, 0, 140, 560)
    crash_wall(stageplay, wall11)
    for i in range(140, 200, 20):
        for j in range(200, 900, 20):
            screen.blit(tile, (i, j))

    for i in range(200, 340, 20):
        for j in range(200, 900, 20):
            screen.blit(tile, (i, j))

    for i in range(340, 480, 20):
        for j in range(340, 940, 20):
            screen.blit(tile, (i, j))

    for i in range(480, 620, 20):
        for j in range(480, 1080, 20):
            screen.blit(tile, (i, j))

    for i in range(480, 620, 20):
        for j in range(0, 140, 20):
            screen.blit(tile, (i, j))

    for i in range(620, 760, 20):
        for j in range(620, 1320, 20):
            screen.blit(tile, (i, j))

    for i in range(620, 760, 20):
        for j in range(0, 280, 20):
            screen.blit(tile, (i, j))

    for i in range(760, 1200, 20):
        for j in range(760, 1460, 20):
            screen.blit(tile, (i, j))

    for i in range(760, 900, 20):
        for j in range(0, 420, 20):
            screen.blit(tile, (i, j))

    for i in range(900, 1040, 20):
        for j in range(0, 560, 20):
            screen.blit(tile, (i, j))





    screen.blit(finish,(1040,100))

    if point_finish(stageplay, fp1) == True:
        cheer.play()


        return True
    pygame.display.flip()
def mod2_stage2():
    pygame.init()
    screen.fill(GRAY)

    cheer = random.choice([cheer2, cheer1])
    fp1 = finishpoint(1040, 760, 160, 20, screen)
    for i in range(0,1200,128):
        for j in range(0,900,128):
            screen.blit(background,(i,j))
    nexon_free_font("stage 2", "", BLACK, 30, (310, 20), screen)
    stageplay2.draw(screen)
    stageplay2.head()
    stageplay2.move()
    wall1 = Wall(0, 840, 1200, 80)
    crash_wall(stageplay2, wall1)
    wall2 = Wall(140, 0, 60, 700)
    crash_wall(stageplay2, wall2)
    wall3 = Wall(300, 300, 60, 700)
    crash_wall(stageplay2, wall3)
    wall4 = Wall(460, 0, 60, 700)
    crash_wall(stageplay2, wall4)
    wall5 = Wall(620, 300, 60, 700)
    crash_wall(stageplay2, wall5)
    wall6 = Wall(800, 0, 60, 700)
    crash_wall(stageplay2, wall6)
    wall7 = Wall(980, 300, 60, 700)
    crash_wall(stageplay2, wall7)


    for i in range(0, 1200, 20):
        for j in range(840, 920, 20):
            screen.blit(tile, (i, j))

    for i in range(140, 200, 20):
        for j in range(0, 700, 20):
            screen.blit(tile, (i, j))

    for i in range(300, 360, 20):
        for j in range(300, 1000, 20):
            screen.blit(tile, (i, j))

    for i in range(460, 520, 20):
        for j in range(0, 700, 20):
            screen.blit(tile, (i, j))

    for i in range(620, 680, 20):
        for j in range(300, 1000, 20):
            screen.blit(tile, (i, j))

    for i in range(800, 860, 20):
        for j in range(0, 700, 20):
            screen.blit(tile, (i, j))

    for i in range(980, 1040, 20):
        for j in range(300, 1000, 20):
            screen.blit(tile, (i, j))


    screen.blit(finishr,(1040,760))

    if point_finish(stageplay2, fp1) == True:
        cheer.play()
        return True

    pygame.display.flip()
def mod2_stage3():
    pygame.init()
    cheer=random.choice([cheer2,cheer1])
    screen.fill(GRAY)
    fp1 = finishpoint(80, 95, 120, 20, screen)
    for i in range(0,1200,128):
        for j in range(0,900,128):
            screen.blit(background,(i,j))
    nexon_free_font("stage 3", "", BLACK, 30, (400, 20), screen)
    stageplay3.draw(screen)
    stageplay3.head()
    stageplay3.move()
    wall1 = Wall(900, 400, 300, 60)
    crash_wall(stageplay3, wall1)
    wall7 = Wall(900, 680, 300, 60)
    crash_wall(stageplay3, wall7)
    wall2 = Wall(740, 0, 60, 800)
    crash_wall(stageplay3, wall2)
    wall6 = Wall(740, 540, 300, 60)
    crash_wall(stageplay3, wall6)
    wall3 = Wall(440, 440, 60, 480)
    crash_wall(stageplay3, wall3)
    wall4 = Wall(440, 380, 240, 60)
    crash_wall(stageplay3, wall4)
    wall8 = Wall(580, 500, 160, 60)
    crash_wall(stageplay3, wall8)
    wall9 = Wall(440, 620, 240, 60)
    crash_wall(stageplay3, wall9)
    wall10 = Wall(640, 80, 40, 300)
    crash_wall(stageplay3, wall10)
    wall11 = Wall(580, 740, 220, 60)
    crash_wall(stageplay3, wall11)
    wall12 = Wall(520, 0, 40, 300)
    crash_wall(stageplay3, wall12)
    wall5 = Wall(200, 0, 60, 700)
    crash_wall(stageplay3, wall5)
    wall13 = Wall(380, 100, 60, 500)
    crash_wall(stageplay3, wall13)
    wall14 = Wall(0, 0, 80, 900)
    crash_wall(stageplay3, wall14)
    for i in range(900, 1200, 20):
        for j in range(400, 460, 20):
            screen.blit(tile, (i, j))

    for i in range(900, 1200, 20):
        for j in range(680, 740, 20):
            screen.blit(tile, (i, j))

    for i in range(740, 800, 20):
        for j in range(0, 800, 20):
            screen.blit(tile, (i, j))

    for i in range(740, 1040, 20):
        for j in range(540, 600, 20):
            screen.blit(tile, (i, j))

    for i in range(440, 500, 20):
        for j in range(440, 920, 20):
            screen.blit(tile, (i, j))

    for i in range(440, 680, 20):
        for j in range(380, 440, 20):
            screen.blit(tile, (i, j))

    for i in range(580, 740, 20):
        for j in range(500, 560, 20):
            screen.blit(tile, (i, j))

    for i in range(440, 680, 20):
        for j in range(620, 680, 20):
            screen.blit(tile, (i, j))

    for i in range(640, 680, 20):
        for j in range(80, 380, 20):
            screen.blit(tile, (i, j))

    for i in range(580, 800, 20):
        for j in range(740, 800, 20):
            screen.blit(tile, (i, j))

    for i in range(520, 560, 20):
        for j in range(0, 300, 20):
            screen.blit(tile, (i, j))

    for i in range(200, 260, 20):
        for j in range(0, 700, 20):
            screen.blit(tile, (i, j))

    for i in range(380, 440, 20):
        for j in range(100, 600, 20):
            screen.blit(tile, (i, j))

    for i in range(0, 80, 20):
        for j in range(0, 900, 20):
            screen.blit(tile, (i, j))


    screen.blit(finish3,(80,80))
    if point_finish(stageplay3, fp1) == True:
        cheer.play()
        return True

    pygame.display.flip()
def mod2_stage4():
    pygame.init()
    screen.fill(GRAY)
    cheer = random.choice([cheer2, cheer1])
    fp1 = finishpoint(1160, 740, 20, 120, screen)
    for i in range(0,1200,128):
        for j in range(0,900,128):
            screen.blit(background,(i,j))
    nexon_free_font("stage 4", "", BLACK, 30, (370, 20), screen)
    stageplay4.draw(screen)
    stageplay4.head()
    stageplay4.move()
    wall1 = Wall(140, 40, 60, 360)
    crash_wall(stageplay4, wall1)
    wall2 = Wall(140, 500, 60, 360)
    crash_wall(stageplay4, wall2)
    wall3 = Wall(320, 140, 60, 600)
    crash_wall(stageplay4, wall3)
    wall4 = Wall(500, 0, 60, 280)
    crash_wall(stageplay4, wall4)
    wall5 = Wall(500, 640, 60, 340)
    crash_wall(stageplay4, wall5)
    wall6 = Wall(500, 360, 60, 200)
    crash_wall(stageplay4, wall6)
    wall7 = Wall(760, 0, 60, 420)
    crash_wall(stageplay4, wall7)
    wall8 = Wall(760, 460, 60, 500)
    crash_wall(stageplay4, wall8)
    wall9 = Wall(940, 0, 60, 280)
    crash_wall(stageplay4, wall9)
    wall10 = Wall(940, 640, 60, 340)
    crash_wall(stageplay4, wall10)
    wall11 = Wall(940, 360, 60, 200)
    crash_wall(stageplay4, wall11)
    wall12 = Wall(1060, 700, 160, 40)
    crash_wall(stageplay4,wall12)
    wall13 = Wall(1060, 860,160,40)
    crash_wall(stageplay4,wall13)
    for i in range(140, 200, 20):
        for j in range(40, 400, 20):
            screen.blit(tile, (i, j))

    for i in range(140, 200, 20):
        for j in range(500, 860, 20):
            screen.blit(tile, (i, j))

    for i in range(320, 380, 20):
        for j in range(140, 740, 20):
            screen.blit(tile, (i, j))

    for i in range(500, 560, 20):
        for j in range(0, 280, 20):
            screen.blit(tile, (i, j))

    for i in range(500, 560, 20):
        for j in range(640, 980, 20):
            screen.blit(tile, (i, j))

    for i in range(500, 560, 20):
        for j in range(360, 560, 20):
            screen.blit(tile, (i, j))

    for i in range(760, 820, 20):
        for j in range(0, 420, 20):
            screen.blit(tile, (i, j))

    for i in range(760, 820, 20):
        for j in range(460, 960, 20):
            screen.blit(tile, (i, j))

    for i in range(940, 1000, 20):
        for j in range(0, 280, 20):
            screen.blit(tile, (i, j))

    for i in range(940, 1000, 20):
        for j in range(640, 980, 20):
            screen.blit(tile, (i, j))

    for i in range(940, 1000, 20):
        for j in range(360, 560, 20):
            screen.blit(tile, (i, j))

    for i in range(1060, 1220, 20):
        for j in range(700, 740, 20):
            screen.blit(tile, (i, j))

    for i in range(1060, 1220, 20):
        for j in range(860, 900, 20):
            screen.blit(tile, (i, j))
    screen.blit(finishb,(1160,740))

    if point_finish(stageplay4, fp1) == True:
        cheer.play()
        time.sleep(0.4)
        success.play()
        return True
    pygame.display.flip()
def mod2_stage5():
    pygame.init()
    screen.fill(GRAY)
    cheer = random.choice([cheer2, cheer1])
    fp1 = finishpoint(720, 320, 100, 20, screen)
    for i in range(0,1200,128):
        for j in range(0,900,128):
            screen.blit(background,(i,j))
    nexon_free_font("stage 5", "", BLACK, 30, (400, 20), screen)
    stageplay5.draw(screen)
    stageplay5.head()
    stageplay5.move()
    wall1 = Wall(0, 0, 20, 900)
    crash_wall(stageplay5, wall1)
    wall2 = Wall(0, 880, 1200, 20)
    crash_wall(stageplay5, wall2)
    wall3 = Wall(1140, 0, 60, 900)
    crash_wall(stageplay5, wall3)
    wall4 = Wall(100, 0, 1120, 60)
    crash_wall(stageplay5, wall4)
    wall5 = Wall(100, 60, 40, 780)
    crash_wall(stageplay5, wall5)
    wall6 = Wall(100, 800, 960, 40)
    crash_wall(stageplay5, wall6)
    wall7 = Wall(1020, 120, 40, 720)
    crash_wall(stageplay5, wall7)
    wall8 = Wall(220, 100, 840, 40)
    crash_wall(stageplay5, wall8)
    wall9 = Wall(220, 100, 40, 660)
    crash_wall(stageplay5, wall9)
    wall10 = Wall(220, 720, 720, 40)
    crash_wall(stageplay5, wall10)
    wall11 = Wall(920, 180, 40, 580)
    crash_wall(stageplay5, wall11)
    wall12 = Wall(320, 180, 620, 40)
    crash_wall(stageplay5, wall12)
    wall13 = Wall(320, 180, 40, 500)
    crash_wall(stageplay5, wall13)
    wall14 = Wall(320, 640, 540, 40)
    crash_wall(stageplay5, wall14)
    wall15 = Wall(820, 260, 40, 420)
    crash_wall(stageplay5, wall15)
    wall16 = Wall(400, 260, 420, 40)
    crash_wall(stageplay5, wall16)
    wall17 = Wall(400, 260, 40, 340)
    crash_wall(stageplay5, wall17)
    wall18 = Wall(400, 560, 360, 40)
    crash_wall(stageplay5, wall18)
    wall19 = Wall(720, 340, 40, 220)
    crash_wall(stageplay5, wall19)

    for i in range(0, 20, 20):
        for j in range(0, 900, 20):
            screen.blit(tile, (i, j))

    for i in range(0, 1200, 20):
        for j in range(880, 900, 20):
            screen.blit(tile, (i, j))

    for i in range(1140, 1200, 20):
        for j in range(0, 900, 20):
            screen.blit(tile, (i, j))

    for i in range(100, 1220, 20):
        for j in range(0, 60, 20):
            screen.blit(tile, (i, j))

    for i in range(100, 140, 20):
        for j in range(60, 840, 20):
            screen.blit(tile, (i, j))

    for i in range(100, 1060, 20):
        for j in range(800, 840, 20):
            screen.blit(tile, (i, j))

    for i in range(1020, 1060, 20):
        for j in range(120, 840, 20):
            screen.blit(tile, (i, j))

    for i in range(220, 1060, 20):
        for j in range(100, 140, 20):
            screen.blit(tile, (i, j))

    for i in range(220, 260, 20):
        for j in range(100, 760, 20):
            screen.blit(tile, (i, j))

    for i in range(220, 940, 20):
        for j in range(720, 760, 20):
            screen.blit(tile, (i, j))

    for i in range(920, 960, 20):
        for j in range(180, 760, 20):
            screen.blit(tile, (i, j))

    for i in range(320, 940, 20):
        for j in range(180, 220, 20):
            screen.blit(tile, (i, j))

    for i in range(320, 360, 20):
        for j in range(180, 680, 20):
            screen.blit(tile, (i, j))

    for i in range(320, 860, 20):
        for j in range(640, 680, 20):
            screen.blit(tile, (i, j))

    for i in range(820, 860, 20):
        for j in range(260, 680, 20):
            screen.blit(tile, (i, j))

    for i in range(400, 820, 20):
        for j in range(260, 300, 20):
            screen.blit(tile, (i, j))

    for i in range(400, 440, 20):
        for j in range(260, 600, 20):
            screen.blit(tile, (i, j))

    for i in range(400, 760, 20):
        for j in range(560, 600, 20):
            screen.blit(tile, (i, j))

    for i in range(720, 760, 20):
        for j in range(340, 560, 20):
            screen.blit(tile, (i, j))


    screen.blit(finish5,(720,320))
    if point_finish(stageplay5, fp1) == True:
        cheer.play()
        return True
    pygame.display.flip()

def mod2_set_event(event):
    mousepos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if lockevent==[False,False,False,False]:
            if modstage1btn.isover(mousepos):
                return "press_stage1"
            if modstage2btn.isover(mousepos):
                locksound.play()
            if modstage3btn.isover(mousepos):
                locksound.play()
            if modstage4btn.isover(mousepos):
                locksound.play()
            if modstage5btn.isover(mousepos):
                locksound.play()
        if lockevent==[True,False,False,False]:
            if modstage1btn.isover(mousepos):
                return "press_stage1"
            if modstage2btn.isover(mousepos):
                return  "press_stage2"
            if modstage3btn.isover(mousepos):
                locksound.play()
            if modstage4btn.isover(mousepos):
                locksound.play()
            if modstage5btn.isover(mousepos):
                locksound.play()
        if lockevent==[True,True,False,False]:
            if modstage1btn.isover(mousepos):
                return "press_stage1"
            if modstage2btn.isover(mousepos):
                return  "press_stage2"
            if modstage3btn.isover(mousepos):
                return  "press_stage3"
            if modstage4btn.isover(mousepos):
                locksound.play()
            if modstage5btn.isover(mousepos):
                locksound.play()
        if lockevent==[True,True,True,False]:
            if modstage1btn.isover(mousepos):
                return "press_stage1"
            if modstage2btn.isover(mousepos):
                return "press_stage2"
            if modstage3btn.isover(mousepos):
                return "press_stage3"
            if modstage4btn.isover(mousepos):
                return "press_stage4"
            if modstage5btn.isover(mousepos):
                locksound.play()
        if lockevent==[True,True,True,True]:
            if modstage1btn.isover(mousepos):
                return "press_stage1"
            if modstage2btn.isover(mousepos):
                return "press_stage2"
            if modstage3btn.isover(mousepos):
                return "press_stage3"
            if modstage4btn.isover(mousepos):
                return "press_stage4"
            if modstage5btn.isover(mousepos):
                return "press_stage5"


class Stageplay(Player):
    # 상속받은 플레이어 클래스에서
    # 초기위치 부분 변경
    def __init__(self, x1, y1):

        self.x1 = x1
        self.y1 = y1
        self.color = GREEN
        self.create()

    def create(self):
        self.position = [((self.x1), (self.y1))]  # 초기위치
        self.direction = (DOWN)  # 시작방향 UP
        self.length = 3  # 길이

    # 이동 변경
    def move(self):
        selectsound=random.choice([deadso1,deadso2,deadso3,deadso4])
        cur = self.position[0]
        x, y = self.direction
        new = ((cur[0] + (x * PIXEL_SIZE)), (cur[1] + (y * PIXEL_SIZE)))
        if new in self.position[4:]:
            screen.blit(dead, (self.position[0][0], self.position[0][1]))
            selectsound.play()
            self.create()
        else:
            self.position.insert(0, new)  # 추가만 하고 삭제 안함

            if self.position[0][0] < 0 or self.position[0][0] > 1200 - PIXEL_SIZE:
                screen.blit(dead, (self.position[0][0], self.position[0][1]))
                selectsound.play()
                self.create()
            if self.position[0][1] < 0 or self.position[0][1] > 900 - PIXEL_SIZE:
                screen.blit(dead, (self.position[0][0], self.position[0][1]))
                selectsound.play()
                self.create()
    def head(self):
        if self.direction==(0,-1):
            newhead=pygame.transform.rotate(head,0)
            screen.blit(newhead,(self.position[0]))
        if self.direction==(0,1):
            newhead=pygame.transform.rotate(head,180)
            screen.blit(newhead,(self.position[0]))
        if self.direction==(1,0):
            newhead=pygame.transform.rotate(head,-90)
            screen.blit(newhead,(self.position[0]))
        if self.direction==(-1,0):
            newhead=pygame.transform.rotate(head,90)
            screen.blit(newhead,(self.position[0]))

# 스테이지 전용 플레이어 상속(
class Stageplay1(Player):
    # 상속받은 플레이어 클래스에서
    # 초기위치 부분 변경
    def __init__(self, x1, y1):

        self.x1 = x1
        self.y1 = y1
        self.color = GREEN
        self.create()

    def create(self):
        self.position = [((self.x1), (self.y1))]  # 초기위치
        self.direction = (UP)  # 시작방향 UP
        self.length = 3  # 길이

    # 이동 변경
    def move(self):
        cur = self.position[0]
        x, y = self.direction
        new = ((cur[0] + (x * PIXEL_SIZE)), (cur[1] + (y * PIXEL_SIZE)))
        selectsound=random.choice([deadso1,deadso2,deadso3,deadso4])
        if new in self.position[4:]:
            screen.blit(dead, (self.position[0][0], self.position[0][1]))
            selectsound.play()
            self.create()
        else:
            self.position.insert(0, new)  # 추가만 하고 삭제 안함

            if self.position[0][0] < 0 or self.position[0][0] > 1200 - PIXEL_SIZE:
                screen.blit(dead, (self.position[0][0], self.position[0][1]))
                selectsound.play()
                self.create()
            if self.position[0][1] < 0 or self.position[0][1] > 900 - PIXEL_SIZE:
                screen.blit(dead, (self.position[0][0], self.position[0][1]))
                selectsound.play()
                self.create()

    def head(self):
        if self.direction == (0, -1):
            newhead = pygame.transform.rotate(head, 0)
            screen.blit(newhead, (self.position[0]))
        if self.direction == (0, 1):
            newhead = pygame.transform.rotate(head, 180)
            screen.blit(newhead, (self.position[0]))
        if self.direction == (1, 0):
            newhead = pygame.transform.rotate(head, -90)
            screen.blit(newhead, (self.position[0]))
        if self.direction == (-1, 0):
            newhead = pygame.transform.rotate(head, 90)
            screen.blit(newhead, (self.position[0]))

# 벽클래스
class Wall(object):
    # 위치, 크기 값으로 생성
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = WHITE
        # 생성함수에 draw 함수 같이 실행
        self.draw()

    # 그리기
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))


# 도착지점
class finishpoint(object):
    # 위치,크기,표시할 화면 생성
    def __init__(self, x, y, w, h, su):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = BLUE
        self.su = su
        # 벽클래스와 같은 방식
        self.draw()

    # 그리기
    def draw(self):
        pygame.draw.rect(self.su, self.color, (self.x, self.y, self.w, self.h))
def crash_wall(p, w):
    if (p.position[0][0] > w.x - 20 and p.position[0][0] < w.x + w.w) and (p.position[0][1] > w.y - 20 and p.position[0][1] < w.y + w.h):
        # 플레이어 머리부분과 벽에 닿았을시 플레이어 리스폰
        screen.blit(dead, (p.position[0][0], p.position[0][1]))
        soundselect=random.choice([deadso1,deadso2,deadso3,deadso4])
        print(w.x,w.y)
        soundselect.play()
        p.create()
        score = 100
        return True
# 플레이어가 도착지점에 닿았는지 판단
def point_finish(sp, pf):
    # 닿았을시 True를 리턴
    if sp.position[0][0] > pf.x - 20 and sp.position[0][0] < pf.x + pf.w and sp.position[0][1] > pf.y - 20 and sp.position[0][1] < pf.y + pf.h:
        #backselect=random.choice([back2,back1])
        #backselect.play()
        return True

# 스테이지 플레이어 인스턴스
stageplay = Stageplay1(60, 900)
stageplay2 = Stageplay(60, 0)
stageplay3 = Stageplay(1100, 0)
stageplay4 = Stageplay1(60, 900)
stageplay5 = Stageplay(60, 0)