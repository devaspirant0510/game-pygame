#코드에대한 자세한 내용은 ver_0.1참고
import pygame
import random
import time
import sys

from pygame.locals import *

#화면크기과 픽셀사이즈
WINDOW_WIDTH,WINDOW_HEIGHT=1000,600
greed=20
greedheight=WINDOW_HEIGHT//greed
greedwidth=WINDOW_WIDTH//greed

#RGB색상
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,100,0)
RED=(100,0,0)
BLUE=(0,0,100)
YELLOW=(255,255,0)
GRAY=(204,204,204)

UP=(0,-1)
DOWN=(0,1)
LEFT=(-1,0)
RIGHT=(1,0)

FPS=10

class Python(object):
    def __init__(self):
        self.create()
        self.color=GREEN
    def create(self):
        self.length=2
        self.positions = [((WINDOW_WIDTH/2),(WINDOW_HEIGHT/2))]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
    def control(self,xy):

        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        else:
            self.direction = xy

    def move(self):
        cur=self.positions[0]
        x,y=self.direction
        new=((cur[0]+(x*greed)),(cur[1]+(y*greed)))

        if new in self.positions[3:]:
            self.create()
        elif new[1]<0 or new[1]>580 or new[0]<0 or new[0]>1000:
            self.create()
        else:
            self.positions.insert(0,new)
            if len(self.positions)>self.length:
                self.positions.pop()
    def eat(self):
        self.length+=1
    
    def draw(self,s):
        for p in self.positions:
            draw_objects(surface,self.color,p)
class Feed(object):
    def __init__(self):
        self.position =(0,0)
        self.create()
        self.color=RED
    def create(self):
        self.position=(random.randint(1,greedwidth-2)*greed,random.randint(1,greedheight-2)*greed)
        #먹이생성시 가장자리에 생성되면 먹기 힘들어지끼때문에 조정
    def draw(self,s):
        draw_objects(surface,self.color,self.position)


def draw_objects(surface,color,pos):
    r=pygame.Rect(int(pos[0]),int(pos[1]),greed,greed)
    pygame.draw.rect(surface,color,r,10)

def check_eat(p,f):
    if python.positions[0] == feed.position:
        python.eat()
        feed.create()
#폰트 
def font(a,x,y,val):
    #a: 문자열
    #x,y : 위치
    #val: 변수
   fontObj = pygame.font.Font(None, 32)
   textSurfaceObj = fontObj.render(a+str(val), True, BLACK, WHITE)
   textRectObj = textSurfaceObj.get_rect()
   textRectObj.center = (x, y)
   surface.blit(textSurfaceObj, textRectObj)

if __name__=="__main__":
    python=Python()
    feed=Feed()
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT+200))
    pygame.display.set_caption("snakegame.ver0.2")
    clock=pygame.time.Clock()
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill(WHITE)
    screen.blit(surface,(0,0))
    pygame.init()

    onegame=True
    while onegame:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    python.control(UP)
                elif event.key== K_DOWN:
                    python.control(DOWN)
                elif event.key == K_LEFT:
                    python.control(LEFT)
                elif event.key == K_RIGHT:
                    python.control(RIGHT)
        surface.fill(WHITE)

        python.move()
        #격자형태로 배경 그림
        for j in range(greedheight):
            if j%2==0:
                for i in range(greedwidth):
                    if i%2==0:
                        pygame.draw.rect(surface, GRAY, (i * greed, j * greed, greed, greed),0)
            elif j%2==1:
                for k in range(greedwidth):
                    if k%2==1:
                        pygame.draw.rect(surface, GRAY, (k * greed, j * greed, greed, greed),0)
        speed=(FPS+python.length)/2
        feed.draw(surface)
        #속도와 길이 나타냄
        font("speed : ",60,620,int(speed))
        font("length : ",60,650,int(python.length))
        python.draw(surface)
        
        screen.blit(surface,(0,0))
        check_eat(python,feed)
       

        clock.tick(speed)
        pygame.display.update()
        pygame.display.flip()
