import numpy as np 
import cv2
#make a canvas
canvas = np.zeros((300,300,3), dtype = "uint8" )
#line
green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("The canvas", canvas)
cv2.waitKey(0)

#line
red = (255,0,0)
cv2.line(canvas,(0,0),(300,300),red, 3)
cv2.imshow("The line 2", canvas)
cv2.waitKey(0)


#draw rectangle
red = (255,0,0)
cv2.rectangle(canvas,(10,10),(100,100),red, 3)
cv2.imshow("The rectangle 1", canvas)
cv2.waitKey(0)

red = (255,234,0)
cv2.rectangle(canvas,(10,10),(100,100),red, 10)
cv2.imshow("The rectangle 2", canvas)
cv2.waitKey(0)

red = (255,234,0)
cv2.rectangle(canvas,(10,20),(100,100),red, 10)
cv2.imshow("The reactangle 3", canvas)
cv2.waitKey(0)

#circle 
blue = (0,0,255)
cv2.(canvas, (100,100), 10, blue)