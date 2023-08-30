# importing cv2
import cv2
	
# path
path = r"C:\Users\roohi\Downloads\garden pic.jpeg"
	
# Reading an image in default mode
image = cv2.imread(path)
	
# Window name in which image is displayed
window_name = 'Image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (25, 75)

# fontScale
fontScale = 0.5

# Blue color in BGR
color = (255, 255, 255)

# Line thickness of 2 px
thickness = 1

# Using cv2.putText() method
image = cv2.putText(image, 'PEACEFUL MORNING', org, font,
				fontScale, color, thickness, cv2.LINE_AA)

# Displaying the image
cv2.imshow(window_name, image)
