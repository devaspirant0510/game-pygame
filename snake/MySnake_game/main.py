#===================================
# 0.필요한 모듈 임포트
import pygame
import time
import sys
import random
import pandas as pd
import os
#===================================
# 0.1 score.csv 파일이 있는지 확인
if os.path.isfile('score.csv'):
    pass
# 없다면 파일 생성
else:
    df = pd.DataFrame(columns=['점수', '시간'])
    print(df)
    df.to_csv("score.csv")
#===================================
#1. 초기 설정

# 전체화면
width=1000
height=700
pixel_size=20
# 게임 화면
game_screen_width=800
game_screen_height=600
# 점수판 화면
score_screen_width=200
score_screen_height=600
# 정보 화면
state_screen_width=1000
state_screen_height=100

UP=(0,-1)
DOWN=(0,1)
LEFT=(-1,0)
RIGHT=(1,0)

#===================================
#2. 색상

red = (232,80,91)
yellow = (249,213,110)
background_color = (243,236,193)
snake_color = (20,177,171)
score_color = (98,82,97)
state_color = (166,166,164)
font_color = (58,42,57)

#===================================
#3. 뱀 클래스

class Snake(object):
    # 생성
    def __init__(self):
        self.color=snake_color
        self.position=[]
        self.direction=[]
        self.length=3
        self.start_time=time.time()
        self.live_time = 0
        self.create()
    #생성
    def create(self):
        self.start_time=time.time()
        # 초기 위치 중앙
        self.position = [(game_screen_width//2,game_screen_height//2)]
        # 초기 방향 랜덤
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
    # 키입력을 받았을때 방향 전환
    def key_control(self,key):
        # 서로 반대방향으로 전환할시 그냥 방향값 리턴 -> 즉 플레이어의 방향이랑 키입력의 방향이 반대가 될때 키입력 안됨
        # 예시 뱀방향 = LEFT 플레이어 입력 = RIGHT 일시 방향 전환 x
        if (self.direction[0]*-1,self.direction[1]*-1) == key:
            return self.direction
        else:
            self.direction=key
            return self.direction
    # 이동
    def move(self):
        # 뱀 한 픽셀의 크기
        # 높이 너비 지정
        x_pos=self.direction[0]*pixel_size
        y_pos=self.direction[1]*pixel_size

        # 뱀의 머리 부분을 기준으로 뱀위치 +(좌표값+방향*픽셀사이즈)로 뱀을 연결시킴
        body_pos = (self.position[0][0] + x_pos, self.position[0][1] + y_pos)
        # 큐알고리즘 FIFO
        # 뱀의 몸통부분을 0번위치에 계속해서 추가함
        self.position.insert(0,body_pos)
        if (self.position[0][0],self.position[0][1]) in self.position[3:]:
            live_time =time.time()- self.start_time
            write_score(live_time)
            time.sleep(1)
            self.create()
            food.create()
            self.length=3
        else:
            # position 의 길이가 length 의 길이를 넘길시 가장 마지막에 있는 값삭제
            # 즉 새로운 값은 0번위치에 들어가고
            # 그 값의 위치가 length 가 되면 값 삭제
            if len(self.position)>self.length:
                self.position.pop()

            # 벽에 닿을시 생성
            if self.position[0][0]<-20 or self.position[0][0]>800:
                live_time = time.time() - self.start_time
                write_score(live_time)
                time.sleep(1)
                self.create()
                food.create()
                self.length=3
            if self.position[0][1]<-20 or self.position[0][1]>600:
                live_time=time.time()-self.start_time
                write_score(live_time)
                time.sleep(1)
                self.create()
                food.create()
                self.length=3

    # 뱀을 화면에 그림
    def draw(self,sc):
        # for 문으로 position 의 인덱스 하나씩 출력하여 draw_rect 함수에 리턴
        for i in range(len(self.position)):
            my_pos_x=self.position[i][0]
            my_pos_y=self.position[i][1]
            # draw_rect(내위치 x값, 내위치 y 값, 그림크기 x,그림크기 y,표시할 화면,색상)
            if i==0:
                draw_rect(my_pos_x,my_pos_y,pixel_size,pixel_size,sc,(0,0,0))
            else:
                draw_rect(my_pos_x,my_pos_y,pixel_size,pixel_size,sc,self.color)
    # 먹었을때 길이 1증가
    def eat(self):
        self.length+=1

#===================================
# 4.먹이 클래스
class Food(object):
    # 생성자 함수
    def __init__(self):
        self.create()
        self.position = []
        # 먹이 상태
        self.food_size = [False,False,False,False]
        # 색 지정
        self.color = red
        # 먹이 위치 지정
        self.food_pos1=[]
        self.food_pos2=[]
        self.food_pos3=[]
        self.food_pos4=[]
        self.create()
    # 먹이 위치 랜덤값
    def create(self):
        # 먹이가 구석으로 가면 먹기 어려워서
        # 범위 조절
        self.position=[(random.randrange(40,760,20)),(random.randrange(40,560,20))]
        # 먹이 상태 모두 True
        self.food_size=[True,True,True,True]

    def draw(self,sc):
        # 먹이 상태에 따라 그림 그림
        if self.food_size[0]:
            draw_rect(self.position[0],self.position[1],pixel_size,pixel_size,sc,self.color)
            self.food_pos1=[self.position[0],self.position[1]]
        # 먹이를 먹으면 먹이 지움
        else:
            draw_rect(self.position[0],self.position[1],pixel_size,pixel_size,sc,background_color)

        if self.food_size[1]:
            draw_rect(self.position[0]+pixel_size, self.position[1], pixel_size, pixel_size, sc, self.color)
            self.food_pos2 = [self.position[0]+pixel_size, self.position[1]]
        else:
            draw_rect(self.position[0]+pixel_size, self.position[1], pixel_size, pixel_size, sc, background_color)

        if self.food_size[2]:
            draw_rect(self.position[0], self.position[1]+pixel_size, pixel_size, pixel_size, sc, self.color)
            self.food_pos3 = [self.position[0], self.position[1]+pixel_size]
        else:
            draw_rect(self.position[0], self.position[1] + pixel_size, pixel_size, pixel_size, sc, background_color)

        if self.food_size[3]:
            draw_rect(self.position[0]+pixel_size, self.position[1]+pixel_size, pixel_size, pixel_size, sc, self.color)
            self.food_pos4 = [self.position[0]+pixel_size, self.position[1]+pixel_size]
        else:
            draw_rect(self.position[0] + pixel_size, self.position[1] + pixel_size, pixel_size, pixel_size, sc, background_color)

#===================================
# 5. 함수정의
# draw_rect(내위치 x값, 내위치 y 값, 그림크기 x,그림크기 y,표시할 화면,색상)
def draw_rect(x,y,size_x,size_y,sc,color):
    pygame.draw.rect(sc,color,(x,y,size_x,size_y))

# 플레이어가 먹이를 먹었는지 판단
def check_eat_food(p,f):

    head=[p.position[0][0],p.position[0][1]]
    if f.food_size==[False,False,False,False]:
        p.eat()
        f.create()
    else:
        if f.food_pos1 == head:
            f.food_size[0]=False
        if f.food_pos2 == head:
            f.food_size[1]=False
        if f.food_pos3 ==  head:
            f.food_size[2]=False
        if f.food_pos4 == head:
            f.food_size[3]=False

# 플레이어가 죽었을때 점수 기록
def write_score(live):
    score=pd.read_csv("score.csv")
    # 딕셔너리 생성

    data_dict={'점수':[round(player.length+((time.time()-player.start_time)*0.037),1)],
               '시간':[round(live,1)]}
    # 딕셔너리 정보를 유저 데이터프레임에 저장
    user_data=pd.DataFrame(data_dict)
    # 원본데이터랑 유저데이터 concat
    score=pd.concat([score,user_data],ignore_index=True)
    # 행에 Unnmae 으로 시작하는 행이 있을시 삭제
    score.drop(score.filter(regex="Unname"), axis=1, inplace=True)
    # 점수를 기준으로 오름차순 정렬
    score=score.sort_values(by=['점수'],axis=0, ascending=False)


    # 추가된 데이터 저장
    score.to_csv("score.csv")

# 폰트 설정
# font-set( 표시할 문자열, 표시할 변수(표시할 변수가 없을시 ""), 글자 색, 글자 크기, 글자위치(튜플, 리스트 형태),표시할 화면)
def font_set(var_m, var_a, txt_color, txt_size, po, su):
    # 기본 폰트
    font = pygame.font.Font(None, txt_size)
    text = font.render(var_m + str(var_a), 1, txt_color)
    su.blit(text, (po[0], po[1]))

#===================================
# 5. 메인함수
if __name__=="__main__":
    # 전체 화면
    main_screen = pygame.display.set_mode((width,height))

    # 게임 화면
    game_surface = pygame.Surface((game_screen_width,game_screen_height))
    game_surface = game_surface.convert()


    # 점수판 화면
    score_surface = pygame.Surface((score_screen_width,score_screen_height))
    score_surface = score_surface.convert()

    # 정보 화면
    state_surface = pygame.Surface((state_screen_width,state_screen_height))
    state_surface = state_surface.convert()

    # 오브젝트 생성
    player = Snake()
    food = Food()

    # 프레임 지정
    clock=pygame.time.Clock()

    # 키 반복제어
    pygame.key.set_repeat(5000,5000)

    # 파이게임 초기화
    pygame.init()
    while True:
        score=pd.read_csv("score.csv")
        # pygame event
        for event in pygame.event.get():

            # 키를 눌렀을때
            if event.type == pygame.KEYDOWN:
                # 플레이어 클래스의 key_control 함수에 해당되는 값 매게변수로 전달
                if event.key in [pygame.K_w,pygame.K_UP]:
                    player.key_control(UP)
                elif event.key in [pygame.K_a,pygame.K_LEFT]:
                    player.key_control(LEFT)
                elif event.key in [pygame.K_s,pygame.K_DOWN]:
                    player.key_control(DOWN)
                elif event.key in [pygame.K_d,pygame.K_RIGHT]:
                    player.key_control(RIGHT)

            # 종료버튼을 눌렀을때
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # surface 설정
        main_screen.blit(game_surface,(0,100))
        main_screen.blit(score_surface,(800,100))
        main_screen.blit(state_surface,(0,0))

        # surface 색상 지정
        game_surface.fill(background_color)
        score_surface.fill(score_color)
        state_surface.fill(state_color)

        # 점수 표시
        font_set('score : ',round(player.length+((time.time()-player.start_time)*0.037),1),font_color,75,(10,15),state_surface)
        time_score=time.time()
        # 시간 표시
        font_set('time : ',round((player.start_time-time_score)*-1),font_color,75,(350,15),state_surface)
        # 점수판
        font_set("rank  score  time",'',background_color,35,(3,10),score_surface)
        for i in range(1,11):
            draw_rect(0,((i-1)*50)-10,200,2,score_surface,state_color)
            if i==1:
                font_set('',f'{i}st',background_color,40,(3,50*i),score_surface)
                if len(score)>0:
                    font_set('',f'   {score["점수"][i-1]}   {score["시간"][i-1]}',background_color,40,(50,50*i),score_surface)
                else:
                    pass
            elif i==2:
                font_set('', f'{i}nd', background_color, 40, (3, 50 * i), score_surface)
                if len(score)>1:
                    font_set('',f'   {score["점수"][i-1]}   {score["시간"][i-1]}',background_color,40,(50,50*i),score_surface)
                else:
                    pass
            elif i==3:
                font_set('', f'{i}rd', background_color, 40, (3, 50 * i), score_surface)
                if len(score)>2:
                    font_set('',f'   {score["점수"][i-1]}   {score["시간"][i-1]}',background_color,40,(50,50*i),score_surface)
                else:
                    pass
            else:
                font_set('', f'{i}th', background_color, 40, (3, 50 * i), score_surface)
                try:
                    font_set('',f'   {score["점수"][i-1]}   {score["시간"][i-1]}',background_color,40,(50,50*i),score_surface)
                except:
                    pass
        # food 오브젝트 화면에 표시
        food.draw(game_surface)
        # player 가 food 를 먹었는지 판단
        check_eat_food(player,food)
        # player 움직임
        player.move()
        # player 그림
        player.draw(game_surface)
        # 프레임 속도
        clock.tick(15)
        # 업데이트
        pygame.display.flip()


