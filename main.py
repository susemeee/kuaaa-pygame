# what a wonderful day!
# we want prof. Suho Lee!! please wake up ...

import sys #외장함수 불러옴
import pygame #파이게임 불러옴
from pygame.locals import * #파이게임의 변수들 불러옴

pygame.init() #파이게임 변수 초기화

# Define the colors we will use in RGB format
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
   
pygame.display.set_caption("냥냥이 vs 댕댕이") #제일 위의 바에 게임 이름 뜸
  
#Loop until the user clicks the close button.
done= False
clock= pygame.time.Clock()


# 플레이화면

width, height = 1167, 550                           #화면 크기
screen = pygame.display.set_mode((width, height))   
font= pygame.font.SysFont("consolas",20)            #폰트 설정


background = pygame.image.load()                    #이미지 받아오기
cat = pygame.image.load()
guide1 = pygame.image.load()                        
guide2 = pygame.image.load()


while not done:
    clock.tick(10) #1초에 10번식 화면 출력
     
    # Main Event Loop
    for eventin pygame.event.get():# 마우스, 키보드 등을 감지함
        if event.type == pygame.QUIT:# 유저가 창 닫으면
            done=True # 게임을 끝냄

        elif event.type == pygame.KEYUP: #아무 키나 누르면
            flag = True

    if flag == True:
        playscreen = playscreen()
        catdog = catdog()

        input1 = input()
        input2 = input()
        catdog.keyinput(input1,input2)


    #여기에 게임 메인 로직 써야할 것 같은데..맞나?




    pygame.display.filp()

pygame.quit()


#이 기본 세팅은 https://kkamikoon.tistory.com/129를 참고해 만들었습니다. 틀렸을지도..







class catdog:

    def __init__(self): #처음의 이닛 함수
        self.catlocation = 0
        self.doglocation = 0
        self.cathand = [False,False,False] #묵,찌,빠 순서
        self.doghand = [False,False,False]

    def start(self):
        if 

    def keyinput(self,input1,input2): #키보드 입력값은 mainlogic.py에서 지정한 글로벌 변수 catinput과 cathand를 받아옴
        if input1 = "a" or "s" or "d":
            self.catinput = input1
            self.doginput = input2
        else :
            self.doginput = input1
            self.catinput = input2

        if catinput == "a" :
            self.cathand[0] = True
        elif catinput == "s" :
            self.cathand[1] = True
        elif catinput == "d" :
            self.cathand[2] = True
        
        if doginput == "," :
            self.doghand[0] = True 
        elif doginput == "." :
            self.doghand[1] = True
        elif doginput == "/" :
            self.doghand[2] = True

    def fight(self): #승무패 알고리즘. 기본적으로 고양이 기준으로 승무패 정함.
        if (self.cathand[0] and not (self.doghand[0] or self.doghand[2]))
        or (self.cathand[1] and not (self.doghand[1] or self.doghand[0]))
        or (self.cathand[2] and not (self.doghand[2] or self.doghand[1])) :#고양이가 보로 이김
            return "win"
        elif cathand == doghand : #무승부:인풋값이 완전같음
            return "draw"
        else: #고양이가 짐
            return "lose"

    def movecat(self):
        #아래에 승무패 변수를 뭐라고 해야 하지? 아무튼 고양이의 이동을 지정함.
        if self.cathand[0] and self.fight == "win" :
            return 1
        elif self.cathand[1] and self.fight == "win" :
            return 2
        elif self.cathand[2] and self.fight == "win" :
            return 5
        else :
            return 0
    
    def movedog(self): #강아지의 이동을 지정함.
        if self.doghand[0] and self.fight == "lose" :
            return 1
        elif self.doghand[1] and self.fight == "lose" :
            return 2
        elif self.doghand[2] and self.fight == "lose" :
            return 5
        else :
            return 0

    def reset(self): # 매 판이 끝날 때마다 키입력값을 리셋함
        self.cathand = [False,False,False]
        self.doghand = [False,False,False]
    

    

class playscreen:
    def __init__(self):
        self.cat_floor = 0
        self.dog_floor = 0
        position = [[300, 360], [300, 360], [500, 370], [600, 360], [700, 350], [780, 300], [790, 220], [770, 150], [690, 110], [580, 100], [470, 100], [330, 90]]
        self.catpos = position[self.cat_floor]
        self.dogpos = position[self.dog_floor]
    

    def moving(self, catmove, dogmove):
        if catmove != 0:
            self.cat_floor += catmove                   # cat의 층수를 catmove만큼 올림
            
            if self.cat_floor >= 11:                    # cat의 층수가 11보다 크면 cat 승리
                self.catpos = position[11]
                screen.blit(cat, self.catpos)
                cat_victory()
                break
            
            self.catpos = position[self.cat_floor]      # cat의 위치 조정
            screen.blit(cat, self.catpos)
        
        elif dogmove != 0:
            self.dog_floor += dogmove                   # dog의 층수를 catmove만큼 올림
            
            if self.dog_floor >= 11:                    # dog의 층수가 11보다 크면 dog 승리
                self.dogpos = position[11]
                screen.blit(dog, self.dogpos)
                dog_victory()
                break
            
            self.dogpos = position[self.dog_floor]      # dog 위치 조정
            screen.blit(dog, self.dogpos)


    def cat_victory(self):
        

                


