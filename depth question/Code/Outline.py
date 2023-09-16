import numpy as np 
import cv2

# Use a raw string for the file path
src = cv2.imread(r"your image")
mask = np.zeros(src.shape, dtype=np.uint8)
w, h, c = src.shape

# Edge detection
threshold = 100
gray = cv2.Canny(src, threshold, threshold * 2)

# Save the image to a file instead of trying to display it
cv2.imwrite('output.jpg', gray)

# Find contours
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
threshold_area = 0.5

# Fill area within contours with white color
for c in cnts:
    area = cv2.contourArea(c)
    if area > threshold_area:
        cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)

# Save the mask to a file instead of trying to display it
cv2.imwrite('mask.jpg', mask)

