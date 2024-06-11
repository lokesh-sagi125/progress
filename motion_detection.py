import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)


def delay(i):
    for j in range(i) :
        l=j


ret,frame1 = cap.read()
ret,frame2 = cap.read()


 
while (cap.isOpened()) :
    diff = cv.absdiff(frame1,frame2)
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    ret,thresh =  cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dialated = cv.dilate(thresh,None,iterations=3)
    contours,hierachy = cv.findContours(dialated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    
    for contour in contours :
        if cv.contourArea(contour) < 2000 :
            continue
        
        (x,y,h,w) = cv.boundingRect(contour)
        final = cv.drawContours(frame1,contours,-1,(0,0,255),2)
        #imgf =  cv.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),3)
        cv.imshow('motion detection',final)
        #delay(10000)

    
    frame1 = frame2
    ret,frame2 = cap.read()
    if cv.waitKey(1)&0xff == ord('q') : 
        break


cv.destroyAllWindows()