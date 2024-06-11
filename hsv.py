import cv2 as cv
import numpy as np


def nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow('cam')
cv.createTrackbar('l_h','cam',0,255,nothing)
cv.createTrackbar('l_s','cam',0,255,nothing)
cv.createTrackbar('l_v','cam',0,255,nothing)
cv.createTrackbar('u_h','cam',0,179,nothing)
cv.createTrackbar('u_s','cam',0,255,nothing)
cv.createTrackbar('u_v','cam',0,255,nothing)

while (cap.isOpened()):
    flag,frame =cap.read()
    
    frame1=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lh = cv.getTrackbarPos('l_h','cam')
    ls = cv.getTrackbarPos('l_s','cam')
    lv = cv.getTrackbarPos('l_v','cam')
    uh = cv.getTrackbarPos('u_h','cam')
    us = cv.getTrackbarPos('u_s','cam')
    uv = cv.getTrackbarPos('u_v','cam')
    
    lb = np.array([lh,ls,lv])
    ub = np.array([uh,us,uv])

    mask = cv.inRange(frame1,lb,ub)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('cam',res)
    if cv.waitKey(1) & 0xFF == ord('q') :
        break
cap.release()
cv.destroyAllWindows()
        
    
    
    
    
    
    
