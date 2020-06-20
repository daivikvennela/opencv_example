import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {},Green: {}, Blue: {}".format(r,g,b))

#change color of the pixel
image[0,0] = (0,0,225)
(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

#grab the reigion
corner = image[0:100, 0:100]
cv2.imshow("Corner just sliced", corner)
cv2.waitKey(1)

#change color of the image
image[0:100, 0:100] = (100,100,100)
cv2.imshow("Color of area changed", image )
cv2.waitKey(0)

#python3 pixel_set_get.py --image cat.jpeg 