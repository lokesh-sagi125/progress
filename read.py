import cv2 as cv
#img = cv.imread('cl.png')
#cv.imshow('logo',img)
video=cv.VideoCapture(0)
while True:
    isTrue, frame=video.read()
    cv.imshow('video',frame)

    if cv.waitKey(1)&0xff == ord('d'):
        break
    else:
        break

cv.waitKey(0)
video.release()
cv.destroyAllWindows        