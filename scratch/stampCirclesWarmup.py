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
gray = (125,125,125)
ivory = (255, 249, 234)
currentColor = white

# pygame.Rect((xCord,yCord), (width,height))
# xCord and yCord of the TOP LEFT CORNER of the rectangle
ivoryBar = pygame.Rect((0,0),(disWidth,50))
pygame.draw.rect(screen,ivory,ivoryBar)

redRectangle = pygame.Rect((0,0),(50,50))
pygame.draw.rect(screen,red,redRectangle)
blueRectangle = pygame.Rect((50,0),(50,50))
pygame.draw.rect(screen,blue,blueRectangle)
greenRectangle = pygame.Rect((100,0),(50,50))
pygame.draw.rect(screen,green,greenRectangle)

#Add these rectangles
whiteRectangle = pygame.Rect((750,0),(50,50))
pygame.draw.rect(screen,white,whiteRectangle)
grayRectangle = pygame.Rect((700,0),(50,50))
pygame.draw.rect(screen,gray,grayRectangle)

def drawMenu():
    ivoryBar = pygame.Rect((0,0),(disWidth,50))
    pygame.draw.rect(screen,ivory,ivoryBar)
    redRectangle = pygame.Rect((0,0),(50,50))
    pygame.draw.rect(screen,red,redRectangle)
    blueRectangle = pygame.Rect((50,0),(50,50))
    pygame.draw.rect(screen,blue,blueRectangle)
    greenRectangle = pygame.Rect((100,0),(50,50))
    pygame.draw.rect(screen,green,greenRectangle)
    whiteRectangle = pygame.Rect((750,0),(50,50))
    pygame.draw.rect(screen,white,whiteRectangle)
    grayRectangle = pygame.Rect((700,0),(50,50))
    pygame.draw.rect(screen,gray,grayRectangle)


    

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
                screen.fill(black)
                drawMenu()
        
    
    
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
            radius = radius + 5
            if (radius > 50):
                radius = radius - 5
            mouse_down = False
        if grayRectangle.collidepoint(spot):
            radius = radius - 5
            if (radius < 5):
                radius = radius + 5
            mouse_down = False
            
    if mouse_down == True:       
        pygame.draw.circle(screen,currentColor,spot,radius)
    
    pygame.display.update()
    
pygame.quit()




