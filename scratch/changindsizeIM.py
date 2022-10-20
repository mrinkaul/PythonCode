import cv2
import numpy as np
import matplotlib.pyplot as plt
  
FILE_NAME = 'earth.jpg'
try:

    img = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\earthimgjpg.jpg")
  

    (height, width) = img.shape[:2]
    print(height, width)

    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
  
    cv2.imwrite('result.jpg', res)

  
except IOError:
    print ('Error while reading files !!!')