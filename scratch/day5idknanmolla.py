import pygame
import time
pygame.init()

disWidth= 800
disHeight= 600
screen = pygame.display.set_mode([disWidth,disHeight])

#First load images
buttonMinus = pygame.image.load('button_minus.png')
buttonPlus = pygame.image.load('button_plus.png')
#Then scale them to size
buttonMinus = pygame.transform.scale(buttonMinus,(50,50))
buttonPlus = pygame.transform.scale(buttonPlus,(50,50))
#Then put them where they need to be
minusRect = buttonMinus.get_rect(topleft=(disWidth-100,0))
plusRect = buttonPlus.get_rect(topleft=(disWidth-50,0))

mouse_down = False
keep_going = True
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
        if plusRect.collidepoint(spot):
            print ("clicked on plus")
            mouse_down = False
        if minusRect.collidepoint(spot):
            print ("clicked on minus")
            mouse_down = False
    
    #How we draw IMAGES on the Screen!
    screen.blit(buttonMinus,minusRect)
    screen.blit(buttonPlus,plusRect)
    pygame.display.update()
pygame.quit()