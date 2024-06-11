import cv2 as cv
import numpy as np
import webcolors

#event = [i for i in dir(cv) if 'EVENT'in i]
#print (event)




def event_handler1(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN :
        co_ord= 'x:'+str(x)+'y:'+str(y)
        cv.putText(img,co_ord,(x,y),fontFace=cv.FONT_HERSHEY_PLAIN,fontScale=1,thickness=1,color=(255,255,0))
        cv.imshow('pointed',img)




        



img= cv.imread('mt-fuji.webp')

cv.imshow('pointed',img)
cv.setMouseCallback('pointed',event_handler1)
cv.waitKey(0)
