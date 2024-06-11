#change value of your image dynamically at rumtime
import cv2 as cv
import numpy as np
img =  np.zeros((200,200,3),dtype=np.uint8)

def Nothing(x) :
    y=x


b=0
g=0
r=0

cv.namedWindow('color')

cv.createTrackbar('blue','color',0,255,Nothing)

cv.createTrackbar('green','color',0,255,Nothing)

cv.createTrackbar('red','color',0,255,Nothing)
import webcolors

#event = [i for i in dir(cv) if 'EVENT'in i]
#print (event)

def get_color (color):
    array= {}
   
    for i,name in webcolors.CSS3_HEX_TO_NAMES.items():
        r,g,b = webcolors.hex_to_rgb(i)
        distr = (r-color[2])**2
        distg = (g-color[1])**2
        distb = (b-color[0])**2
        array[distr+distg+distb] = name
    return array[min(array.keys())]


def get_color_name(bgr_tuple):
    try:
        color_name = webcolors.rgb_to_name((bgr_tuple[2], bgr_tuple[1], bgr_tuple[0]))
    except ValueError:
        color_name = get_color(bgr_tuple)
    return color_name


while(1):


    cv.imshow('color',img)

    k = cv.waitKey(1) & 0xff  
    if k==27:
        break
    else :
        b=cv.getTrackbarPos('blue','color')      
        g=cv.getTrackbarPos('green','color')      
        r=cv.getTrackbarPos('red','color') 
        bgr_tuple = (b,g,r)
        color = get_color_name(bgr_tuple)
        img[:]=(b,g,r)   
        cv.putText(img,color,(50,100),fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,thickness=1,color = (255-b,255-g,255-r))
          
        
cv.destroyAllWindows()





