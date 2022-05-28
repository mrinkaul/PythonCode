import turtle



def drawShape(sides):
    t= turtle.Turtle()
    t.pendown()
    for i in range(sides):
        t.left(360/sides)
        t.fd(3)
       
    
    
sides = 360
drawShape(sides)

