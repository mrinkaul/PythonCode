import cv2
import matplotlib.pyplot as plt



image1 = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\clockimg.jpg")
print(image1.shape)
cv2.imshow("original clock", image1)

image2 = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\earthimgjpg.jpg")
print(image2.shape)
cv2.imshow("original earth", image2)

 
#to add images together
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.6, 0)
cv2.imshow('Weighted Image', weightedSum)
 
#to subtract images from eachother
sub = cv2.subtract(image2, image1)
cv2.imshow('Subtracted Image', sub)
 
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()