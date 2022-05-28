import pygame

pygame.init()
keep_going = True
disWidth= 800
disHeight= 600
screen = pygame.display.set_mode([disWidth,disHeight])

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.KEYDOWN:
            line1 = input('what is your name?')
            print('Nice name!')
            line3 = input('Wanna see this cool thing i can do? type YES to proceed.')
            print('heres the cool thing! press space to see!')
        if event.type == pygame.K_SPACE:
            print('3....')
        if event.type == pygame.KEYUP:
            print('2...')
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('1...')
            q1 = input('are you ready?')
            if q1 == 'yes':
                print(' congrats' , line1 , ' i just wasted your time you noob! enjoy playing roblox!')

        
        
    



