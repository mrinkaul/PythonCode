import cv2
import matplotlib.pyplot as plt



image1 = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\clockimg.jpg")
print(image1.shape)
image2 = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\earthimgjpg.jpg")
print(image2.shape)
 

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.6, 0)
cv2.imshow('Weighted Image', weightedSum)
 

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()