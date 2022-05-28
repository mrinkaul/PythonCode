import pygame
import time

pygame.init()

Display_Width= 800
Display_Height= 600
screen = pygame.display.set_mode([Display_Width,Display_Height])


pygame.display.set_caption("Click and drag to draw dots")

keep_going = True
mouse_down = False
radius = 15

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE=(255,255,255)
GRAY=(190,190,190) 
currentColor = BLACK


rLen = 50
redRectangle= pygame.Rect((0,0),(rLen,rLen))
blueRectangle= pygame.Rect((50,0),(rLen,rLen))
greenRectangle= pygame.Rect((100,0),(rLen,rLen))
whiteRectangle= pygame.Rect((700,0),(rLen,rLen))
grayRectangle= pygame.Rect((750,0),(rLen,rLen))
# ((left, top), (width, height))

#buttonMinus = pygame.image.load('button_minus.png')
#buttonPlus= pygame.image.load('button_plus.png')
#buttonMinus = pygame.transform.scale(buttonMinus,(rLen,rLen))
#buttonPlus = pygame.transform.scale(buttonPlus,(rLen,rLen))
#minusRect = buttonMinus.get_rect(topleft=(150,0))
#plusRect = buttonPlus.get_rect(topleft=(200,0))
#NOT WORKING FOR SOME REASON

pygame.draw.rect(screen,RED,redRectangle)
pygame.draw.rect(screen,BLUE,blueRectangle)
pygame.draw.rect(screen,GREEN,greenRectangle)
pygame.draw.rect(screen,WHITE,whiteRectangle)
pygame.draw.rect(screen,GRAY,grayRectangle)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        #if event.type = pygame.KEYDOWN:
        #    if event.key = pygame.K_LEFT:
        #        //do whatever
    
    onButton = False
    if mouse_down == True:
        spot = pygame.mouse.get_pos()
        #screen.fill(BLACK)
        if whiteRectangle.collidepoint(spot):
            onButton = True
            if (radius < 40):
                radius = radius + 5
            time.sleep(1)
        if grayRectangle.collidepoint(spot):
            onButton = True
            if (radius > 5):
                radius = radius - 5
            time.sleep(1)
        if redRectangle.collidepoint(spot):
            onButton = True
            currentColor = RED
        if blueRectangle.collidepoint(spot):
            onButton = True
            currentColor = BLUE
        if greenRectangle.collidepoint(spot):
            onButton = True
            currentColor = GREEN
        
        if (onButton == False):
            pygame.draw.circle(screen,currentColor,spot,radius)
        if (onButton == True):
            onButton = False
    
    pygame.display.update()
    
pygame.quit()