import cv2
import numpy as np
from matplotlib import pyplot as plt

 
# Read the original image
img = cv2.imread(r"C:\Users\shafina\Desktop\dipmp\d1.jpg") 
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# Sobel Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
# setting threshold of gray image
img = cv2.imread(r"C:\Users\shafina\Desktop\dipmp\d1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 107, 195, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing names of shapes
for contour in contours:

	# here we are ignoring first counter because
	# findcontour function detects whole image as shape
	if i == 0:
		i = 1
		continue

	# cv2.approxPloyDP() function to approximate the shape
	approx = cv2.approxPolyDP(
		contour, 0.01 * cv2.arcLength(contour, True), True)
	
	# using drawContours() function
	cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

	# finding center point of shape
	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	# putting shape name at center of each shape
	if len(approx) == 0:
		cv2.putText(img, 'Triangle', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
	elif len(approx) == 0:
		cv2.putText(img, 'other', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 255, 255), 2)	

	else:
		cv2.putText(img, 'circle', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		

# displaying the image after drawing contours
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()