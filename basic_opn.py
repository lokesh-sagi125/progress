import cv2 as cv
import numpy as np



img=np.ones((500,500,3),dtype=np.uint8)
img[:]=(255,255,255)
img2= np.zeros((500,500,3),dtype=np.uint8)
img3=cv.imread('mt-fuji.webp')
cv.resize(img3,(500,500))
#img4 = cv.bitwise_or(img3,img)

#img3 = img[500:741,266:342]#== img[y1,y2:x1,x2]
#final = cv.bitwise_or(img,img3)
cv.imshow('test',img3)

cv.waitKey(0)
