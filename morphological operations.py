import cv2
import numpy as np
image = cv2.imread(r"C:\Users\roohi\Downloads\dog pic 1.jpeg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(image, kernel, iterations=1)
eroded = cv2.erode(image, kernel, iterations=1)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated)
cv2.imshow('Eroded Image', eroded)
cv2.imshow('Opening Image', opening)
cv2.imshow('Closing Image', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
