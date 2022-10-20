import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\clockimg.jpg")
print(img1.shape)
cv2.imshow("original clock", img1)

img2 = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\earthimgjpg.jpg")
print(img2.shape)
cv2.imshow("original earth", img2)

dest_and = cv2.bitwise_and(img2, img1, mask = None)
 
# the window showing output image
# with the Bitwise AND operation
# on the input images
cv2.imshow('Bitwise And', dest_and)




if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()