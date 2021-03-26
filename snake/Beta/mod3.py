import pygame
from set_mode import screen
from event_class import nexon_free_font
from color import GRAY,RED,BLACK,YELLOW,ORANGE,GREEN,WHITE
from mod2 import Wall,crash_wall,finishpoint,point_finish
from set_mode import UP,PIXEL_SIZE,SCREEN_WIDTH,SCREEN_HEIGHT
from mod1 import Player
from sound import loading
import time
from sound import deadso1,deadso3,deadso2,deadso4
from image import pauseheader,menu,home,play,background,mod3setpng,loadingtext,loadingbar,loadingem,load,tt
from image import building2,building1,building3,building4,building5,sun1,tree1,tree2,tree3,tree8,tree11,label
from image import building6,dead,rock1,rock2,rock3,rock4,rock5,decor,car,mount1,mount2,gasi,bone,grass2,eye,fire,head
import random

score=300
clock=pygame.time.Clock()
x=-400
def mod3_loading():
    global x
    pygame.init()
    for i in range(0, SCREEN_WIDTH, 256):
        for j in range(0, SCREEN_HEIGHT, 256):
            screen.blit(background, (i, j))

    screen.blit(loadingtext, (500, 390))

    screen.blit(load, (x, 445))

    x += 20

    for i in range(-15, SCREEN_HEIGHT, 256):
        screen.blit(background, (0, i))
    if x > 265:
        screen.blit(load, (260, 445))
        x = 260

        time.sleep(1)
        x = -400
        return True
    pygame.display.flip()
def mod3_set():
    screen.blit(mod3setpng,(0,0))
    pygame.display.flip()
def mod3_pause():
    pygame.init()
    screen.fill(GRAY)
    for i in range(0,1400,256):
        for j in range(0,900,256):
            screen.blit(background,(i,j))
    screen.blit(pauseheader,(350,50))
    screen.blit(play,(200,350))
    screen.blit(home,(500,350))
    screen.blit(menu,(800,350))
def mod3_stage1():
    global score

    wall0 = Wall(500, 500, 150, 150)
    wall1 = Wall(520, 660, 150, 150)
    wall2 = Wall(340, 20, 150, 150)
    wall3 = Wall(520, 390, 150, 150)
    wall4 = Wall(520, 20, 150, 150)
    gg2 = Wall(840, 300, 20, 500)
    gg3 = Wall(540, 500, 20, 500)
    gg1 = Wall(340, 300, 500, 20)
    gg = Wall(340, 300, 20, 600)
    for i in range(0,1200,256):
        for j in range(0,900,256):
            screen.blit(background,(i,j))
    screen.blit(label, (5, 5))
    nexon_free_font("점수 ", str(score), BLACK, 50, (25, 15), screen)
    if score >= 250:
        nexon_free_font("등급 ", 'A', RED, 50, (25, 70), screen)
    elif score >= 200:
        nexon_free_font("등급 ", 'B', ORANGE, 50, (25 , 70), screen)
    elif score >= 150:
        nexon_free_font("등급 ", 'C', YELLOW, 50, (25 , 70), screen)
    elif score >= 100:
        nexon_free_font("등급 ", 'D', GREEN, 50, (25 , 70), screen)
    else:
        nexon_free_font("등급 ", 'F', BLACK, 50, (25, 70), screen)

    line1 = Line(300, 200, 20, 660)
    line2 = Line(300, 200, 600, 20)
    line3 = Line(900, 200, 20, 660)
    line4 = Line(760, 840, 140, 20)
    line5 = Line(760, 360, 20, 500)
    line6 = Line(460, 340, 300, 20)
    line7 = Line(440, 360, 20, 500)
    line8 = Line(300, 840, 160, 20)
    line9 = Line(460, 360, 20, 20)
    line10 = Line(740, 360, 20, 20)


    for i in range(300,900,20):
        screen.blit(gasi,(340,i))

    for i in range(340,840,20):
        screen.blit(gasi,(i,300))

    for i in range(300,800,20):
        screen.blit(gasi,(840,i))

    for i in range(440,900,20):
        screen.blit(gasi,(540,i))

    screen.blit(building4,(500,500))#buil4 150 150
    screen.blit(building5,(520,660))#build 150 150
    screen.blit(building1,(340,20))#build1 150 150
    screen.blit(building6,(520,390))#build6 100 100
    screen.blit(building2,(520,20))#build2 150 150
    #screen.blit(building3,(530,360))
    # wall0 = Wall(500, 500, 150, 150)
    # wall1 = Wall(520, 660, 150, 150)
    # wall2 = Wall(340, 20, 150, 150)
    # wall3 = Wall(650, 230, 100, 100)
    # wall4 = Wall(520, 40, 150, 150)
    # wall5 = Wall(530,360,150,150)
    # screen.blit(sun1,(340,380))
    # screen.blit(rock1,(335,520))
    # screen.blit(decor,(325,650))
    #
    # screen.blit(tree2,(790,500))
    # screen.blit(car,(400,235))
    # screen.blit(mount1,(0,405))
    # screen.blit(mount2,(0,655))



    if crash_wall(picplay1, gg) == True or crash_wall(picplay1,wall0)==True or crash_wall(picplay1,wall1)==True or crash_wall(picplay1,wall2)==True or crash_wall(picplay1,wall3)==True or crash_wall(picplay1,wall4)==True \
            or crash_wall(picplay1, gg1) == \
    True or crash_wall(picplay1,gg2) == True or crash_wall(picplay1,gg3):
        score = 300
    if line_play(picplay1, line1) != True and line_play(picplay1, line2) != True and line_play(picplay1, line3) \
            != True and line_play(picplay1, line4) != True and line_play(picplay1, line5) != True and line_play( \
            picplay1, line6) != True and line_play(picplay1, line7) != True and line_play(picplay1,
                                                                                          line8) != True and \
            line_play(picplay1, line9) != True and line_play(picplay1, line10) != True :
        score -= 1

    st3_fin = finishpoint(360, 840, 20, 20, screen)
    if point_finish(picplay1, st3_fin) == True:

        if score >= 250:
            rank = 'A'
            color = RED
        elif score >= 200:
            rank = 'B'
            color = ORANGE
        elif score >= 150:
            rank = 'C'
            color = YELLOW
        elif score >= 100:
            rank = 'D'
            color = GREEN
        else:
            rank = 'F'
            color = BLACK
        return rank

    picplay1.draw(screen)
    clock.tick(12)
    if picplay1.move() == True:
        score = 300
    picplay1.head()
    pygame.display.flip()


