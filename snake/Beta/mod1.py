import pygame
import random
from color import GREEN,RED,ORANGE,BLACK,GRAY,BLUE
from set_mode import UP,DOWN,LEFT,RIGHT,PIXEL_SIZE,PIXEL_HEIGHT,PIXEL_WIDTH,FPS,screen,barsurface,mainsurface,SCREEN_HEIGHT,SCREEN_WIDTH
from event_class import nexon_free_font
from image import dead,head,bomb,grass,menu,home,background,pauseheader,loadingtext,loadingem,loadingbar,food2,food1,tail,bomb_r
import image
from sound import deadso4,deadso3,deadso2,deadso1,missile,eat1,eat2,eat3,eat4,loading
from button import playbtn,menubtn,homebtn
import sys
import time
clock=pygame.time.Clock()

# 플레이어 클래스
class Player(object):
    # 생성 함수
    def __init__(self):
        # 플레이어 색지정
        self.color = GREEN
        self.create()


    # 리스폰시 위치 초기화
    def create(self):

        self.length = 2  # 초기 길이
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # 방향 랜덤
        self.position = [((400), (400))]  # 초기위치

    # 방향
    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1) == self.direction:  # 위-아래, 왼쪽 오른쪽으로 틀지 못함
            return
        else:
            # 아닐경우 방향 그대로 반영
            self.direction = xy

    # 이동
    def move(self):
        selectsound = random.choice([deadso1, deadso3, deadso2, deadso4])
        # 머리부분 좌표
        cur = self.position[0]
        # 방향좌표 x,y로 선언
        x, y = self.direction
        # 방향 * 픽셀사이즈
        new = ((cur[0] + (x * 20)), (cur[1] + (y * 20)))



        if new in self.position[3:]:  # 자기몸에 닿으면 리스폰
            screen.blit(dead, (self.position[0][0], self.position[0][1]))
            selectsound.play()
            self.create()

        else:
            self.position.insert(0, new)  # 아닐경우 길이 증가

            if len(self.position) > self.length:

                self.position.pop()  # 원래 길이보다 크면 젤 뒷부분 삭제 (큐 알고리즘)
            # 벽에 닿으면 죽음
            if self.position[0][0] < 0 or self.position[0][0] > 1200 - 20:
                screen.blit(dead,(self.position[0][0],self.position[0][1]))
                selectsound.play()

                self.create()

            if self.position[0][1] < 0 or self.position[0][1] > 700 - 20:
                screen.blit(dead,(self.position[0][0],self.position[0][1]))
                selectsound.play()
                self.create()
            # if self.direction==(-1,0):
            #     newimg=pygame.transform.rotate(head,90)
            #     screen.blit(newimg, (self.position[0][0], self.position[0][1]))
            # if self.direction==(1,0):
            #     newimg=pygame.transform.rotate(head,-90)
            #     screen.blit(newimg, (self.position[0][0], self.position[0][1]))
            # if self.direction==(0,1):
            #     newimg=pygame.transform.rotate(head,180)
            #     screen.blit(newimg, (self.position[0][0], self.position[0][1]))
            # if self.direction==(0,-1):
            #     newimg=pygame.transform.rotate(head,0)
            #     screen.blit(newimg, (self.position[0][0], self.position[0][1]))

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




    # eat
    def eat(self):
        # eat 함수 실행될때 뱀의 길이 1 증가
        pygame.mixer.Sound.play(random.choice([eat1, eat2, eat3, eat4]))
        self.length += 1

    # 객체 그리기
    def draw(self, su):
        # position 좌표 모두 불러옴
        for p in self.position:
            # draw_object 함수에 보냄
            draw_objects(su, self.color, p)

# 플레이어의 먹이 클래스
class Food(object):
    # 생성
    def __init__(self):
        self.color = RED
        self.create()

    # 리스폰
    def create(self):
        # create 함수가 실행될때 마다 랜덤한 위치에 먹이생성
        self.ranfood = random.choice([food1, food2])
        self.position = random.randint(2, PIXEL_WIDTH - 3) * PIXEL_SIZE, random.randint(2,PIXEL_HEIGHT - 3) * PIXEL_SIZE
        # random.randint(0, PIXEL_WIDTH - 1) * PIXEL_SIZE, random.randint(0, PIXEL_HEIGHT - 1) * PIXEL_SIZE
    # 그리기
    def draw(self, su):

        mainsurface.blit(self.ranfood,(self.position[0]-5,self.position[1]-5))

# 발사체 클래스
class Missile(object):

    def __init__(self):
        self.create()
    def create(self):

        self.x=-60

        self.direction = RIGHT

        self.y = random.choice([0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660])

        self.position=[self.x,self.y]

    def move(self):

        screen.blit(bomb,self.position)

        self.position[0]+=20
        if self.position[0]>1200:
            self.position[0]=0
            self.position[1]=random.choice([0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660])
            self.create()
            missile.play()

