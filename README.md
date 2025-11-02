# Edge-Linking-using-Hough-Transformm


## Developed By: R Anirudh
## Reg.No.: 212223230016
## Date : 30/10/25
## Aim:
To write a Python program to detect the lines using Hough Transform.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:

Import all the necessary modules for the program.
### Step2:

Load a image using imread() from cv2 module.
### Step3:

Convert the image to grayscale.
### Step4:

Using Canny operator from cv2,detect the edges of the image.
### Step5:

Using the HoughLinesP(),detect line co-ordinates for every points in the images.Using For loop,draw the lines on the found co-ordinates.Display the image.

## Program
## Developed By: R Anirudh
## Reg.No.: 212223230016

## Input image
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('Qn_7_.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert image to RGB for displaying
plt.title("Input Image")
plt.axis('off')
```
## Grayscale image
```
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
```
## Canny Edge detector output
```
edges = cv2.Canny(gray_image, 50, 150)
plt.imshow(edges, cmap='gray')
plt.title("Canny Edge Detector")
plt.axis('off')
```
## Display the result of Hough transform
```
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]  # Unpacking the line coordinates
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw green lines with thickness of 2
# Display the result of Hough Transform (Image with lines)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Image with lines drawn
plt.title("Result of Hough Transform")
plt.axis('off')
```

## Output
### Input image  

<img width="619" height="423" alt="image" src="https://github.com/user-attachments/assets/09033df3-096d-4944-98ef-607a2e78109f" />

### Grayscale image

<img width="596" height="426" alt="image" src="https://github.com/user-attachments/assets/98f2b0e2-efc5-43b1-8d96-a903c307209b" />

### Canny Edge detector output

<img width="606" height="442" alt="image" src="https://github.com/user-attachments/assets/3c5ab79b-5acc-4a5f-ab76-e208c44c3c0b" />

### Display the result of Hough transform

<img width="624" height="431" alt="image" src="https://github.com/user-attachments/assets/4c29ad76-f3d0-4843-93e9-c56fc4a746bc" />

## Result:
 Thus the python program to detect the lines using Hough Transform was successfully completed.
