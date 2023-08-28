import cv2
img=cv2.imread( r"C:\Users\roohi\Downloads\scenery.jpeg")
cv2.imshow('original',img)
cv2.waitKey()
img_Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_Gray,(3,3),0)
sobelx=cv2.Sobel(src=img_blur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
cv2.imshow('Sobel X',sobelx)
cv2.waitKey()