def mod3_stage2():
    global score

    gg = Wall(560, 180, 20, 840)
    wall0 = Wall(400, 420, 100, 160)
    wall1 = Wall(640, 700, 150, 150)
    wall2 = Wall(560, 410, 150, 150)
    wall3 = Wall(440, 300, 122, 94)
    wall4 = Wall(420, 510, 84, 73)
    for i in range(0, 1200, 256):
        for j in range(0, 900, 256):
            screen.blit(background, (i, j))
    screen.blit(label, (5, 5))
    nexon_free_font("점수 ", str(score), BLACK, 50, (25, 15), screen)
    if score >= 250:
        nexon_free_font("등급 ", 'A', RED, 50, (25, 70), screen)
    elif score >= 200:
        nexon_free_font("등급 ", 'B', ORANGE, 50, (25, 70), screen)
    elif score >= 150:
        nexon_free_font("등급 ", 'C', YELLOW, 50, (25, 70), screen)
    elif score >= 100:
        nexon_free_font("등급 ", 'D', GREEN, 50, (25, 70), screen)
    else:
        nexon_free_font("등급 ", 'F', BLACK, 50, (25, 70), screen)
    line1 = Line(500, 600, 20, 320)
    line2 = Line(260, 600, 240, 20)
    line3 = Line(260, 420, 20, 180)
    line4 = Line(260, 400, 140, 20)
    line5 = Line(400, 240, 20, 180)
    line6 = Line(400, 220, 100, 20)
    line7 = Line(500, 140, 20, 100)
    line8 = Line(520, 140, 100, 20)
    line9 = Line(620, 140, 20, 100)
    line10 = Line(620, 220, 100, 20)
    line11 = Line(720, 220, 20, 180)
    line12 = Line(720, 400, 100, 20)
    line13 = Line(820, 400, 20, 220)
    line14 = Line(620, 600, 200, 20)
    line15 = Line(620, 600, 20, 300)
    screen.blit(tree2,(400,420))#tree2 100 160
    screen.blit(tree1,(640,700))#tree1 150 150
    screen.blit(tree3,(590,410))#tree3 150 150
    screen.blit(bone,(440,300))#bone 122 94
    screen.blit(grass2,(420,510))#grass2 84 73
    for i in  range(180,900,20):
        screen.blit(gasi,(560,i))

    if crash_wall(picplay, gg) == True or crash_wall(picplay,wall0)==True or crash_wall(picplay,wall1)==True or \
            crash_wall(picplay,wall2)==True or crash_wall(picplay,wall3)==True or crash_wall(picplay,wall4)==True:  # or crash_wall(picplay1,gg1)==True or crash_wall(picplay1,gg2)==True:
        score = 300

    if line_play(picplay, line1) != True and line_play(picplay, line2) != True and line_play(picplay, line3) \
            != True and line_play(picplay, line4) != True and line_play(picplay, line5) != True and line_play( \
            picplay, line6) != True and line_play(picplay, line7) != True and line_play(picplay,
                                                                                        line8) != True and \
            line_play(picplay, line9) != True and line_play(picplay, line10) != True and line_play(picplay,
                                                                                                   line11) != True \
            and line_play(picplay, line12) != True and line_play(picplay, line13) != True and line_play(picplay,
                                                                                                        line14) != True \
            and line_play(picplay, line15) != True:
        score -= 1
    st3_fin = finishpoint(620, 880, 20, 20, screen)
    if point_finish(picplay, st3_fin) == True:
        if score >= 250:
            rank = 'A'
        elif score >= 200:
            rank = 'B'
        elif score >= 150:
            rank = 'C'
        elif score >= 100:
            rank = 'D'
        else:
            rank = 'F'
        return rank

    picplay.draw(screen)
    clock.tick(11)
    if picplay.move() == True:
        score = 300
    picplay.head()
    pygame.display.flip()
