import cv2

# Load the Haar Cascade for detecting eyes
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load the image
image_path = "C:/Users/roohi/Downloads/human face.jpeg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect eyes in the image
eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with detected eyes
cv2.imshow('Detected Eyes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
