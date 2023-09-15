import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('images/b_009.jpg')

# Apply median filtering to reduce noise
median_filtered = cv.medianBlur(img, 11)

# Convert the filtered image to HSV color space
hsv = cv.cvtColor(median_filtered, cv.COLOR_BGR2HSV)

# Define the color range for the blue ball
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Define multiple HSV ranges for red
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 50, 50])
upper_red2 = np.array([180, 255, 255])

lower_red3 = np.array([170, 50, 50])
upper_red3 = np.array([180, 255, 255])

# Threshold the HSV image to get the blue and red balls' colors
blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
red_ball_mask1 = cv.inRange(hsv, lower_red1, upper_red1)
red_ball_mask2 = cv.inRange(hsv, lower_red2, upper_red2)
red_ball_mask3 = cv.inRange(hsv, lower_red3, upper_red3)

# Combine the red masks
red_mask = cv.bitwise_or(red_ball_mask1, red_ball_mask2, red_ball_mask3)

# Additional processing for red_mask (e.g., median blur)
red_mask = cv.medianBlur(red_mask, 11)

# Find contours in the masks
contours, _ = cv.findContours(blue_mask + red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

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

# Draw the outermost rectangles on a copy of the original image and label them
result_image = median_filtered.copy()
for x, y, w, h in outer_rectangles:
    if (x, y, w, h) in outer_rectangles:
        # If the rectangle is red, draw it in pink
        if cv.countNonZero(red_mask[y:y+h, x:x+w]) > cv.countNonZero(blue_mask[y:y+h, x:x+w]):
            label = "Red"
            color = (255, 192, 203)  # Pink color
        else:
            label = "Blue"
            color = (0, 255, 0)  # Blue color

        cv.rectangle(result_image, (x, y), (x + w, y + h), color, 2)
        cv.putText(result_image, label, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Display the original image with rectangles and labels around the balls
cv.imshow('Image with Ball Detection', result_image)
cv.waitKey(0)
cv.destroyAllWindows()
