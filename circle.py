import numpy as np 
import cv2
#make a canvas
# canvas = np.zeros((300,300,3), dtype = "uint8" )
# green = (0,255,0)
# cv2.circle(canvas,(100,100), 10, green)
# cv2.imshow("Single Circle", canvas)
# cv2.waitKey(0)
# #concentric circles 
# canvas = np.zeros((300,300,3), dtype = "uint8" )
# white = (255,255,255)
# (centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
# for r in range(0,175,25):
#     cv2.circle(canvas,(centerX, centerY),r, white)
# cv2.imshow("Concentric Circles", canvas)
# cv2.waitKey(0)
#art
canvas = np.zeros((300,300,3), dtype = "uint8" )
for i in range(0,25):
 radius = np.randint(5,high = 200)
 color  = np.random.randint(0,high = 255, size =(3,)).tolist()
 pt = np.random.randint(0, high = 300, size =(2,))
 cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)