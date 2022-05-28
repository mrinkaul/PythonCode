import pygame
import time
import random
# imports


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

#computers random choices
myList = ["Rock" , "Scissors" , "Paper"]
comp = random.choice(myList)
pygame.init()

#set the pygame
black = (0,0,0)
disWidth= 800
disHeight= 600
screen = pygame.display.set_mode([disWidth,disHeight])

#set up all images
compscissor  = pygame.image.load('compscissor.png')
compscissor= pygame.transform.scale(compscissor,(300,300))
compscissorRect = compscissor.get_rect(topleft=(disWidth-350,0))

comppaper  = pygame.image.load('comppaper.png')
comppaper= pygame.transform.scale(comppaper,(300,300))
comppaperRect = comppaper.get_rect(topleft=(disWidth-350,0))

comprock  = pygame.image.load('comprock.png')
comprock= pygame.transform.scale(comprock,(300,300))
comprockRect = comprock.get_rect(topleft=(disWidth-350,0))

intro  = pygame.image.load('4.png')
intro = pygame.transform.scale(intro,(300,300))
introRect = intro.get_rect(topleft=(disWidth-750,0))

sciss = pygame.image.load('3.png')
sciss = pygame.transform.scale(sciss,(200,200))
scissRect = sciss.get_rect(topleft=(disWidth-250,400))


rock = pygame.image.load('1.png')
rock = pygame.transform.scale(rock,(200,200))
rockRect = rock.get_rect(topleft=(disWidth-500,400))


paper = pygame.image.load('2.png')
paper = pygame.transform.scale(paper,(200,200))
paperRect = rock.get_rect(topleft=(disWidth-750,400))

#make user choice and instruction pictures
screen.blit(intro,introRect)
screen.blit(sciss,scissRect)
screen.blit(rock,rockRect)
screen.blit(paper,paperRect)

pygame.display.update()



mouse_down = False
keep_going = True
ask_user = 'blank'


while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
    
    if mouse_down == True:
        pygame.display.update()
        spot = pygame.mouse.get_pos()
        
        
        if scissRect.collidepoint(spot):
            ask_user = 'Scissors'
            if comp == ask_user:
                screen.blit(compscissor,compscissorRect)
                time.sleep(1)
                print("Scissors and Scissors! It's a tie!")
            elif comp == "Paper":
                screen.blit(comppaper,comppaperRect)
                time.sleep(1)
                print("Scissors beats Paper! Great job!")
            elif comp == "Rock":
                screen.blit(comprock,comprockRect)
                time.sleep(1)
                print("Rock beats Scissors! Try again!")    
            mouse_down = False
            pygame.display.update()

        
        
        if rockRect.collidepoint(spot):
            ask_user = 'Rock'
            
            if comp == ask_user:
                screen.blit(comprock,comprockRect)
                time.sleep(1)
                print("Two Rocks!It's a tie!")
            elif comp == "Paper":
                screen.blit(comppaper,comppaperRect)
                time.sleep(1)
                print("Paper beats Rock! Sorry!")
            elif comp == "Scissors":
                screen.blit(compscissor,compscissorRect)
                time.sleep(1)
                print("Rock beats Scissors! Good job!")
            mouse_down = False
            pygame.display.update()

       
       
        if paperRect.collidepoint(spot):
            ask_user = 'Paper'
            
            if comp == ask_user:
                screen.blit(comppaper,comppaperRect)
                time.sleep(1)
                print("A papaer and a paper!It's a tie!")
            elif comp == "Scissors":
                screen.blit(compscissor,compscissorRect)
                time.sleep(1)
                print("Scissors beat Paper! Better luck next time!")
            elif comp == "Rock":
                screen.blit(comprock,comprockRect)
                time.sleep(1)
                print("Paper beats rock! Good job!")
          
            mouse_down = False
            pygame.display.update()

        

pygame.quit()