class RMissile(object):

    def __init__(self):
        self.create()
    def create(self):

        self.x=1200

        self.direction = LEFT

        self.y = random.choice([30, 90, 150, 210, 270, 330, 400, 460, 520, 580, 640, 680])

        self.position=[self.x,self.y]

    def move(self):

        screen.blit(bomb_r,self.position)

        self.position[0]-=20
        if self.position[0]<0:
            self.position[0]=1200
            self.position[1]=random.choice([0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660])
            self.create()
            missile.play()





# 플레이어가 먹이를 먹었는지 판단
def eat_food(p, f):
    if play.position[0] == food.position:
        # 플레이어 머리부분과 먹이 위치가 일치할시
        food.create()
        play.eat()
        # 먹이 재생성
        # 플레이어 클래스내에서 eat함수 불러옴
        # eat() => 플레이어 길이 1 증가
def crash_mis(p,m):

    selectsound = random.choice([deadso1, deadso3, deadso2, deadso4])
    if m.position[0]-20<play.position[0][0]<m.position[0]+60:
        if m.y==play.position[0][1]:
            screen.blit(dead, (play.position[0][0], play.position[0][1]))
            selectsound.play()
            m1.create()
            play.create()



# 도형그려줌
def draw_objects(su, co, pos):
    r = pygame.Rect((pos[0], pos[1]), (PIXEL_SIZE, PIXEL_SIZE))
    pygame.draw.rect(su, co, r)
play=Player()
food=Food()
m1=Missile()
m2=RMissile()
m3=Missile()
def mod1_play():
    pygame.init()

    # mainsurface와 barsurface screen에 삽입
    screen.blit(mainsurface, (0, 0))
    screen.blit(barsurface, (0, 700))
    # surface화면 배경 설정
    mainsurface.fill(GRAY)
    barsurface.fill(ORANGE)
    # for i in range(0,1200,256):
    #     for j in range(0,900,256):
    #         mainsurface.blit(grass,(i,j))
    # 플레이어 그리기
    play.draw(mainsurface)
    # 음식 그리기
    food.draw(mainsurface)
    # eat_food 참 거짓 여부확인
    eat_food(play, food)
    # 뱀길이와 speed는 정비례
    speed = (FPS + play.length)
    # 속도 반영
    clock.tick(speed)
    if speed>=18:
        speed=18
    play.head()
    # 플레이어 이동
    play.move()
    # 폰트
    print(speed)
    if play.length==4:
        m1.create()
        m2.create()
    if play.length>4:

        m1.move()
        crash_mis(play,m1)
    if play.length>15:
        m2.move()
        crash_mis(play,m2)
    print(len(play.position))
    nexon_free_font("길이 : ", play.length, BLACK, 40, (10, 0), barsurface)
    nexon_free_font("속도 : ", str(round(speed / 3, 2)), BLACK, 40, (10, 55), barsurface)
    nexon_free_font("종료하고 싶으면 esc키를 누르세요", "", BLACK, 20, (20, 150), barsurface)
    pygame.display.flip()


def mod1_event_key(event):
    if event.type == pygame.KEYDOWN:
        if event.key in [pygame.K_UP,pygame.K_w]:
            play.control(UP)
        if event.key in [pygame.K_DOWN,pygame.K_s]:
            play.control(DOWN)
        if event.key in [pygame.K_LEFT,pygame.K_a]:
            play.control(LEFT)
        if event.key in [pygame.K_RIGHT,pygame.K_d]:
            play.control(RIGHT)
        if event.key == pygame.K_ESCAPE:
            return True
def mod1_pause():
    pygame.init()
    for i in range(0,1400,256):
        for j in range(0,900,256):
            screen.blit(background,(i,j))
    screen.blit(pauseheader,(350,50))
    screen.blit(image.play,(200,350))
    screen.blit(home,(500,350))
    screen.blit(menu,(800,350))
    pygame.display.flip()

def mod1_pause_event(event):
    mousepos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
        if playbtn.isover(mousepos):
            return "press_playbtn"
        if menubtn.isover(mousepos):
            return  "press_menubtn"
        if homebtn.isover(mousepos):
            return  "press_homebtn"
x=-400
def mod1_load():

    global x

    screen.fill(0)

    for i in range(0, SCREEN_WIDTH, 256):
        for j in range(0, SCREEN_HEIGHT, 256):
            screen.blit(background, (i, j))
    screen.blit(loadingem, (250, 445))
    screen.blit(loadingtext, (500, 390))

    screen.blit(loadingbar, (x, 445))
    x += 20
    for i in range(-15, SCREEN_HEIGHT, 256):
        screen.blit(background, (0, i))
    if x > 265:
        screen.blit(loadingbar, (260, 445))
        x = 260
        loading.play()
        time.sleep(1)
        return True
    pygame.display.flip()