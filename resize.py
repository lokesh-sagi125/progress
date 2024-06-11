import cv2 as cv
def resize1(frame,scale):
    width = int(frame.shape[1]*scale)
    height =int(frame.shape[0]*scale)
    dimension =(width,height)
    final=cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    return final



img = cv.imread('cl.png')   

final1=resize1(img,10)
cv.imshow('resized',final1)

cv.waitKey(0)

cv.destroyAllWindows