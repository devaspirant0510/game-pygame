import pygame
#diplay icon
icon=pygame.image.load("img/jongno.jpg")
#startscreen image
homescreen=pygame.image.load("img/homescreen.png")

#lodingbar image
loadingbar=pygame.image.load('img/1.png')
loadingbar=pygame.transform.scale(loadingbar,(700,40))
#loadingbar background
loadingem=pygame.image.load('img/loadbar.png')
loadingem=pygame.transform.scale(loadingem,(700,43))
#mod load bar
load=pygame.image.load("img/load.png")
load=pygame.transform.scale(load,(700,40))
#loading comment
loadingtext=pygame.image.load('img/text.png')

#background
background=pygame.image.load('img/bg.png')

#playbtn image
play=pygame.image.load("img/play.png")
#menubtn image
menu=pygame.image.load("img/menu.png")
sumenu=pygame.transform.scale(menu,(180,180))
#homebtn image
home=pygame.image.load("img/leader.png")
suhome=pygame.transform.scale(home,(180,180))
#restart image
restart=pygame.image.load("img/restart.png")
surestart=pygame.transform.scale(restart,(180,180))
#nextbtn image
next = pygame.image.load("img/next.png")
sunext=pygame.transform.scale(next,(180,180))
#comment pause
pauseheader=pygame.image.load("img/pause_header.png")
pauseheader=pygame.transform.scale(pauseheader,(500,200))
#wood image
mod2sucgui=pygame.image.load("img/wood.png")
mod2sucgui=pygame.transform.scale(mod2sucgui,(680,700))
#table2 image
mod2suctable=pygame.image.load("img/table2.png")
mod2suctable=pygame.transform.scale(mod2suctable,(450,350))
#comment win
wintext=pygame.image.load("img/win.png")
wintext=pygame.transform.scale(wintext,(450,200))
#explosion image
dead=pygame.image.load("img/explosion.png")
#snake head
head=pygame.image.load("img/snake2.png")
head=pygame.transform.scale(head,(20,20))
tail=pygame.image.load("img/tail1.png")
tail=pygame.transform.scale(tail,(20,20))
#image missile
bomb=pygame.image.load("img/missile.png")
bomb=pygame.transform.scale(bomb,(60,20))
rbomb=pygame.image.load("img/missile-re.png")
rbomb=pygame.transform.scale(rbomb,(60,20))
#image mirro missile
bomb_r=pygame.image.load('img/missile-re.png')
bomb_r=pygame.transform.scale(bomb_r,(60,20))
#grass image
grass = pygame.image.load('img/land_6.png')

mod2setpng=pygame.image.load("img/stagemod.png")
mod3setpng=pygame.image.load("img/perfectmod.png")
backkey=pygame.image.load("img/backkey.png")
backkey=pygame.transform.scale(backkey,(75,75))

losetext=pygame.image.load("img/lose.png")
losetext=pygame.transform.scale(losetext,(450,200))

food1=pygame.image.load("img/apple.png")
food1=pygame.transform.scale(food1,(30,30))
food2=pygame.image.load("img/pear.png")
food2=pygame.transform.scale(food2,(30,30))

howtoplay=pygame.image.load("img/howtoplay.png")
howtoplay=pygame.transform.scale(howtoplay,(1200,900))
backnum=pygame.image.load("img/01.png")
backnum=pygame.transform.scale(backnum,(168,168))

mod2background=pygame.image.load("img/wood.png")
mod2background=pygame.transform.scale(mod2background,(1400,1100))

num1=pygame.image.load("img/n1.png")
num2=pygame.image.load("img/n2.png")
num3=pygame.image.load("img/n3.png")
num4=pygame.image.load("img/n4.png")
num5=pygame.image.load("img/n5.png")

headerbtn= pygame.image.load("img/table2.png")
headerbtn=pygame.transform.scale(headerbtn,(700,200))

tile=pygame.image.load("img/land_17.png")
tile=pygame.transform.scale(tile,(20,20))

endcredit=pygame.image.load("img/endingcr.png")

lock=pygame.image.load("img/lock.png")

finish=pygame.image.load("img/Finish.png")
finish=pygame.transform.scale(finish,(160,60))
finish3=pygame.transform.scale(finish,(120,50))
finish5=pygame.transform.scale(finish,(100,30))
finishr=pygame.image.load("img/Finish_r.png")
finishr=pygame.transform.scale(finishr,(160,60))
finishb=pygame.image.load("img/finish_b.png")
finishb=pygame.transform.scale(finishb,(40,120))

tt=pygame.image.load("img/Road_02_Tile_05.png")

building1=pygame.image.load("img/building_1.png")
building1=pygame.transform.scale(building1,(150,150))
building2=pygame.image.load("img/building_2.png")
building2=pygame.transform.scale(building2,(150,150))
building3=pygame.image.load("img/building_3.png")
building3=pygame.transform.scale(building3,(150,150))
building4=pygame.image.load("img/building_4.png")
building4=pygame.transform.scale(building4,(150,150))
building5=pygame.image.load("img/building_5.png")
building5=pygame.transform.scale(building5,(150,150))
building6=pygame.image.load("img/decor_2.png")
building6=pygame.transform.scale(building6,(100,100))

sun1=pygame.image.load("img/greenery_1.png")
sun1=pygame.transform.scale(sun1,(70,150))

tree1= pygame.image.load("img/tree_1.png")
tree1 = pygame.transform.scale(tree1,(150,150))

tree2 = pygame.image.load("img/tree_2.png")
tree2 = pygame.transform.scale(tree2,(100,160))
tree3 = pygame.image.load("img/tree_3.png")
tree3 = pygame.transform.scale(tree3,(150,150))
tree8 = pygame.image.load("img/tree_8.png")
tree8 = pygame.transform.scale(tree8,(150,200))
tree11 = pygame.image.load("img/tree_11.png")

label=pygame.image.load("img/table3.png")
label=pygame.transform.scale(label,(230,140))

rock1=pygame.image.load("img/stones_1.png")
rock1=pygame.transform.scale(rock1,(75,75))
rock2=pygame.image.load("img/stones_5.png")
rock3=pygame.image.load("img/stones_6.png")
rock4=pygame.image.load("img/stones_7.png")
rock5=pygame.image.load("img/stones_9.png")

decor=pygame.image.load("img/decor_3.png")
decor=pygame.transform.scale(decor,(100,100))

car=pygame.image.load("img/decor_8.png")
car=pygame.transform.scale(car,(100,65))

mount1=pygame.image.load("img/land_3.png")
mount2=pygame.image.load("img/land_16.png")

gasi=pygame.image.load("img/greenery_2.png")
gasi=pygame.transform.scale(gasi,(20,20))

bone=pygame.image.load("img/decor_6.png")

grass2=pygame.image.load("img/greenery_6.png")

eye=pygame.image.load("img/greenery_8.png")
eye=pygame.transform.scale(eye,(50,50))

fire = pygame.image.load("img/decor_7.png")
fire = pygame.transform.scale(fire,(100,100))

mod1=pygame.image.load("img/mod1png.png")
mod2=pygame.image.load("img/mod2.png")
mod3=pygame.image.load("img/mod3.png")