# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plt 
import numpy as np
import scipy

"""
1)Getting the image
"""
img=cv2.imread("test_068.jpg") # gets images in the array format 
cv2.imshow("The_image",img)


'''
2 a) Resizing to a feasible aspect ratio
'''
#1( makes the image smaller))
#resized=cv2.resize(img,(0,0), fx=0.5,fy=0.5) #resizes both axes by half

#2(in terms of columns)
#resized=cv2.resize(img,(100,100)) #width,columns
#cv2.imshow("Resized",resized)

#3(using scipy module)
#resized=scipy.misc.imresize(img,0.75)
#cv2.imshow("Resized",resized)

#Cropping
#cropped=img[y:y+h,x:x+w]  x,y,w,h
cropped=img[140:400, 125:300]  
cv2.imshow("Cropped",cropped)

#rmake crop bigger
resized=scipy.misc.imresize(cropped,1.5)
#cv2.imshow("Resized",resized)


"""
2 b)convert to grayscale
"""
#method 1
#gray_scaled=cv2.imread("test_068.jpg",0)
#cv2.imshow("gray_image",gray_scaled)

#method 2     
gray_scaled= cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_scaled)

'''
3)THRESHOLDING (localise)
'''
#ret:holds  tranitional value  above or below which the olor becomes either black or white 
#threshed :holds the image itself

ret, threshed = cv2.threshold(gray_scaled,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Threshed",threshed)

'''
4 connected component analysis
'''
#code



#must be there 
cv2.waitKey(0)
#destroys windows with the click of a button
cv2.destroyAllWindows()