import pygame
import time

pygame.init()

DisWidth= 800
DisHeight= 600
screen = pygame.display.set_mode([DisWidth, DisHeight])
pygame.display.set_caption("Click and drag to draw dots")


keep_going = True
mouse_down = False
radius = 20
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
gray =  (125,125,125)
black = (0,0,0)
purple = (138,43,226)
teal =  (32, 176, 124)
Lav_color = (230,230,250)


currentColor = red

Lavendercolor = pygame.Rect((0,0),(DisWidth,50))
purpleRect = pygame.Rect((275,0),(50,50))
redRectangle = pygame.Rect((0,0),(50,50))
blueRectangle = pygame.Rect((50,0),(50,50))
greenRectangle = pygame.Rect((100,0),(50,50))
whiteRectangle = pygame.Rect((750,0),(50,50))
grayRectangle = pygame.Rect((700,0),(50,50))

shape = 'rectangle'

def drawMenu():
    pygame.draw.rect(screen,Lav_color,Lavendercolor)
    pygame.draw.rect(screen,purple,purpleRect)
    pygame.draw.circle(screen,teal,(550,25),radius)
    pygame.draw.rect(screen,red,redRectangle)
    pygame.draw.rect(screen,blue,blueRectangle)
    pygame.draw.rect(screen,green,greenRectangle)
    pygame.draw.rect(screen,white, whiteRectangle)
    pygame.draw.rect(screen,gray,grayRectangle)

drawMenu()


while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                currentColor = black
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill((0,0,0))
                

                
            
            
    if mouse_down == True:
        spot = pygame.mouse.get_pos()
        if redRectangle.collidepoint(spot):
            currentColor = red
            mouse_down = False
        if blueRectangle.collidepoint(spot):
            currentColor = blue
            mouse_down = False
        if greenRectangle.collidepoint(spot):
            currentColor = green
            mouse_down = False
            
        if whiteRectangle.collidepoint(spot):
            radius = radius +5
            mouse_down = False
            
        if grayRectangle.collidepoint(spot):
            radius = radius - 5
            if (radius < 5 ):
                radius = radius +5
            mouse_down = False

        
        if purpleRect.collidepoint(spot):
            shape = 'rectangle'
            mouse_down = False
        if Lavendercolor.collidepoint(spot):
            mouse_down = False

        if spot[1] >= 5 and spot[1] <= 45 and spot[0] <= 570 and spot[0] >= 530:
            shape = 'circle'
            mouse_down = False
            
    if mouse_down == True:
        if shape == 'circle':
            pygame.draw.circle(screen,currentColor,spot,radius)
        else:
            Rectangle = pygame.Rect(spot,(radius,radius+radius))
            pygame.draw.rect(screen,currentColor,Rectangle)
        
        
        
    pygame.display.update()
    
pygame.quit()