import numpy as np
import cv2

img = cv2.imread('watch2.jpeg',cv2.IMREAD_COLOR)


#makiing one pixel of white color
img[55,55] - [255,255,255]
px = img[55,55]


#making a roi(Region Of Image) a white color box
img[100:150,100:150] = [255,255,255]


#Copy past ROI
watch_part = img[37:111,107:194]
img[0:74,0:87] = watch_part
#111-37 = 74-0 and 194-107 = 87-0 if both are equal then only this works

cv2.imshow('Image',img)
cv2.waitKey()
cv2.destroyAllWindows()
