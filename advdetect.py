import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('images/b_000.jpg')

# Apply median filtering to reduce noise
median_filtered = cv.medianBlur(img, 11)

# Convert the filtered image to HSV color space
hsv = cv.cvtColor(median_filtered, cv.COLOR_BGR2HSV)

# Define the color ranges for the red and blue balls
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Threshold the HSV image to get the red and blue balls' colors
red_mask = cv.inRange(hsv, lower_red, upper_red)
blue_mask = cv.inRange(hsv, lower_blue, upper_blue)

# Combine the red and blue masks
mask = red_mask + blue_mask

# Find contours in the mask
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Set a minimum contour area threshold to filter out small noise
min_contour_area = 425  # Adjust as needed

# Create an empty list to store outer rectangles
outer_rectangles = []

# Iterate through the detected contours and draw rectangles around larger objects
for contour in contours:
    contour_area = cv.contourArea(contour)
    if contour_area > min_contour_area:
        x, y, w, h = cv.boundingRect(contour)
        is_outer = True

        for rect in outer_rectangles:
            # Check if the current rectangle is completely contained within another
            if x >= rect[0] and y >= rect[1] and x + w <= rect[0] + rect[2] and y + h <= rect[1] + rect[3]:
                is_outer = False
                break

        if is_outer:
            # Remove any inner rectangles that are already in the list
            outer_rectangles = [rect for rect in outer_rectangles if not (rect[0] >= x and rect[1] >= y and rect[0] + rect[2] <= x + w and rect[1] + rect[3] <= y + h)]
            outer_rectangles.append((x, y, w, h))

# Draw the outermost rectangles on a copy of the original image
result_image = median_filtered.copy()
for x, y, w, h in outer_rectangles:
    cv.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the original image with rectangles around the ball
cv.imshow('Image with Ball Detection', result_image)
cv.waitKey(0)
cv.destroyAllWindows()
