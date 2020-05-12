import cv2
import numpy as np

img1 = cv2.imread('p1.jpg')
img2 = cv2.imread('py_logo.png')


#to rezie any image
#img2 = cv2.resize(img2, (163,122), interpolation=cv2.INTER_AREA)

#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#blow willl select all the pixel with value above 220 i.e all white and thn mask it and inv it
ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

#now black out the are of logo in ROI

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#Taknig only the region of the logo image.

img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res',img1)
cv2.waitKey()
cv2.destroyAllWindows()