import cv2 as cv
from matplotlib import pyplot as plt 
import numpy as np



img = cv.imread('cl.png')
img2 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img2,127,255,0)

contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)


cv.drawContours(img,contours,-1,(255,255,0),2)

if contours :
    print(contours[0])

cv.imshow('original',img)
cv.waitKey(0)