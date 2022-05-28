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

    def followBall(self,ball):
        self.yPos = ball.pos[1]
        offset = (self.rect[1] - self.yPos) * (-0.1)
        self.rect.move_ip(0,offset)
        pygame.draw.rect(screen,self.color,self.rect)        

class Ball:
    
    def __init__(self,size,color):
        self.color = color
        self.size = size
        self.pos = [dis_width/2 , dis_height/2]
        self.speed = [-6,-6]
        #speed [xSpeed,ySpeed]
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
            yswitch = randint(0,2)
            if yswitch == 0:
                self.speed[1] = self.speed[1] * 0.9
            if yswitch != 0:
                self.speed[1] = self.speed[1] * -1.1
        
#Game Loop
            
left_bumper = Bumper ([80,50],[25,200],red)
right_bumper = Bumper ([1120,50],[25,200],blue)
#Bumper([xPos,yPos],[width,height],color)
#These change based off display width and height

ball = Ball(50,blue)
keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    ball.move()
    left_bumper.followMouse()
    right_bumper.followBall(ball)
    ball.bounce_bumper(left_bumper)
    ball.bounce_bumper(right_bumper)
    
    screen.fill(black)
    pygame.draw.rect(screen, ball.color, ball.rect)
    
    pygame.draw.rect(screen, left_bumper.color, left_bumper.rect)
    pygame.draw.rect(screen, right_bumper.color, right_bumper.rect)
    
    pygame.display.update()
    clock.tick(60)
    #This is saying that pygame will update 60 times every second

pygame.quit()  
   
   
   


