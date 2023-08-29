# Python3 program to draw line
# shape on solid image
import numpy as np
import cv2

# Creating a black image with 3 channels
# RGB and unsigned int datatype
img = np.zeros((400, 400, 3), dtype = "uint8")

# Creating line
cv2.line(img, (20, 160), (100, 160), (0, 0, 255), 10)

cv2.imshow('dark', img)

# Allows us to see image
# until closed forcefully
cv2.waitKey(0)
cv2.destroyAllWindows()
