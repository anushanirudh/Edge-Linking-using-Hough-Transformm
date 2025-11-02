
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1=cv2.imread('.jpg',0)
img= cv2.GaussianBlur()
plt.imshow(img)

edges1 = cv2.Canny(img,)
plt.imshow(edges1,cmap = 'gray')
plt.title('Edge Image'), plt.xticks()
plt.show()

lines=cv2.HoughLinesP(edges1,1,np.pi/180, threshold=80, minLineLength=50,maxLineGap=250)


for line in lines:
    x1, y1, x2, y2 = line [0] 
    cv2.line(edges1,(x1, y1),,3)

 
plt.imshow(edges1)

