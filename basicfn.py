import cv2 as cv
import numpy as np

img=cv.imread('mt-fuji.webp')
#grey image
img2 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',img2) 
##########################################################
#blurring an image



#edge cascade
canny = cv.Canny(img,125,175)
dialated = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('dialated',dialated)
#eroding a dialated image
cv.erode(dialated,(3,3),iterations=3 )
cropped = cv.resize(img,(300,300),interpolation= cv.INTER_CUBIC)
cv.imshow('eroded',cropped)
cv.waitKey(0)
cv.destroyAllWindows