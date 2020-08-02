# 해당모듈 임포트
import pygame
import time
import random
import sys

# 전체화면 사이즈
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

# 메인화면 사이즈
MAIN_SURFACE_WIDTH = 1200
MAIN_SURFACE_HEIGHT = 700

# 픽셀 사이즈
PIXEL_SIZE = 20
PIXEL_WIDTH = MAIN_SURFACE_WIDTH / PIXEL_SIZE
PIXEL_HEIGHT = MAIN_SURFACE_HEIGHT / PIXEL_SIZE

# 색상코드
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
ORANGE = (255, 123, 0)
BLUE = (0, 0, 255)
YELLOW = (150, 150, 0)
intro = (243,246,248)
# 방향
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 속도
FPS = 11

# 화면구성

# 시작화면 및 모드선택화면
startscreen = True
selectmode = False
howtoplayscreen = False
# 모드1
mode1 = False
# 모드2
mode2_set = False
mode2_stage_1 = False
mode2_stage_2 = False
mode2_stage_3 = False
mode2_stage_4 = False
mode2_stage_5 = False
# 모드3
mod3_set = False
mod3_stage1 = False
mod3_stage2 = False
mod3_stage3 = False
# 일시정지화면 및 로딩중 화면
pause_screen = False
roading_screen = False
mod2_pause_screen = False
mod3_pause_screen = False
mod2_roading_screen = False
mod3_roading_screen = False
# 게임성공 화면
game_success_1 = False
game_success_2 = False
game_success_3 = False
game_success_4 = False
# stage 3
mod3_suc_1 = False
mod3_suc_2 = False
mod3_suc_3 = False
# 엔딩
ending_credit = False
mod1_dead = False
introscreen = False

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
        # 머리부분 좌표
        cur = self.position[0]
        # 방향좌표 x,y로 선언
        x, y = self.direction
        # 방향 * 픽셀사이즈
        new = ((cur[0] + (x * 20)), (cur[1] + (y * 20)))
        if new in self.position[3:]:  # 자기몸에 닿으면 리스폰
            self.create()

        else:
            self.position.insert(0, new)  # 아닐경우 길이 증가

            if len(self.position) > self.length:
                self.position.pop()  # 원래 길이보다 크면 젤 뒷부분 삭제 (큐 알고리즘)
            # 벽에 닿으면 죽음
            if self.position[0][0] < 0 or self.position[0][0] > 1200 - 20:
                self.create()

            if self.position[0][1] < 0 or self.position[0][1] > 700 - 20:
                self.create()

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


# 스테이지 전용 플레이어 상속(
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
        cur = self.position[0]
        x, y = self.direction
        new = ((cur[0] + (x * PIXEL_SIZE)), (cur[1] + (y * PIXEL_SIZE)))
        if new in self.position[3:]:
            self.create()
        else:
            self.position.insert(0, new)  # 추가만 하고 삭제 안함

            if self.position[0][0] < 0 or self.position[0][0] > 1200 - PIXEL_SIZE:
                self.create()
            if self.position[0][1] < 0 or self.position[0][1] > 900 - PIXEL_SIZE:
                self.create()


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
        if new in self.position[3:]:
            self.create()
        else:
            self.position.insert(0, new)  # 추가만 하고 삭제 안함

            if self.position[0][0] < 0 or self.position[0][0] > 1200 - PIXEL_SIZE:
                self.create()
            if self.position[0][1] < 0 or self.position[0][1] > 900 - PIXEL_SIZE:
                self.create()


class Picplayer(Stageplay):
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


# 플레이어의 먹이 클래스
class Food(object):
    # 생성
    def __init__(self):
        self.color = RED
        self.create()

    # 리스폰
    def create(self):
        # create 함수가 실행될때 마다 랜덤한 위치에 먹이생성

        self.position = random.randint(1, PIXEL_WIDTH - 2) * PIXEL_SIZE, random.randint(1,
                                                                                        PIXEL_HEIGHT - 2) * PIXEL_SIZE
        # random.randint(0, PIXEL_WIDTH - 1) * PIXEL_SIZE, random.randint(0, PIXEL_HEIGHT - 1) * PIXEL_SIZE

    # 그리기
    def draw(self, su):
        draw_objects(su, self.color, self.position)


# 벽클래스
class Wall(object):
    # 위치, 크기 값으로 생성
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = BLACK
        # 생성함수에 draw 함수 같이 실행
        self.draw()

    # 그리기
    def draw(self):
        pygame.draw.rect(screen,self.color, (self.x, self.y, self.w, self.h))


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


# 버튼클래스
class Button(object):
    # 위치 크기 생성
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # 마우스 좌표값 불러와서 생성한 버튼내에 마우스좌표가 들어가있는지 판단
    def isover(self, p):
        if self.x < p[0] and p[0] < self.x + self.w:
            if self.y < p[1] and p[1] < self.y + self.h:
                # 마우스 좌표가 버튼 범위 내에 들어있으면 True 리턴
                return True

    # 그리기
    def draw(self, su, co):
        pygame.draw.rect(su, co, (self.x, self.y, self.w, self.h))


