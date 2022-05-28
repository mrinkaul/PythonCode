import pygame
import time

disWidth   = 1000
disHeight = 1000
pygame.init()
screen = pygame.display.set_mode([disWidth,disHeight])

rgb1 = input('Enter the red value for the RGB.')
rgb2 = input('Enter the green value for the RGB.')
rgb3 = input('Enter the blue value for the RGB.')



keep_going  = True
green = (rgb1, rgb2, rgb3)
black = (0,0,0)
white = (255,255,255)
radius = 50
xPos = disWidth - radius
yPos = 0 + radius



xSpeed = int(input('What is the horizontal speed you want to go at?'))
ySpeed = int(input('What is the vertical speed you want to go at?'))

while keep_going:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    xPos = xPos - xSpeed
    yPos = yPos + ySpeed
    if yPos >= disHeight-radius:
        ySpeed = ySpeed * (-1)
    
    if xPos <= 0 + radius:
        xSpeed = xSpeed * (-1)
    
    if yPos <= radius:
        ySpeed = ySpeed * (-1)
    
    if xPos >= disWidth - radius:
        xSpeed = xSpeed*(-1)
    screen.fill(black)
    pygame.draw.circle(screen,green,(xPos,yPos),radius)
    pygame.display.update()
    time.sleep(0.01)

pygame.quit()

