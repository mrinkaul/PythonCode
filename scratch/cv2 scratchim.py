import cv2
import matplotlib.pyplot as plt

# read and print using open cv
img = cv2.imread("C:\\Users\\Mrinalini\\Downloads\\beachouse3.png", cv2.IMREAD_COLOR)
print(img.shape)
cv2.imshow("image display with cv2" , img)

# read and display using matplotlib
plt.figure(1)
c = plt.imshow(img)
plt.colorbar(c)
plt.title('image display using matplotlib')
plt.show()

# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(RGB_img.shape)
 
#Displaying image using plt.imshow() method
plt.figure(2)
plt.imshow(RGB_img)
plt.title('display converting BRG to RGB')
plt.show()

# using greyscale to read image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
plt.figure(3)
plt.imshow(gray)
plt.title('display converting BRG to GRAY')
plt.show()

#close all opened cv windows
cv2.waitKey(0)
cv2.destroyAllWindows()

