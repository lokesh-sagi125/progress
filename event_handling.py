import cv2 as cv
import numpy as np
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



def event_handler1(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN :
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img [y,x,2]  
      
        img2=np.zeros((200,200,3),dtype=np.uint8)
        img2[:]= (blue,green,red)
        bgr_tuple = img[y,x,:]
        color = get_color_name(bgr_tuple)
        cv.putText(img2,color,(50,100),fontFace=cv.FONT_HERSHEY_PLAIN,fontScale=1,thickness=1,color=(0,0,0))
        cv.imshow('palette',img2)




        



img= cv.imread('mt-fuji.webp')

cv.imshow('event',img)
cv.setMouseCallback('event',event_handler1)
cv.waitKey(0)
