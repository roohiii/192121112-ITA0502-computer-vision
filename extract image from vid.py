import cv2
video_path = "C:/Users/roohi/OneDrive/Pictures/walking vid.mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

scale_factor = 0.5

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

new_width = int(frame_width * scale_factor)
new_height = int(frame_height * scale_factor)

frame_count = 0

while True:
    while frame_count<=5:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (new_width, new_height))
        image_name = f"frame_{frame_count}.jpg"
        cv2.imshow(image_name, frame)
        cv2.imshow('Resized Frame', frame)
        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

print(f"Extracted {frame_count} frames from the video.")
