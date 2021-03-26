s=0
li=[]
name=input("저장할 파일명")
while True:
    a=input("변환시킬 명령어 : ")
    if a=='q':
        print("screen.blit 가 끝나는 부분 밑에  복붙")
        print("if ",end='')
        for i,j in enumerate(li):
            print(j,end='')

        break
    w=int(input("사진의 너비 : "))
    h=int(input("사진의 높이 : "))
    
    

    a=(a.split('(')[2].split(')')[0])
    a=a.split(',')

    x1=int(a[0])
    x2=int(a[1])
    f=open(f'{name}.txt','a',encoding='utf-8')
    f.write(f"wall{s}=Wall({x1},{x2},{w},{h})\n")
    t=f"or crash_wall(picplay1,wall{s})==True "
    li.append(t)
    s+=1
    
 

