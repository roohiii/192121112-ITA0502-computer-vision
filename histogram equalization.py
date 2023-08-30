import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image_path = r"C:\Users\roohi\Downloads\cat pic 1.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display the original and equalized images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')

plt.tight_layout()
plt.show()
