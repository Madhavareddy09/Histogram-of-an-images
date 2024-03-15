# Histogram-of-an-images
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the gray and color image using imread()

### Step2:
Print the image using imshow().



### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.


## Program:
```python
# Developed By : K MADHAVA REDDY
# Register Number : 212223240064
```
### Gray Image and Color Image
```python
import cv2
gray_img = cv2.imread('grayapple.jpeg')
gray_img = cv2.resize(gray_img,(300,200))
color_img = cv2.imread('mountainlake.jpg')
color_img = cv2.resize(color_img,(300,200))
cv2.imshow("Gray Image",gray_img)
cv2.imshow("Colour Image",color_img)
cv2.waitKey(0)
```
### Histogram of Grayscale Image
```python
import cv2
import matplotlib.pyplot as plt
gray_img = cv2.imread('grayapple.jpeg')
color_img = cv2.imread('mountainlake.jpg')
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
hist1 = cv2.calcHist([color_img],[1],None,[256],[0,256])
plt.figure()
plt.imshow(gray_img)
plt.show()
plt.title("Histogram")
plt.xlabel('grayscale value')
plt.ylabel('pixel count')
plt.stem(hist)
plt.show()
```
### Histogram of Color Image
```python
import cv2
import matplotlib.pyplot as plt
gray_img = cv2.imread('grayapple.jpeg')
color_img = cv2.imread('mountainlake.jpg')
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
hist1 = cv2.calcHist([color_img],[1],None,[256],[0,256])
plt.figure()
plt.imshow(color_img)
plt.show()
plt.title("Histogram")
plt.xlabel('grayscale value')
plt.ylabel('pixel count')
plt.stem(hist1)
plt.show()
```
### Histogram Equilization of GrayScale Image
```python
import cv2
gray_img = cv2.imread('grayapple.jpeg',0)
gray_img = cv2.resize(gray_img,(300,200))
cv2.imshow('Grey Scale Image',gray_img)
equ = cv2.equalizeHist(gray_img)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)
```


## Output:
### Input Grayscale Image and Color Image
![image](https://github.com/Madhavareddy09/Histogram-of-an-images/assets/145742470/4f7cfcec-c0a4-440c-bd98-97a3175b1608)


### Histogram of Grayscale Image
![image](https://github.com/Madhavareddy09/Histogram-of-an-images/assets/145742470/2348e4a3-e59d-4fd9-8afe-b86d00d435c4)

### Histogram of Color Image 
![image](https://github.com/Madhavareddy09/Histogram-of-an-images/assets/145742470/8fdba87e-2df7-4022-8e86-c99af11648cb)


### Histogram Equalization of Grayscale Image.
![image](https://github.com/Madhavareddy09/Histogram-of-an-images/assets/145742470/44fd3ae0-b885-4072-bbc4-ff55d576f4d9)




## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