# 발사체 클래스
class Missile(object):
    # 미완성
    def __init__(self):
        self.color = BLACK
        self.create()

    def create(self):
        self.position = [(0, 400)]
        self.direction = RIGHT
        self.move()

    def move(self):
        cur = self.position[0]
        x, y = self.direction
        new = ((cur[0] + (x * PIXEL_SIZE)), (cur[1] + (y * PIXEL_SIZE)))
        clock.tick(20)
        print(x,y)
        if new in self.position[3:]:
            self.create()
        else:
            self.position.insert(0, new)
            self.position.pop()
            if cur[0]>1200:
                self.create()

    def draw(self, su):
        for p in self.position:
            draw_objects(su, self.color, p)


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
def crash_wall(p, w):
    if (p.position[0][0] > w.x - 20 and p.position[0][0] < w.x + w.w) and (
            p.position[0][1] > w.y - 20 and p.position[0][1] < w.y + w.h):
        # 플레이어 머리부분과 벽에 닿았을시 플레이어 리스폰

        p.create()
        score=100
        return True


def line_play(p, l):
    if (p.position[0][0] > l.x - 20 and p.position[0][0] < l.x + l.w) and (
            p.position[0][1] > l.y - 20 and p.position[0][1] < l.y + l.h):
        return True


# 플레이어가 도착지점에 닿았는지 판단
def point_finish(sp, pf):
    # 닿았을시 True를 리턴
    if sp.position[0][0] > pf.x - 20 and sp.position[0][0] < pf.x + pf.w and sp.position[0][1] > pf.y - 20 and sp.position[0][1] < pf.y + pf.h:
        return True


# 플레이어가 먹이를 먹었는지 판단
def eat_food(p, f):
    if play.position[0] == food.position:
        # 플레이어 머리부분과 먹이 위치가 일치할시
        food.create()
        play.eat()
        # 먹이 재생성
        # 플레이어 클래스내에서 eat함수 불러옴
        # eat() => 플레이어 길이 1 증가
def crash_mi(p,m):
    if (p.position[0] ==m.position):
        # 플레이어 머리부분과 벽에 닿았을시 플레이어 리스폰

        p.create()
# 도형그려줌
def draw_objects(su, co, pos):
    r = pygame.Rect((pos[0], pos[1]), (PIXEL_SIZE, PIXEL_SIZE))
    pygame.draw.rect(su, co, r, 3)


# 폰트 클래스:
# 문자열,변수,글자색,글자크기,글자위치,표시화면
def hansin_font(var_m, var_a, txt_color, txt_size, po, su):
    font = pygame.font.Font("font/Maplestory Bold.ttf", txt_size)
    text = font.render(var_m + str(var_a), 1, txt_color)
    pos = text.get_rect()
    su.blit(text, (po[0], po[1]))


def change(mainsc, survesc):
    mainsc = False
    survesc = True


