import cv2 as cv
import numpy as np

blank = np.zeros((1000,1000,3),dtype='uint8')#((width,height,no of color ),data type //uint8 for image)
blank[:]  = 0,0,0
#cv.rectangle(blank , (0,blank.shape[0]//2),(blank.shape[1]//2,0),(0,0,255),thickness=-1) 
#cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),blank.shape[0]//2,(255,255,0),thickness=- 1)
cv.line(blank,(0,0),(blank.shape[1],0),(255,255,255),thickness=3)



cv.putText(blank,'hello, i am not telling you my name',(0,blank.shape[1]//2),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),thickness=2)


cv.imshow('practice',blank)

cv.waitKey(0)
cv.destroyAllWindows