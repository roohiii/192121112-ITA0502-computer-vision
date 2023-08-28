import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')


image_path = "C:/Users/roohi/Downloads/smile face.jpeg"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)


for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8)
    
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
        cv2.putText(roi_color, 'Smile', (sx, sy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)


cv2.imshow('Smile Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