def mod3_stage3():
    global score

    gg = Wall(480, 440, 20, 600)
    gg1 = Wall(260, 440, 700, 20)
    gg2 = Wall(620, 140, 20, 560)
    wall0 = Wall(500, 200, 50, 50)
    wall1 = Wall(620, 700, 50, 50)
    wall2 = Wall(320,760,100,100)
    for i in range(0,1200,256):
        for j in range(0,900,256):
            screen.blit(background,(i,j))
    screen.blit(label, (5, 5))
    nexon_free_font("점수 ", str(score), BLACK, 50, (25, 15), screen)
    if score >= 250:
        nexon_free_font("등급 ", 'A', RED, 50, (25, 70), screen)

    elif score >= 200:
        nexon_free_font("등급 ", 'B', ORANGE, 50, (25, 70), screen)
    elif score >= 150:
        nexon_free_font("등급 ", 'C', YELLOW, 50, (25, 70), screen)
    elif score >= 100:
        nexon_free_font("등급 ", 'D', GREEN, 50, (25, 70), screen)
    else:
        nexon_free_font("등급 ", 'F', BLACK, 50, (25, 70), screen)

    line1 = Line(420, 600, 20, 360)
    line2 = Line(280, 600, 160, 20)
    line13 = Line(260, 580, 20, 40)
    line3 = Line(200, 360, 20, 180)
    line14 = Line(200, 520, 40, 20)
    line15 = Line(220, 520, 20, 40)
    line16 = Line(220, 560, 60, 20)
    line4 = Line(280, 280, 160, 20)
    line17 = Line(200, 340, 40, 20)
    line18 = Line(220, 320, 20, 40)
    line19 = Line(240, 300, 20, 40)
    line20 = Line(260, 280, 20, 40)
    line5 = Line(420, 140, 20, 160)
    line21 = Line(420, 120, 40, 20)
    line22 = Line(440, 100, 40, 20)
    line23 = Line(460, 80, 40, 20)
    line24 = Line(480, 60, 60, 20)
    line6 = Line(980, 360, 20, 180)
    line25 = Line(660, 60, 60, 20)
    line26 = Line(700, 80, 40, 20)
    line27 = Line(720, 100, 40, 20)
    line28 = Line(740, 120, 40, 20)
    line7 = Line(760, 140, 20, 160)
    line8 = Line(520, 40, 160, 20)
    line9 = Line(520, 840, 160, 20)
    line10 = Line(760, 600, 20, 160)
    line29 = Line(920, 280, 20, 40)
    line30 = Line(940, 300, 20, 40)
    line31 = Line(960, 320, 20, 40)
    line32 = Line(980, 340, 20, 20)
    line11 = Line(760, 600, 160, 20)
    line32 = Line(960, 540, 40, 20)
    line33 = Line(940, 560, 40, 20)
    line34 = Line(900, 580, 60, 20)
    line12 = Line(760, 280, 160, 20)
    line35 = Line(740, 740, 40, 20)
    line36 = Line(740, 760, 20, 40)
    line37 = Line(720, 780, 40, 20)
    line38 = Line(720, 800, 20, 20)
    line39 = Line(720, 800, 20, 20)
    line40 = Line(700, 800, 20, 40)
    line41 = Line(660, 820, 40, 20)

    if line_play(picplay2, line1) != True and line_play(picplay2, line2) != True and line_play(picplay2,
                                                                                               line3) != True and \
            line_play(picplay2, line4) != True and line_play(picplay2, line5) != True and line_play(picplay2,
                                                                                                    line6) != True \
            and line_play(picplay2, line7) != True and line_play(picplay2, line8) != True and line_play(
        picplay2, line9) != \
            True and line_play(picplay2, line10) != True and line_play(picplay2, line11) != True and line_play(
        picplay2, line12) \
            != True and line_play(picplay2, line13) != True and line_play(picplay2,
                                                                          line14) != True and line_play(
        picplay2, line15) \
            != True and line_play(picplay2, line16) != True and line_play(picplay2,
                                                                          line17) != True and line_play(
        picplay2, line18) \
            != True and line_play(picplay2, line19) != True and line_play(picplay2,
                                                                          line20) != True and line_play(
        picplay2, line21) \
            != True and line_play(picplay2, line22) != True and line_play(picplay2,
                                                                          line23) != True and line_play(
        picplay2, line24) \
            != True and line_play(picplay2, line25) != True and line_play(picplay2,
                                                                          line26) != True and line_play(
        picplay2, line27) \
            != True and line_play(picplay2, line28) != True and line_play(picplay2,
                                                                          line29) != True and line_play(
        picplay2, line30) \
            != True and line_play(picplay2, line31) != True and line_play(picplay2,
                                                                          line32) != True and line_play(
        picplay2, line33) \
            != True and line_play(picplay2, line34) != True and line_play(picplay2,
                                                                          line35) != True and line_play(
        picplay2, line36) \
            != True and line_play(picplay2, line37) != True and line_play(picplay2,
                                                                          line38) != True and line_play(
        picplay2, line39) \
            != True and line_play(picplay2, line40) != True and line_play(picplay2, line41) != True:
        score -= 1

    st3_fin = finishpoint(520, 800, 20, 120, screen)
    if point_finish(picplay2, st3_fin) == True:
        if score >= 250:
            rank = 'A'
            color = RED
        elif score >= 200:
            rank = 'B'
            color = ORANGE
        elif score >= 150:
            rank = 'C'
            color = YELLOW
        elif score >= 100:
            rank = 'D'
            color = GREEN
        else:
            rank = 'F'
            color = BLACK
        return rank

    picplay2.draw(screen)
    for i in range(440,900,20):
        screen.blit(gasi,(480,i))

    for i in range(260,960,20):
        screen.blit(gasi,(i,440))

    for i in range(140,700,20):
        screen.blit(gasi,(620,i))


    pygame.draw.rect(screen,BLACK,(440, 440, 340, 20))
    pygame.draw.rect(screen,BLACK,(760, 300, 20, 140))
    pygame.draw.rect(screen,BLACK,(440, 280, 140, 20))
    pygame.draw.rect(screen,BLACK,(620, 600, 140, 20))
    screen.blit(eye,(500,200))#eye 50 50
    screen.blit(eye,(620,700))
    screen.blit(fire,(320,760))#fire 100 100

    clock.tick(11)
    if crash_wall(picplay2, gg) == True or crash_wall(picplay2,wall0)==True or crash_wall(picplay2,wall1)==True or \
    crash_wall(picplay2,wall2)==True or crash_wall(picplay2, gg1) == True or crash_wall(picplay2,gg2) == True:
        score = 300
    if picplay2.move() == True:
        score = 300
    picplay2.head()
    pygame.draw.rect(screen, BLACK, (420, 440, 20, 160))

    pygame.display.flip()


