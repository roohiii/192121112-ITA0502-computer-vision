import cv2 
import numpy as np
path =r"C:\Users\roohi\OneDrive\Pictures\Screenshots\ethics.png"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
