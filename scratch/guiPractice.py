import pygame
import time

# basically warms up pygame
# basically is the green flag from Scratch
pygame.init()

disWidth= 800
disHeight= 600
screen = pygame.display.set_mode([disWidth,disHeight])
pygame.display.set_caption("Click and drag to draw dots")


keep_going = True
mouse_down = False
radius = 15
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
currentColor = white

# pygame.Rect((xCord,yCord), (width,height))
# xCord and yCord of the TOP LEFT CORNER of the rectangle
redRectangle = pygame.Rect((0,0),(50,50))
pygame.draw.rect(screen,red,redRectangle)
blueRectangle = pygame.Rect((50,0),(50,50))
pygame.draw.rect(screen,blue,blueRectangle)
greenRectangle = pygame.Rect((100,0),(50,50))
pygame.draw.rect(screen,green,greenRectangle)
blackRectangle = pygame.Rect((150,0),(50,50))
pygame.draw.rect(screen,black,blackRectangle)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
    
    if mouse_down == True:
        spot = pygame.mouse.get_pos()
        if spot[0] < 50 and spot[1] < 50:
            currentColor = red
        if spot[0] > 50 and spot[0] < 100 and spot[1] < 50:
            currentColor = blue
        if spot[0] > 100 and spot[0] < 150 and spot[1] < 50:
            currentColor = green
        if spot[0] > 150 and spot [0] < 200 and spot [1] < 50:
            currentColor = black
        pygame.draw.circle(screen,currentColor,spot,radius)
    pygame.display.update()
    
pygame.quit()





#this is for if you ever need to use a key from your keyboard
 #if event.type = pygame.KEYDOWN:
        #    if event.key = pygame.K_LEFT:
        #        //do whatever
