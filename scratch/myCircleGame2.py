import pygame
import time

pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going  = True
green = (79, 116, 125)
black = (0,0,0)
white = (255,255,255)
radius = 50
xPos = 700
yPos = 100
xSpeed = 1
ySpeed = 1

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    xPos = xPos - xSpeed
    yPos = yPos + ySpeed
    screen.fill(black)
    pygame.draw.circle(screen,green,(xPos,yPos),radius)
    pygame.display.update()
    time.sleep(0.01)

pygame.quit()
