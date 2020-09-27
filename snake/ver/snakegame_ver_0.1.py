import pygame
import sys
import time
import random

from pygame.locals import *

#화면 사이즈
width,height = 800,600
#픽셀 사이즈
grid=20
gridwidth=width/grid
gridheight=height/grid
#RGB색상코드
White=(255,255,255)
Green=(0,250,0)
Orange=(250,100,0)
#방향값
UP=(0,-1)
DOWN=(0,1)
LEFT=(-1,0)
RIGHT=(1,0)
#속도
FPS=10

#플레이어 클래스 
class Python(object):
    #생성함수 
    def __init__(self):
        self.create()
        self.color =Green#생성시 초록색으로 색 지정
    #create 함수 실행됬을때
    #생성시 자동으로 create 함수 실행됨
    def create(self):
        self.length=2#초기길이
        self.positions=[((width/2),(height/2))] #초기위치 중앙값으로 지정
        self.direction=random.choice([UP,DOWN,LEFT,RIGHT]) #생성시 방향 랜덤으로 지정 
    def control(self,xy):
        #위에서 아래 왼쪽에서 오른쪽으로 방향 전환시 원래 방향값 그대로 적용(방향 전환 안됨)
        
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        
        else:
            self.direction =xy
    #이동하는 함수
    def move(self):
        #머리부분 정의
        cur=self.positions[0]
        #방향을 x,y로 정의
        x,y=self.direction
        #세로운 몸통 위치 정의
        new = (((cur[0] +(x*grid))%width),(cur[1]+(y*grid))%height)
        if new in self.positions[3:]:
            #자기 머리에 몸통이 닿았을시
            #crete 함수 실행
            #즉 길이 위치 방향 초기화 시킴 
            self.create()
        else:
            #아닐경우 머리부분에 new에서 생성한 몸통 추가 
            self.positions.insert(0,new)
            if len(self.positions)>self.length:
                #새로운 몸통이 추가 됬으니 꼬리부분 삭제
                #큐 알고리즘 
                self.positions.pop()
    def eat(self):
        #eat 함수가 실행됬을때
        #길이 1 증가
        self.length+=1
    #화면에 표시
    def draw(self, surface):
        for p in self.positions:
            #뱀의 방향값 모두 불러옴
            #draw_object 함수 실행
            draw_objects(surface,self.color,p)

class Feed(object):
    def __init__(self):
        #생성함수
        #주황색으로 지정
        self.color=Orange
        #생성과 동시에 create 실행
        self.create()
    def create(self):
        #방향 랜덤으로 지정 
        self.position=(random.randint(0,gridwidth-1)*grid, random.randint(0,gridheight-1)*grid)
    def draw(self,surface):
        #화면에 그림 
        draw_objects(surface,self.color,self.position)
def draw_objects(surface,color,pos):
    #방향값과 색 화면 정보를 받아들여 실제 화면에 표시
    r= pygame.Rect((pos[0], pos[1]),(grid,grid) )
    pygame.draw.rect(surface,color,r)
def check_eat(pyhton,feed):
    #뱀의 머리부분과 먹이 좌표가 똑같을시 
    if python.positions[0] == feed.position:
        python.eat()
        #뱀의 eat 함수 실행
        #즉 뱀 길이 1 증가
        feed.create()
        #먹이는 새로 생성


#메인함수
if __name__ == "__main__":
    #인스턴스
    python=Python()
    feed=Feed()
    #초기화
    pygame.init()
    #화면 정의
    #위에서 정의한 높이값과 길이값 불러옴 
    screen=pygame.display.set_mode((width,height))
    #캡션이름 정의
    pygame.display.set_caption("title")
    #surface라는 변수 선언해 screen 화면 convert
    #Surface의 경우 화면을 분활할때 사용
    #지금 같은경우 기능이 없기때문에 그냥 screen을 상관없음
    surface=pygame.Surface(screen.get_size())
    surface=surface.convert()
    #화면 하얀색으로 칠함
    surface.fill(White)
    clock=pygame.time.Clock()
    screen.blit(surface,(0,0))
    while True:
        for event in pygame.event.get():
            #x버튼 (종료버튼)눌렀을때 종료됨 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #방향키 눌러졌을때
            #위에서 정의한 방향값 python의 control함수에 반환
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    python.control(UP)
                elif event.key == K_DOWN:
                    python.control(DOWN)
                elif event.key == K_LEFT:
                    python.control(LEFT)
                elif event.key == K_RIGHT:
                    python.control(RIGHT)
        surface.fill(White)
        #뱀이 이동하는 함수
        python.move()
        #뱀과 먹이의 좌표값이 똑같은가?
        #즉 뱀이 먹이를 먹었는지 판단
        check_eat(python,feed)
        #프레임속도는 뱀길이와 정비례
        speed=(FPS+python.length)/2
        clock.tick(speed)
        #뱀 화면에 보이게 그림 
        python.draw(surface)
        #먹이 화면에 보이게 그림 
        feed.draw(surface)
        #앞에서 정의한 surface를 주 화면으로 사용함
        screen.blit(surface,(0,0))
        #화면 업데이트
        #꼭 필요함!!
        pygame.display.flip()
        
        






