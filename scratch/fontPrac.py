import pygame
from pygame.locals import *
import time
 
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

x = "hi there noob"
zz = "Hello " + x
pygame.init()
screen = pygame.display.set_mode((640, 240))
font1 = pygame.font.SysFont('chalkduster.ttf', 72)
img1 = font1.render(zz, True, BLACK)

running = True
background = GRAY
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(background)
    screen.blit(img1, (20, 50))
    pygame.display.update()
