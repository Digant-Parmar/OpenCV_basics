import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch2.jpeg',cv2.IMREAD_GRAYSCALE)
#other options
#IMREAD_COLOR -1  ---this means color 1
#IMREAD_UNCHANGED  =  -1

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#plt.imshow(img,cmap='gray',interpolation = 'bicubic')
#plt.show()

cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()