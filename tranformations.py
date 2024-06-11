import cv2 as cv
import numpy as np
import datetime as dt


img = cv.imread('mt-fuji.webp',1)

#cv.imshow('exp',img)
cap = cv.VideoCapture(0)
cap.set(3, 500)
cap.set(4,500)#camera will provide with an available resolution close to the set resolutions
text = 'width:'+str(cap.get(3))
text2 = 'height:'+ str(cap.get(4))


while (cap.isOpened()) :
 
    flag, frame = cap.read ()
    text3 = str(dt.datetime.now())
    cv.putText(frame,text,(50,100),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(255,255,0))
    cv.putText(frame,text2,(50,150),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(255,255,0))
    cv.putText(frame,text3,((frame.shape[0]-400),100),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(255,255,0))
    if flag == True:
        cv.imshow('cam' ,frame)
    if cv.waitKey(1)& 0xff == ord(' '):
       ss=frame
       break
 

      


cap.release()
cv.imshow('selfie',ss)
cv.waitKey(0)
cv.destroyAllWindows()