import matplotlib.pyplot as plt

def getLineInputs(var):
    print('Enter coordinates for the ', var, ' line')
    p1x = int(input('Enter the x of the first pair of coordinates:'))
    p1y = int(input('Enter the y of the first pair of coordinates:'))
    p2x = int(input('Enter the x of the second pair of coordinates:'))
    p2y = int(input('Enter the y of the second pair of coordinates:'))

    x1 = [p1x,p2x]
    y1 = [p1y,p2y]
    
    return x1,y1


# First line
x1, y1 = getLineInputs('first')

# Second Line
x2, y2 = getLineInputs('second')

# Plot
plt.plot(x1, y1, 'bo-', label = "line 1")
plt.plot(x2, y2, 'r+-', label = "line 2")
plt.title('linear graph.')
plt.legend()
plt.show()


