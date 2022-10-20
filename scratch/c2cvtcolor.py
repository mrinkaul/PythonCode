import cv2 
   
path = r'C:\\Users\\Mrinalini\\Downloads\\clockimg.jpg'
   
src = cv2.imread(path)
window_name = 'Image'
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )
cv2.imshow(window_name, image)