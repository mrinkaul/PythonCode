class Rectangle :
    sides = 4
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        
    def area(self):
        return (self.width * self.height)
pygame.init()
screen = pygame.display.set_mose([800,600])
        
        
blue = (0,0,255)
red = (255,0,0)
blueRect = Rectangle (20,40,blue)
redRect = Rectangle(90,10,red)

keep_going = True

while keep_going:
    
