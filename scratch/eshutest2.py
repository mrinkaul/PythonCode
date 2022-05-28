import matplotlib.pyplot as plt
import numpy as np


    pair1x = input('Enter the x of the first pair of coordinates:')
    pair1y = input('Enter the y of the first pair of coordinates:')
    pair2x = input('Enter the x of the second pair of coordinates:')
    pair2y = input('Enter the y of the second pair of coordinates:')

def line2():
    sec_pair1x = input('Enter the x of the first pair of coordinates:')
    sec_pair1y = input('Enter the y of the first pair of coordinates:')
    sec_pair2x = input('Enter the x of the second pair of coordinates:')
    sec_pair2y = input('Enter the y of the second pair of coordinates:')


    xaxis = np.array([pair1x, pair2x])
    yaxis = np.array([pair1y, pair2y])


    xaxis2 = np.array([sec_pair1x, sec_pair2x])
    yaxis2 = np.array([sec_pair1y, sec_pair2y])

plt.plot(xaxis, yaxis)
plt.show()