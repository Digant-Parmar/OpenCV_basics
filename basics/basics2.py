import numpy as np
import cv2

img = cv2.imread('watch2.jpeg',cv2.IMREAD_COLOR)


#in cv2 if we add more color that color gets brither rather than getting darker

#cv2.line(img,(0,0),(150,150),(0,0,255),15)
#cv2.line(file_name,Starting coordinate,end_coordinate,color,wieth)
#the above line is fore creating a line with read color
#As in openCV the color scheme is BGR insted of RGB
#hence (255,0,0)=Blue,(0,255,0)=Green , (0,0,0) = black and (255,255,255) = White


#For rectangle
#cv2.rectangle(img,(15,15),(200,150),(0,0,255),5)


#For Circle
#cv2.circle(img,(100,63),55,(0,0,255),-1)
#here -1 will fill the circle and if positive num. is writern the it is the wifth of the line


#For polygone
#pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#if reshape is require the use the next line
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img,[pts],True,(255,0,0),5)
#true is for joining the first point and the last point of the polygone

#For text

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'First',(0,120),font,1,(0,22,33),4,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()