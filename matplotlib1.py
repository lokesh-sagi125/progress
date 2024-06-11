from matplotlib import pyplot as plt
import cv2 as cv


img = cv.imread('mt-fuji.webp')

plt.imshow(img)
plt.show()
cv.waitKey(0)