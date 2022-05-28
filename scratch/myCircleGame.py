import pygame

pygame.init()


disWidth = input('what is your width?')
disHeight = input('what is your height?')


screen = pygame.display.set_mode([disWidth,disHeight])


keep_going  = True
green = (0,205,10)
blueish = (63,100,126)
radius = 50
xPos2 = disWidth - radius*3
yPos2 = 0 + radius
xPos = disWidth - radius
yPos = 0 + radius

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.circle(screen,green,(xPos,yPos),radius)
    pygame.draw.circle(screen,blueish,(xPos2, yPos2),radius)
    pygame.display.update()

pygame.quit()
