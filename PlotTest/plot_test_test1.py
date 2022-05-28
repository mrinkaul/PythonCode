import matplotlib.pyplot as plt

print('-----line 1-----')
p1x = int(input('Enter the x of the first pair of coordinates:'))
p1y = int(input('Enter the y of the first pair of coordinates:'))
p2x = int(input('Enter the x of the second pair of coordinates:'))
p2y = int(input('Enter the y of the second pair of coordinates:'))

x1 = [p1x,p2x]
y1 = [p1y,p2y]

print('-----line 2------')
sec_p1x = int(input('Enter the x of the first pair of coordinates:'))
sec_p1y = int(input('Enter the y of the first pair of coordinates:'))
sec_p2x = int(input('Enter the x of the second pair of coordinates:'))
sec_p2y = int(input('Enter the y of the second pair of coordinates:'))

x2 = [sec_p1x,sec_p2x]
y2 = [sec_p1y,sec_p2y]

xmin = min([min(x1), min(x2)])
xmax = max([max(x1), max(x2)])
ymin = min([min(y1), min(y2)])
ymax = max([max(y1), max(y2)])

print('xmin, xmax = ', xmin, xmax)
print('ymin, ymax = ', ymin, ymax)

plt.plot(x1, y1, label = "line 1")
plt.plot(x2, y2, label = "line 2")
  

plt.title('linear graph.')
plt.legend()
plt.show()