# 메인함수
if __name__ == "__main__":
    # 메인화면 생성(screen)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 화면 레이아웃 설정 => mainsurface
    # 주 화면
    mainsurface = pygame.Surface((MAIN_SURFACE_WIDTH, MAIN_SURFACE_HEIGHT))
    mainsurface = mainsurface.convert()
    mainsurface.fill(GRAY)
    # 화면 레이아웃 설정 => barsurface
    # 상태 화면
    barsurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - MAIN_SURFACE_HEIGHT))
    barsurface = barsurface.convert()
    barsurface.fill(ORANGE)
    # 화면 레이아웃 설정 => fullsurface
    fullsurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fullsurface = fullsurface.convert()
    fullsurface.fill(GRAY)
    i1=0
    # screen 흰색으로 칠함
    screen.fill(WHITE)

    # 버튼 클래스의 인스턴스 생성

    mod1btn = Button(100, 50, 1000, 400)
    mod2btn = Button(100, 450, 450, 400)
    mod3btn = Button(650, 450, 450, 400)
    modstage1btn = Button(40, 381, 168, 168)
    modstage2btn = Button(278, 381, 168, 168)
    modstage3btn = Button(510, 381, 168, 168)
    modstage4btn = Button(744, 381, 168, 168)
    modstage5btn = Button(979, 381, 168, 168)
    gameplaybtn = Button(415, 450, 370, 90)
    howtoplaybtn = Button(415, 640, 370, 90)
    returnbtn = Button(910, 800, 100, 40)
    mod3_stage1btn = Button(215, 260, 308, 289)
    mod3_stage2btn = Button(655, 267, 308, 289)
    mod3_stage3btn = Button(431, 581, 308, 289)
    backbtn = Button(1000, 700, 75, 75)
    mod3backbtn = Button(50,600,228,243)
    mod3nextbtn = Button(730,600,304,184)
    home = Button(700, 400, 150, 150)
    resume = Button(400, 400, 150, 150)
    # 캡션이름
    pygame.display.set_caption("Team WhileSucced")
    jongno=pygame.image.load("img/jongno.jpg")
    pygame.display.set_icon(jongno)
    # 이미지 로드
    modestagepng = pygame.image.load("img/stagemod.png")
    homekey = pygame.image.load("img/homekey.png")
    pausekey = pygame.image.load("img/pausekey.png")
    perfectmod = pygame.image.load("img/perfectmod.png")
    homescreen = pygame.image.load("img/homescreen.png")
    backkey = pygame.image.load("img/backkey.png")
    backkey = pygame.transform.scale(backkey, (75, 75))
    nextkey = pygame.image.load("img/next.png")
    returnkey = pygame.image.load("img/back.png")
    icon = pygame.image.load("img/icon.png")
    howtopg = pygame.image.load("img/howtoplay.png")
    icon = pygame.transform.scale(icon,(800,800))
    tree = pygame.image.load("img/tree.png")
    tree = pygame.transform.scale(tree,(1600,900))
    star = pygame.image.load("img/star.png")
    star = pygame.transform.scale(star,(30,30))
    blackstar = pygame.image.load("img/blackstar.png")
    blackstar = pygame.transform.scale(blackstar,(30,30))
    introjongno = pygame.image.load("img/introjongno.png")
    introjongno = pygame.transform.scale(introjongno,(1020,400))
    theend = pygame.image.load("img/thend.png")
    pygame.mixer.init(124110)
    eat1 = pygame.mixer.Sound("sound/eat1.wav")
    eat2 = pygame.mixer.Sound("sound/eat2.wav")
    eat3 = pygame.mixer.Sound("sound/eat3.wav")
    eat4 = pygame.mixer.Sound("sound/eat4.wav")
    pygame.mixer.music.load("sound/main.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    # 플레이어 인스턴스
    play = Player()
    # 음식 인스턴스
    food = Food()
    # 점수
    score = 200
    # 스테이지 플레이어 인스턴스
    stageplay = Stageplay1(60, 900)
    stageplay2 = Stageplay(60, 0)
    stageplay3 = Stageplay(1100, 0)
    stageplay4 = Stageplay1(60, 900)
    stageplay5 = Stageplay(60,0)

    picplay1 = Picplayer(300, 840)
    picplay = Picplayer(500, 900)
    picplay2 = Picplayer(420,880)
    # 프레임
    clock = pygame.time.Clock()
    # 파이게임 초기화
    pygame.init()
    # 발사체 인스턴스
    m1 = Missile()
    ongame = True
    # 무한루프
    while ongame:
        # 마우스 좌표값 불러옴
        mousepos = pygame.mouse.get_pos()
        # 이벤트가 실행되었을때
        for event in pygame.event.get():
            # 종료버튼누르면 종료
            if event.type == pygame.QUIT:
                ongame = False
                pygame.quit()
                sys.exit()
            # 키보드를 눌렀을때 이벤트 처리
            if event.type == pygame.KEYDOWN:
                # 현재 화면이 mode1일때
                if mode1 == True:
                    # 플레이어 클래스에서 방향값 리턴
                    # wads 와 방향키 둘다 사용
                    if event.key in [pygame.K_w, pygame.K_UP]:
                        play.control(UP)
                    if event.key in [pygame.K_a, pygame.K_LEFT]:
                        play.control(LEFT)
                    if event.key in [pygame.K_s, pygame.K_DOWN]:
                        play.control(DOWN)
                    if event.key in [pygame.K_d, pygame.K_RIGHT]:
                        play.control(RIGHT)
                    if event.key == pygame.K_q:
                        # 일시정지 화면
                        # 현재 화면 False로 바꾼후
                        # pasue_screnn 은 True 로 바꿈
                        mode1 = False
                        pause_screen = True
                # 현재 화면이 mode2_set일때
                if mode2_set == True:
                    # 미완성
                    if event.key == pygame.K_SPACE:
                        mode2_set = False
                        mode2_stage_1 = True
                # 현재 화면이 mode2_stage_1일때

                # mod2의 모든 스테이지에서 적용됨
                if mode2_stage_1 == True or mode2_stage_2 == True or mode2_stage_3 == True or mode2_stage_4 == True or mode2_stage_5 == True:
                    # 방향값을 스테이지 플레이어 클래스에 리턴
                    if event.key in [pygame.K_w, pygame.K_UP]:
                        stageplay.control(UP)
                        stageplay2.control(UP)
                        stageplay3.control(UP)
                        stageplay4.control(UP)
                        stageplay5.control(UP)
                    if event.key in [pygame.K_a, pygame.K_LEFT]:
                        stageplay.control(LEFT)
                        stageplay2.control(LEFT)
                        stageplay3.control(LEFT)
                        stageplay4.control(LEFT)
                        stageplay5.control(LEFT)
                    if event.key in [pygame.K_s, pygame.K_DOWN]:
                        stageplay.control(DOWN)
                        stageplay2.control(DOWN)
                        stageplay3.control(DOWN)
                        stageplay4.control(DOWN)
                        stageplay5.control(DOWN)
                    if event.key in [pygame.K_d, pygame.K_RIGHT]:
                        stageplay.control(RIGHT)
                        stageplay2.control(RIGHT)
                        stageplay3.control(RIGHT)
                        stageplay4.control(RIGHT)
                        stageplay5.control(RIGHT)
                    if event.key == pygame.K_q:
                        if mode2_stage_1 == True:
                            mode2_stage_1=False
                            mod2_pause_screen=True
                            a=1

                        if mode2_stage_2 == True:
                            mode2_stage_2=False
                            mod2_pause_screen=True
                            a=2
                        if mode2_stage_3 == True:
                            mode2_stage_3=False
                            mod2_pause_screen=True
                            a=3
                        if mode2_stage_4 == True:
                            mode2_stage_4=False
                            mod2_pause_screen=True
                            a=4
                        if mode2_stage_5 ==True:
                            mode2_stage_5=False
                            mod2_pause_screen=True
                            a=5

                if mod3_stage1 == True or mod3_stage2 == True or mod3_stage3 == True:
                    if event.key in [pygame.K_w, pygame.K_UP]:
                        picplay.control(UP)
                        picplay1.control(UP)
                        picplay2.control(UP)
                    if event.key in [pygame.K_a, pygame.K_LEFT]:
                        picplay.control(LEFT)
                        picplay1.control(LEFT)
                        picplay2.control(LEFT)
                    if event.key in [pygame.K_s, pygame.K_DOWN]:
                        picplay.control(DOWN)
                        picplay1.control(DOWN)
                        picplay2.control(DOWN)
                    if event.key in [pygame.K_d, pygame.K_RIGHT]:
                        picplay.control(RIGHT)
                        picplay1.control(RIGHT)
                        picplay2.control(RIGHT)
                    if event.key == pygame.K_q:
                        if mod3_stage1 == True:
                            mod3_stage1=False
                            mod3_pause_screen=True
                            b=1

                        if mod3_stage2 == True:
                            mod3_stage2=False
                            mod3_pause_screen=True
                            b=2
                        if mod3_stage3 == True:
                            mod3_stage3=False
                            mod3_pause_screen=True


                # 스테이지모드에서 성공했을때
                if game_success_1 == True:
                    if event.key == pygame.K_SPACE:
                        game_success_1 = False
                        mode2_stage_2 = True
                        stageplay.create()
                    if event.key == pygame.K_a:
                        game_success_1 = False
                        startscreen = True
                        stageplay.create()
                if game_success_2 == True:
                    if event.key == pygame.K_SPACE:
                        game_success_2 = False
                        mode2_stage_3 = True
                        stageplay.create()
                    if event.key == pygame.K_a:
                        game_success_2 = False
                        startscreen = True
                        stageplay.create()
                if game_success_3 == True:
                    if event.key == pygame.K_SPACE:
                        game_success_3 = False
                        mode2_stage_4 = True
                        stageplay.create()
                    if event.key == pygame.K_a:
                        game_success_3 = False
                        startscreen = True
                        stageplay.create()
                if game_success_4 == True:
                    if event.key == pygame.K_SPACE:
                        game_success_4 = False
                        mode2_stage_5 = True
                        stageplay.create()
                    if event.key == pygame.K_a:
                        game_success_4 = False
                        startscreen = True
                        stageplay.create()
                if mod1_dead == True:
                    if event.key == pygame.K_r:
                        mod1_dead = False
                        mode1 = True

                if mod3_suc_1 == True:
                    if event.key == pygame.K_r:
                        mod3_suc_1=False
                        mod3_stage1=True
                if mod3_suc_2 == True:
                    if event.key == pygame.K_r:
                        mod3_suc_2=False
                        mod3_stage2=True
                if mod3_suc_3 == True:
                    if event.key == pygame.K_r:
                        mod3_suc_3=False
                        mod3_stage3=True




            # 마우스 버튼을 눌렀을때
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 현재 화면이 startscreen 일때
                if startscreen == True:
                    # 버튼 클래스에서 isover조건에 참이 됬을때
                    if gameplaybtn.isover(mousepos):
                        # 화면전환
                        startscreen = False
                        roading_screen = True
                    if howtoplaybtn.isover(mousepos):
                        startscreen = False
                        howtoplayscreen = True
                if selectmode == True:
                    if mod1btn.isover(mousepos):
                        selectmode = False
                        mode1 = True
                    if mod2btn.isover(mousepos):
                        selectmode = False
                        mod2_roading_screen = True
                    if mod3btn.isover(mousepos):
                        selectmode = False
                        mod3_roading_screen = True

                if mode2_set == True:
                    if modstage1btn.isover(mousepos):
                        mode2_set = False
                        mode2_stage_1 = True
                    if modstage2btn.isover(mousepos):
                        mode2_set = False
                        mode2_stage_2 = True
                    if modstage3btn.isover(mousepos):
                        mode2_set = False
                        mode2_stage_3 = True
                    if modstage4btn.isover(mousepos):
                        mode2_set = False
                        mode2_stage_4 = True
                    if modstage5btn.isover(mousepos):
                        mode2_set = False
                        mode2_stage_5 = True
                    if backbtn.isover(mousepos):
                        mode2_set = False
                        startscreen = True
                # pause_screen이 True 일때 홈키 버튼 과 다시시작 버튼
                if pause_screen == True:
                    if resume.isover(mousepos):
                        pause_screen = False
                        mode1 = True
                    if home.isover(mousepos):
                        play.create()
                        food.create()
                        pause_screen = False
                        startscreen = True
                if howtoplayscreen == True:
                    if returnbtn.isover(mousepos):
                        howtoplayscreen = False
                        startscreen = True
                if game_success_1==True:
                    if mod3backbtn.isover(mousepos):
                        game_success_1=False
                        startscreen=True
                    if mod3nextbtn.isover(mousepos):
                        game_success_1=False
                        mode2_stage_2=True


                if game_success_2==True:
                    if mod3backbtn.isover(mousepos):
                        game_success_2=False
                        startscreen=True
                    if mod3nextbtn.isover(mousepos):
                        game_success_2=False
                        mode2_stage_3=True
                if game_success_3==True:
                    if mod3backbtn.isover(mousepos):
                        game_success_3=False
                        startscreen=True
                    if mod3nextbtn.isover(mousepos):
                        game_success_3=False
                        mode2_stage_4=True
                if game_success_4==True:
                    if mod3backbtn.isover(mousepos):
                        game_success_4=False
                        startscreen=True
                    if mod3nextbtn.isover(mousepos):
                        game_success_4=False
                        mode2_stage_5=True
                if mod3_set == True:

                    if mod3_stage1btn.isover(mousepos):
                        mod3_set = False
                        mod3_stage1 = True
                    if mod3_stage2btn.isover(mousepos):
                        mod3_set = False
                        mod3_stage2 = True
                    if mod3_stage3btn.isover(mousepos):
                        mod3_set = False
                        mod3_stage3 = True
                    if backbtn.isover(mousepos):
                        mod3_set=False
                        startscreen = True
                if mod3_suc_1==True:
                    if mod3backbtn.isover(mousepos):
                        mod3_suc_1=False
                        startscreen=True
                    if mod3nextbtn.isover(mousepos):
                        mod3_suc_1=False
                        mod3_stage2=True
                if mod3_suc_2== True:
                    if mod3backbtn.isover(mousepos):
                        mod3_suc_2=False
                        startscreen=True
                    if mod3nextbtn.isover(mousepos):
                        mod3_suc_2=False
                        mod3_stage3=True
                if mod2_pause_screen==True:
                    if resume.isover(mousepos):
                        if a==1:
                            mod2_pause_screen=False
                            mode2_stage_1=True
                        elif a==2:
                            mod2_pause_screen = False
                            mode2_stage_2 = True
                        elif a==3:
                            mod2_pause_screen = False
                            mode2_stage_3 = True
                        elif a==4:
                            mod2_pause_screen=False
                            mode2_stage_4=True
                        elif a==5:
                            mod2_pause_screen = False
                            mode2_stage_5 = True

                    if home.isover(mousepos):
                        mod2_pause_screen=False
                        startscreen=True
                        score=200
                        stageplay.create()
                        stageplay2.create()
                        stageplay3.create()
                        stageplay4.create()
                        stageplay5.create()
                if mod3_pause_screen == True:
                    if resume.isover(mousepos):
                        print(b)
                        if b == 1:
                            mod3_pause_screen = False
                            mod3_stage1 = True
                        elif b == 2:
                            mod3_pause_screen = False
                            mod3_stage2 = True
                        elif b == 3:
                            mod3_pause_screen = False
                            mod3_stage3 = True

                    if home.isover(mousepos):
                        mod3_pause_screen = False
                        startscreen = True
                        score=200
                        picplay.create()
                        picplay1.create()
                        picplay2.create()

        # 화면 구성
        # startscreen이 True일 경우
        if startscreen == True:
            # 화면구성
            screen.blit(homescreen, (0, 0))
            pygame.display.flip()
        # 모드 선택
        if selectmode == True:
            pygame.init()
            screen.fill(BLACK)
            pygame.draw.rect(screen, WHITE, (100, 25, 1000, 400))
            hansin_font("ArcadeMod","",BLACK,40,(100,25),screen)
            pygame.draw.rect(screen, WHITE, (100, 450, 450, 400))
            hansin_font("StageMod", "", BLACK, 40, (100, 450), screen)
            pygame.draw.rect(screen, WHITE, (650, 450, 450, 400))
            hansin_font("PerfectMod","",BLACK,40,(650,450),screen)
            pygame.display.flip()
        # 모드 1
        if mode1 == True:
            # mainsurface와 barsurface screen에 삽입
            screen.blit(mainsurface, (0, 0))
            screen.blit(barsurface, (0, 700))
            # surface화면 배경 설정
            mainsurface.fill(GRAY)
            barsurface.fill(ORANGE)
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
            # 플레이어 이동
            play.move()
            # 폰트
            hansin_font("길이 : ", play.length, BLACK, 40, (10, 0), barsurface)
            hansin_font("속도 : ", str(round(speed/3, 2)), BLACK, 40, (10, 55), barsurface)
            hansin_font("종료하고 싶으면 q키를 누르세요", "", BLACK, 20, (20, 150), barsurface)
            pygame.display.flip()
        # 모드 2 - 스테이지 선택 화면
        if mode2_set == True:
            screen.fill(GREEN)
            screen.blit(modestagepng, (0, 0))
            screen.blit(backkey, (1000, 700))

        # 모드 2 - 스테이지 1
        if mode2_stage_1 == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("stage 1", "", BLACK, 30, (340, 20), screen)
            stageplay.draw(screen)
            clock.tick(10)
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
            wall9 = Wall(620,0,140,280)
            crash_wall(stageplay, wall9)
            wall6 = Wall(760, 760, 440, 700)
            crash_wall(stageplay, wall6)
            wall10 = Wall(760,0,140,420)
            crash_wall(stageplay,wall10)

            wall11 = Wall(900,0,140,560)
            crash_wall(stageplay,wall11)
            fp1 = finishpoint(1100, 200, 20, 20, screen)
            if point_finish(stageplay, fp1) == True:
                stageplay.create()
                mode2_stage_1 = False
                game_success_1 = True
            pygame.display.flip()
        if mode2_stage_2 == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("stage 2", "", BLACK, 30, (310, 20), screen)
            stageplay2.draw(screen)
            clock.tick(16)
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

            fp1 = finishpoint(1100, 800, 20, 20, screen)
            if point_finish(stageplay2, fp1) == True:
                mode2_stage_2 = False
                game_success_2 = True

            pygame.display.flip()

        if mode2_stage_3 == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("stage 3", "", BLACK, 30, (400, 20), screen)
            stageplay3.draw(screen)
            clock.tick(22)
            stageplay3.move()
            wall1 = Wall(900, 400, 300, 60)
            crash_wall(stageplay3, wall1)
            wall7 = Wall(900,680,300,60)
            crash_wall(stageplay3, wall7)
            wall2 = Wall(740, 0, 60, 800)
            crash_wall(stageplay3, wall2)
            wall6=Wall(740,540,300,60)
            crash_wall(stageplay3, wall6)
            wall3 = Wall(440, 440, 60, 480)
            crash_wall(stageplay3, wall3)
            wall4 = Wall(440, 380, 240, 60)
            crash_wall(stageplay3, wall4)
            wall8 = Wall(580,500,160,60)
            crash_wall(stageplay3,wall8)
            wall9 = Wall(440,620,240,60)
            crash_wall(stageplay3, wall9)
            wall10=Wall(640,80,40,300)
            crash_wall(stageplay3, wall10)
            wall11=Wall(580,740,220,60)
            crash_wall(stageplay3, wall11)
            wall12=Wall(520,0,40,300)
            crash_wall(stageplay3, wall12)
            wall5 = Wall(200, 0, 60, 700)
            crash_wall(stageplay3, wall5)
            wall13= Wall(380,100,60,500)
            crash_wall(stageplay3, wall13)
            wall14=Wall(0,0,80,900)
            crash_wall(stageplay3,wall14)

            fp1 = finishpoint(100, 100, 20, 20, screen)
            if point_finish(stageplay3, fp1) == True:
                mode2_stage_3 = False
                game_success_3 = True

            pygame.display.flip()

        if mode2_stage_4 == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("stage 4", "", BLACK, 30, (370, 20), screen)
            stageplay4.draw(screen)
            clock.tick(32)
            stageplay4.move()
            wall1 = Wall(140, 40, 60, 360)
            crash_wall(stageplay4, wall1)
            wall2 = Wall(140, 500, 60, 360)
            crash_wall(stageplay4, wall2)
            wall3 = Wall(320, 140, 60, 600)
            crash_wall(stageplay4, wall3)
            wall4 = Wall(500, 0 , 60 , 280)
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

            fp1 = finishpoint(1160, 420, 20, 20, screen)
            if point_finish(stageplay4, fp1) == True:
                mode2_stage_4 = False
                game_success_4 = True

            pygame.display.flip()

        if mode2_stage_5 == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("stage 5", "", BLACK, 30, (400, 20), screen)
            stageplay5.draw(screen)
            clock.tick(29)
            stageplay5.move()
            wall1 = Wall(0, 0, 20, 900)
            crash_wall(stageplay5, wall1)
            wall2 = Wall(0, 880, 1200, 20)
            crash_wall(stageplay5, wall2)
            wall3 = Wall(1140, 0 , 60, 900)
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
            wall15 = Wall(820, 260, 40 , 420)
            crash_wall(stageplay5, wall15)
            wall16 = Wall(400, 260, 420, 40)
            crash_wall(stageplay5 , wall16)
            wall17 = Wall(400, 260, 40, 340)
            crash_wall(stageplay5, wall17)
            wall18 = Wall(400, 560, 360, 40)
            crash_wall(stageplay5, wall18)
            wall19 = Wall(720, 340, 40, 220)
            crash_wall(stageplay5, wall19)


            fp1 = finishpoint(760, 340, 60, 20, screen)
            if point_finish(stageplay5, fp1) == True:
                mode2_stage_5 = False
                ending_credit = True

            pygame.display.flip()
        # pause_screen 화면 구성
        if pause_screen == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("paused", "", BLACK, 40, (500, 50), screen)

            screen.blit(pausekey, (400, 400))
            screen.blit(homekey, (700, 400))

            pygame.display.flip()
        # 로딩 스크린 구성
        if roading_screen == True:
            screen.fill(0)
            hansin_font("로딩중...", "", WHITE, 50, (500, 400), screen)
            pygame.display.flip()
            time.sleep(1)
            roading_screen = False
            selectmode = True
        # 모드 2 - 성공 화면 구성
        if game_success_1 == True or game_success_2 == True or game_success_3 == True or game_success_4 == True:
            screen.fill(GREEN)
            screen.blit(nextkey,(730,600,304,184))
            screen.blit(returnkey,(50,600,228,243))
            hansin_font("스테이지 클리어!!", "", WHITE, 70, (300, 150), screen)
        if mod2_roading_screen == True:
            screen.fill(BLACK)
            hansin_font("로딩중...", "", WHITE, 50, (500, 400), screen)
            pygame.display.update()
            time.sleep(0.6)
            mod2_roading_screen = False
            mode2_set = True
        if mod3_roading_screen == True:
            screen.fill(BLACK)
            hansin_font("로딩중...", "", WHITE, 50, (500, 400), screen)
            pygame.display.update()
            time.sleep(0.6)
            mod3_roading_screen = False
            mod3_set = True
        if mod3_set == True:
            # 도형 하나당 크기 308 289
            pygame.init()
            screen.fill(0)
            screen.blit(perfectmod, (0, 0))
            screen.blit(backkey, (1000,700))
            #pygame.draw.rect(screen, BLUE, (431, 581, 308, 289))
        if howtoplayscreen == True:
            screen.fill(GRAY)

            screen.blit(howtopg,(150,100))
            pygame.draw.ellipse(screen, BLUE, (910, 800, 100, 40))
        # 점수
        if mod3_stage1 == True:
            pygame.init()

            screen.fill(GRAY)
            hansin_font("점수", str(score), BLACK, 50, (0, 0), screen)
            if score >= 180:
                hansin_font("등급", 'A', RED, 50, (0, 60), screen)

            elif score >= 160:
                hansin_font("등급", 'B', ORANGE, 50, (0, 60), screen)
            elif score >= 140:
                hansin_font("등급", 'C', YELLOW, 50, (0, 60), screen)
            elif score >= 120:
                hansin_font("등급", 'D', GREEN, 50, (0, 60), screen)
            else:
                hansin_font("등급", 'F', BLACK, 50, (0, 60), screen)
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
            gg1 = Wall(340,300,500,10)
            gg2= Wall(840,300,10,500)
            gg3 = Wall(540,500,10,500)
            if crash_wall(picplay1,gg)==True or crash_wall(picplay1,gg1)==True or crash_wall(picplay1,gg2)==True:
                score=200
            if line_play(picplay1, line1) != True and line_play(picplay1, line2) != True and line_play(picplay1, line3) \
                    != True and line_play(picplay1, line4) != True and line_play(picplay1, line5) != True and line_play( \
                    picplay1, line6) != True and line_play(picplay1, line7) != True and line_play(picplay1,line8) != True and \
                    line_play(picplay1, line9) != True and line_play(picplay1, line10) != True :
                score -= 1

            st3_fin = finishpoint(360, 840, 20, 20, screen)
            if point_finish(picplay1, st3_fin) == True:
                mod3_stage1 = False
                mod3_suc_1 = True
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
            picplay1.draw(screen)
            clock.tick(10)
            if picplay1.move() == True:
                score = 200


        if mod3_stage2 == True:
            pygame.init()

            screen.fill(GRAY)

            hansin_font("점수", str(score), BLACK, 50, (0, 0), screen)
            if score >= 180:
                hansin_font("등급", 'A', RED, 50, (0, 60), screen)

            elif score >= 160:
                hansin_font("등급", 'B', ORANGE, 50, (0, 60), screen)
            elif score >= 140:
                hansin_font("등급", 'C', YELLOW, 50, (0, 60), screen)
            elif score >= 120:
                hansin_font("등급", 'D', GREEN, 50, (0, 60), screen)
            else:
                hansin_font("등급", 'F', BLACK, 50, (0, 60), screen)
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

            if crash_wall(picplay,gg)==True:# or crash_wall(picplay1,gg1)==True or crash_wall(picplay1,gg2)==True:
                score=200
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
                mod3_stage2 = False
                mod3_suc_2 = True
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
            picplay.draw(screen)
            clock.tick(13)
            if picplay.move() == True:
                score = 200
        if mod3_stage3==True:
            pygame.init()

            screen.fill(GRAY)
            hansin_font("점수", str(score), BLACK, 50, (0, 0), screen)
            if score >= 180:
                hansin_font("등급", 'A', RED, 50, (0, 60), screen)
            elif score >= 160:
                hansin_font("등급", 'B', ORANGE, 50, (0, 60), screen)
            elif score >= 140:
                hansin_font("등급", 'C', YELLOW, 50, (0, 60), screen)
            elif score >= 120:
                hansin_font("등급", 'D', GREEN, 50, (0, 60), screen)
            else:
                hansin_font("등급", 'F', BLACK, 50, (0, 60), screen)

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

            if line_play(picplay2, line1 ) != True and line_play(picplay2, line2 ) != True and line_play(picplay2, line3 ) != True and \
                    line_play(picplay2, line4 ) != True and line_play(picplay2, line5 ) != True and line_play(picplay2, line6 ) != True \
                    and line_play(picplay2, line7 ) != True and line_play(picplay2, line8 ) != True and line_play(picplay2, line9 ) != \
                    True and line_play(picplay2, line10 ) != True and line_play(picplay2, line11 ) != True and line_play(picplay2, line12 )\
                    != True and line_play(picplay2, line13 ) != True and line_play(picplay2, line14 ) != True and line_play(picplay2, line15 )\
                    != True and line_play(picplay2, line16 ) != True and line_play(picplay2, line17 ) != True and line_play(picplay2, line18 )\
                    != True and line_play(picplay2, line19 ) != True and line_play(picplay2, line20 ) != True and line_play(picplay2, line21 )\
                    != True and line_play(picplay2, line22 ) != True and line_play(picplay2, line23 ) != True and line_play(picplay2, line24 )\
                    != True and line_play(picplay2, line25 ) != True and line_play(picplay2, line26 ) != True and line_play(picplay2, line27 )\
                    != True and line_play(picplay2, line28 ) != True and line_play(picplay2, line29 ) != True and line_play(picplay2, line30 )\
                    != True and line_play(picplay2, line31 ) != True and line_play(picplay2, line32 ) != True and line_play(picplay2, line33 )\
                    != True and line_play(picplay2, line34 ) != True and line_play(picplay2, line35 ) != True and line_play(picplay2, line36 )\
                    != True and line_play(picplay2, line37 ) != True and line_play(picplay2, line38 ) != True and line_play(picplay2, line39 )\
                    != True and line_play(picplay2, line40 ) != True and line_play(picplay2, line41 ) != True:
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
            clock.tick(13)
            gg=Wall(480,440,10,600)

            gg1=Wall(260,440,700,10)

            gg2=Wall(620,140,10,560)

            if crash_wall(picplay2,gg)==True or crash_wall(picplay2,gg1)==True or crash_wall(picplay2,gg2)==True:
                score=200
            if picplay2.move() == True:
                score = 200

        if mod1_dead == True:
            pygame.init()
            screen.fill(RED)
            hansin_font("죽었습니다 ㅠㅜ", "", WHITE, 50, (0, 0), screen)
            pygame.display.flip()
        if mod2_pause_screen == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("paused", "", BLACK, 40, (500, 50), screen)

            screen.blit(pausekey, (400, 400))
            screen.blit(homekey, (700, 400))

            pygame.display.flip()
        if mod3_suc_1 == True:
            screen.fill(color)
            pygame.init()
            if rank == "A" :
                hansin_font("합격!! 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("정말잘하네요!","",WHITE,80,(30,110),screen)
                hansin_font("r키를 눌러 다시 합니다.","",WHITE,35,(100,300),screen)
                screen.blit(nextkey,(730,600))
                screen.blit(returnkey,(50,600))
            elif rank == "B":
                hansin_font("합격!! 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("잘하네요!", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(nextkey, (730, 600))
                screen.blit(returnkey, (50, 600))
            elif rank =="C":
                hansin_font("합격!! 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("좀~ 하네요!", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(nextkey, (730, 600))
                screen.blit(returnkey, (50, 600))
            elif rank == "D":
                hansin_font("탈락... 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("너무 아쉽당~", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(returnkey, (50, 600))
            elif rank == "F":
                hansin_font("탈락... 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("안타깝네요 힘내세요", "", WHITE, 100, (10, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(returnkey, (50, 600))

        if mod3_suc_2 == True:
            screen.fill(color)
            pygame.init()
            if rank == "A":
                hansin_font("합격!! 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("정말잘하네요!", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(nextkey, (730, 600))
                screen.blit(returnkey, (50, 600))
            elif rank == "B":
                hansin_font("합격!! 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("잘하네요!", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(nextkey, (730, 600))
                screen.blit(returnkey, (50, 600))
            elif rank == "C":
                hansin_font("합격!! 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("좀~ 하네요!", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(nextkey, (730, 600))
                screen.blit(returnkey, (50, 600))
            elif rank == "D":
                hansin_font("탈락... 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("너무 아쉽당~", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(returnkey, (50, 600))
            elif rank == "F":
                hansin_font("탈락... 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("안타깝네요 힘내세요", "", WHITE, 100, (10, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(returnkey, (50, 600))
        if mod3_suc_3==True:
            screen.fill(color)
            pygame.init()
            if rank == "A" or rank == "B" or rank == "C":
                mod3_suc_3=False
                ending_credit=True
            elif rank == "D":
                hansin_font("탈락... 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("너무 아쉽당~", "", WHITE, 80, (30, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(returnkey, (50, 600))
            elif rank == "F":
                hansin_font("탈락... 등급 : ", rank, WHITE, 100, (10, 10), screen)
                hansin_font("안타깝네요 힘내세요", "", WHITE, 100, (10, 110), screen)
                hansin_font("r키를 눌러 다시 합니다.", "", WHITE, 35, (100, 300), screen)
                screen.blit(returnkey, (50, 600))

        if mod3_pause_screen == True:
            pygame.init()
            screen.fill(GRAY)
            hansin_font("paused", "", BLACK, 40, (500, 50), screen)
            screen.blit(pausekey, (400, 400))
            screen.blit(homekey, (700, 400))

            pygame.display.flip()
        if ending_credit == True:
            screen.fill(0)
            print(i1)
            screen.blit(theend,(0,i1))
            i1-=1
            if i1<=-1050:
                time.sleep(1)
                ongame=False
            pygame.display.flip()

        pygame.display.flip()
