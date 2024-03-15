#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Developed by : K MADHAVA REDDY
# Register no : 212223240064
import cv2
gray_img = cv2.imread('grayapple.jpeg')
gray_img = cv2.resize(gray_img,(300,200))
color_img = cv2.imread('mountainlake.jpg')
color_img = cv2.resize(color_img,(300,200))
cv2.imshow("Gray Image",gray_img)
cv2.imshow("Colour Image",color_img)
cv2.waitKey(0)


# In[16]:


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


# In[18]:


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


# In[21]:


import cv2
gray_img = cv2.imread('grayapple.jpeg',0)
gray_img = cv2.resize(gray_img,(300,200))
cv2.imshow('Grey Scale Image',gray_img)
equ = cv2.equalizeHist(gray_img)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)


# In[ ]:




