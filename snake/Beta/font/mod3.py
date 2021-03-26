import pygame
from event_class import nexon_free_font
from color import GRAY,RED,BLACK,YELLOW,ORANGE,GREEN,WHITE
from mod2 import Wall,crash_wall,finishpoint,point_finish
from set_mode import UP,PIXEL_SIZE,screen
from mod1 import Player
from image import pauseheader,menu,home,play,background
from button import mod3_stage1btn,mod3_stage2btn,mod3_stage3btn
score=200
clock=pygame.time.Clock()
def mod3_set_event(event):
    mousepos=pygame.mouse.get_pos()
    if mod3_stage1btn.isover(mousepos):
        return "press_mod3_stage1btn"
    if mod3_stage2btn.isover(mousepos):
        return "press_mod3_stage2btn"
    if mod3_stage3btn.isover(mousepos):
        return "press_mod3_stage3btn"
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
    pygame.init()

    screen.fill(GRAY)
    nexon_free_font("점수", str(score), BLACK, 50, (0, 0), screen)
    if score >= 180:
        nexon_free_font("등급", 'A', RED, 50, (0, 60), screen)

    elif score >= 160:
        nexon_free_font("등급", 'B', ORANGE, 50, (0, 60), screen)
    elif score >= 140:
        nexon_free_font("등급", 'C', YELLOW, 50, (0, 60), screen)
    elif score >= 120:
        nexon_free_font("등급", 'D', GREEN, 50, (0, 60), screen)
    else:
        nexon_free_font("등급", 'F', BLACK, 50, (0, 60), screen)
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

    gg = Wall(340, 300, 10, 600)
    gg1 = Wall(340, 300, 500, 10)
    gg2 = Wall(840, 300, 10, 500)
    gg3 = Wall(540, 500, 10, 500)
    if crash_wall(picplay1, gg) == True or crash_wall(picplay1, gg1) == True or crash_wall(picplay1,gg2) == True\
            or crash_wall(picplay1,gg3):
        score = 200
    if line_play(picplay1, line1) != True and line_play(picplay1, line2) != True and line_play(picplay1, line3) \
            != True and line_play(picplay1, line4) != True and line_play(picplay1, line5) != True and line_play( \
            picplay1, line6) != True and line_play(picplay1, line7) != True and line_play(picplay1,
                                                                                          line8) != True and \
            line_play(picplay1, line9) != True and line_play(picplay1, line10) != True:
        score -= 1

    st3_fin = finishpoint(360, 840, 20, 20, screen)
    if point_finish(picplay1, st3_fin) == True:

        if score >= 180:
            rank = 'A'
            color = RED
        elif score >= 160:
            rank = 'B'
            color = ORANGE
        elif score >= 140:
            rank = 'C'
            color = YELLOW
        elif score >= 120:
            rank = 'D'
            color = GREEN
        else:
            rank = 'F'
            color = BLACK
        return True
    picplay1.draw(screen)
    clock.tick(10)
    if picplay1.move() == True:
        score = 200


def mod3_stage2():
    global score
    pygame.init()

    screen.fill(GRAY)

    nexon_free_font("점수", str(score), BLACK, 50, (0, 0), screen)
    if score >= 180:
        nexon_free_font("등급", 'A', RED, 50, (0, 60), screen)

    elif score >= 160:
        nexon_free_font("등급", 'B', ORANGE, 50, (0, 60), screen)
    elif score >= 140:
        nexon_free_font("등급", 'C', YELLOW, 50, (0, 60), screen)
    elif score >= 120:
        nexon_free_font("등급", 'D', GREEN, 50, (0, 60), screen)
    else:
        nexon_free_font("등급", 'F', BLACK, 50, (0, 60), screen)
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
    gg = Wall(560, 180, 20, 840)

    if crash_wall(picplay, gg) == True:  # or crash_wall(picplay1,gg1)==True or crash_wall(picplay1,gg2)==True:
        score = 200
        print(2)
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

        if score >= 180:
            rank = 'A'
            color = RED
        elif score >= 160:
            rank = 'B'
            color = ORANGE
        elif score >= 140:
            rank = 'C'
            color = YELLOW
        elif score >= 120:
            rank = 'D'
            color = GREEN
        else:
            rank = 'F'
            color = BLACK
        return True
    picplay.draw(screen)
    clock.tick(10)
    if picplay.move() == True:
        score = 200
def mod3_stage3():
    global score
    pygame.init()

    screen.fill(GRAY)
    nexon_free_font("점수", str(score), BLACK, 50, (0, 0), screen)
    if score >= 180:
        nexon_free_font("등급", 'A', RED, 50, (0, 60), screen)
    elif score >= 160:
        nexon_free_font("등급", 'B', ORANGE, 50, (0, 60), screen)
    elif score >= 140:
        nexon_free_font("등급", 'C', YELLOW, 50, (0, 60), screen)
    elif score >= 120:
        nexon_free_font("등급", 'D', GREEN, 50, (0, 60), screen)
    else:
        nexon_free_font("등급", 'F', BLACK, 50, (0, 60), screen)

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
        mod3_stage3 = False
        mod3_suc_3 = True
        if score >= 180:
            rank = 'A'
            color = RED
        elif score >= 160:
            rank = 'B'
            color = ORANGE
        elif score >= 140:
            rank = 'C'
            color = YELLOW
        elif score >= 120:
            rank = 'D'
            color = GREEN
        else:
            rank = 'F'
            color = BLACK
    picplay2.draw(screen)

    gg = Wall(480, 440, 10, 600)

    gg1 = Wall(260, 440, 700, 10)

    gg2 = Wall(620, 140, 10, 560)
    clock.tick(10)
    if crash_wall(picplay2, gg) == True or crash_wall(picplay2, gg1) == True or crash_wall(picplay2,gg2) == True:
        score = 200
    if picplay2.move() == True:
        score = 200


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
        cur = self.position[0]
        x, y = self.direction
        new = ((cur[0] + (x * 20)), (cur[1] + (y * 20)))
        if new in self.position[3:]:
            self.create()
            return True
        else:
            self.position.insert(0, new)  # 추가만 하고 삭제 안함

            if self.position[0][0] < 0 or self.position[0][0] > 1200 - PIXEL_SIZE:
                self.create()

                return True

            if self.position[0][1] < 0 or self.position[0][1] > 900 - PIXEL_SIZE:
                self.create()
                return True




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