class Picplayer(Player):
    global score

    def __init__(self, x, y):
        self.color = GREEN
        self.x = x
        self.y = y
        self.create()

    def create(self):
        self.length = 2  # 초기 길이
        self.direction = UP  # 방향 랜덤
        self.position = [((self.x), (self.y))]  # 초기위치

    def move(self):
        selectsound = random.choice([deadso1, deadso3, deadso2, deadso4])

        cur = self.position[0]
        x, y = self.direction
        new = ((cur[0] + (x * 20)), (cur[1] + (y * 20)))
        if new in self.position[3:]:
            screen.blit(dead, (self.position[0][0], self.position[0][1]))
            selectsound.play()
            self.create()
            return True
        else:
            self.position.insert(0, new)  # 추가만 하고 삭제 안함

            if self.position[0][0] < 0 or self.position[0][0] > 1200 - PIXEL_SIZE:
                screen.blit(dead, (self.position[0][0], self.position[0][1]))
                selectsound.play()
                self.create()

                return True

            if self.position[0][1] < 0 or self.position[0][1] > 900 - PIXEL_SIZE:
                self.create()
                return True
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




class Line(object):
    def __init__(self, x, y, w, h):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.w, self.h))


# 플레이어와 벽이 닿았는지 판단



def line_play(p, l):
    if (p.position[0][0] > l.x - 20 and p.position[0][0] < l.x + l.w) and (
            p.position[0][1] > l.y - 20 and p.position[0][1] < l.y + l.h):
        return True

picplay1 = Picplayer(300, 840)
picplay = Picplayer(500, 900)
picplay2 = Picplayer(420, 880)
