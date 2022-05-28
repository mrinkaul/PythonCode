import pygame
from random import randint

dis_width = 1200
dis_height = 720
pygame.init()
screen = pygame.display.set_mode([dis_width,dis_height])
clock = pygame.time.Clock()

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

class Bumper:
    def __init__ (self,position,size,color):
        self.xPos = position[0]
        self.yPos = position[1]
        self.width = size[0]
        self.height = size[1]
        self.color = color
        self.rect = pygame.rect.Rect(position,size)
        #self.rect[(xPos,yPos),(width,height)]
        
    def followMouse(self):
        self.yPos = pygame.mouse.get_pos()[1]
        offset = (self.rect[1] - self.yPos) * -1 
        self.rect.move_ip(0,offset)
        pygame.draw.rect(screen,self.color,self.rect)

class Ball:
    
    def __init__(self,size,color):
        self.color = color
        self.size = size
        self.pos = [dis_width/2 , dis_height/2]
        self.speed = [-6,-6]
        self.rect = pygame.rect.Rect(self.pos,(size,size))

    def move (self):
        self.bounce_edge()        
        self.rect.move_ip(self.speed)
        self.pos = self.rect[0:2]
        pygame.draw.rect(screen, self.color,self.rect)
    
    def bounce_edge(self):
        spot = self.rect[0:2]
        xPos = spot[0]
        yPos = spot[1]
        
        if xPos <= 0 or xPos >= (dis_width - self.size):
            self.speed[0] = self.speed[0] * -1
        
        if yPos <= 0 or yPos >= (dis_height - self.size):
            self.speed[1] = self.speed[1] * -1
            
    def bounce_bumper(self,bumper):
        if self.rect.colliderect(bumper):
            self.speed[0] = self.speed[0] * -1
            return True
        else:
            return False
        
#Game Loop
            
player_bumper = Bumper ([80,50],[25,200],red)
#Bumper([xPos,yPos],[width,height],color)
#These change based off display width and height

ball = Ball(30,white)
keep_going = True

bricks = []
x_scale = dis_width // 10
y_scale = dis_height // 5
x_offset = dis_width / 2


for x in range(5):
    for y in range(5):
        tempBrick = Bumper((x*x_scale+x_offset, y*y_scale),(25,100),blue)
        bricks.append(tempBrick)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    ball.move()
    player_bumper.followMouse()
    ball.bounce_bumper(player_bumper)
    for brick in bricks:
        ball.bounce_bumper(brick)
    
    
    screen.fill(black)
    pygame.draw.rect(screen, ball.color, ball.rect)
    
    #This is where we draw our paddle and brick
    pygame.draw.rect(screen, player_bumper.color, player_bumper.rect)
    for brick in bricks:
        pygame.draw.rect(screen, brick.color, brick.rect)
    
    pygame.display.update()
    clock.tick(60)
    #This is saying that pygame will update 60 times every second

pygame.quit()  
   
   
   


