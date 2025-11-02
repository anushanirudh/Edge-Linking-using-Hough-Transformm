# EDGE--LINKING-HOUGH-TRANSFORM
# Name : R Anirudh
# Reg no :212223230016
## Aim:
To write a Python program to detect the lines using Hough Transform.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the image

### Step2:
Convert the input image to gray to get more details

### Step3:
Apply any smoothing filter, here we apply Gaussian blur

### Step4:
Apply an edge detector

### Step5:
Apply hough transform and show the detected edge on the original image


## Program:
```Python

# Read image and convert it to grayscale image
import cv2
import numpy as np
r=cv2.imread('catt.jpg',-1)
gray=cv2.cvtColor(r,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray,(3,3),0)
cv2.imshow('origianl',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Find the edges in the image using canny detector and display
canny_edges = cv2.Canny(img, 50, 120)
cv2.imshow('canny',canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Detect points that form a line using HoughLinesP
lines =cv2.HoughLinesP(canny_edges, 1, np.pi/180,threshold = 15, minLineLength =5 ,
maxLineGap = 7)



# Draw lines on the image
for line in lines:
 x1,y1,x2,y2 = line[0]
 cv2.line(r, (x1,y1),(x2,y2),(255,0,0),3)



# Display the result
cv2.imshow('hough_detected',r)
cv2.waitKey(0)
cv2.destroyAllWindows()



```
## Output

### Input image and grayscale image
![WhatsApp Image 2024-04-10 at 11 09 31_8e788b47](https://github.com/Ragu-123/Edge-Linking-using-Hough-Transformm/assets/113915622/32386311-5adf-4c16-914d-c233b2e33777)
![WhatsApp Image 2024-04-10 at 11 09 58_4f44c31b](https://github.com/Ragu-123/Edge-Linking-using-Hough-Transformm/assets/113915622/f7d7fd9d-66a9-49b1-86c2-cba7c02f2e5c)


### Canny Edge detector output
![WhatsApp Image 2024-04-10 at 11 10 23_b31d75bd](https://github.com/Ragu-123/Edge-Linking-using-Hough-Transformm/assets/113915622/67580a82-e08a-4186-9e7f-f1aac20d2717)



### Display the result of the Hough transform
![WhatsApp Image 2024-04-10 at 11 10 52_941bf782](https://github.com/Ragu-123/Edge-Linking-using-Hough-Transformm/assets/113915622/5a5b96d4-3a64-452b-8e21-f7975d416303)




## Result:
Thus the program is written with Python and OpenCV to detect lines using Hough transform. 
