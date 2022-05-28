# Enter the two points
firstx = input("Enter any number for X1: ")
secondx = input("Enter any number for X2: ")
fisrty = input("Enter any number for Y1: ")
secondy = input("Enter any number for Y2: ")

# Print them
print("("+firstx+","+fisrty+")")
print("("+secondx+","+secondy+")")

# Convert from string to numbers
x1 = float(firstx)
y1 = float(fisrty)

x2 = float(secondx)
y2 = float(secondy)


# Compute slope and intercept
slope = (y2-y1)/(x2-x1)
slopeString = str(y2-y1) + '/' + str(x2-x1)
intercept = y1 - slope*x1
theEquation = 'y = ' + str(slope) + '*x + ' + str(intercept) 
theEquation2 = 'y = ' + slopeString + '*x + ' + str(intercept) 


# Print 
print('slope:', slope)
print('y-intercept:', intercept)
print('Equation:',  theEquation)
print('Equation:',  theEquation2)

# FInd y for some values of x
for x in range (-10, 10):
    y = slope*x + intercept
    print('For x = ', x, ' y is ', y)


