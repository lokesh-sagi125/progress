import cv2 as cv
import cvlib 
import numpy as np
from cvlib.object_detection import draw_bbox


cap = cv.VideoCapture(0)


while(cap.isOpened()) :
    ret,frame = cap.read()
    cap.set (3,600)
    cap.set (4,600)
    bbox,label,conf = cvlib.detect_common_objects(frame)
    final = draw_bbox(frame,bbox,label,conf)
    cv.imshow ('object',final)

    if cv.waitKey(1) & 0xff == ord(' ') :
        break


cv.destroyAllWindows()