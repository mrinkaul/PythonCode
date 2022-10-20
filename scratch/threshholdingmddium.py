

import cv2 
import numpy as np 
   
image1 = cv2.imread('C:\\Users\\Mrinalini\\Downloads\\thresholding img.jpg') 
   
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
   

threshone = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
  
threshtwo = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)
  

cv2.imshow('Adaptive Mean', threshone)
cv2.imshow('Adaptive Gaussian', threshtwo)
  
     

if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 