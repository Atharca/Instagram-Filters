import cv2
import matplotlib.pyplot as plt

im=cv2.imread("crow.jpg.jpg")

#dst=cv2.GaussianBlur(im,(7,7),cv2.BORDER_DEFAULT)
#medianBlur
#dst=cv2.medianBlur(im,5)
dst=cv2.bilateralFilter(im,25,100,100,cv2.BORDER_DEFAULT)

#edges=cv2.Canny(im,50,200)
#plt.imshow(edges)
#plt.show()

plt.imshow(dst)
plt.show()