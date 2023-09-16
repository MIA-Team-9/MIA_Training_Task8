##Author : Amir Kasseb
##MIA TASK 8.3 - Advanced Ball Detection
##DESCRIPTION: This program detects blue and red balls in an image and draws rectangles around them.

# Import the necessary packages
import cv2 as cv
import numpy as np
import os 

# Load the image
img = cv.imread('images/rb_021.jpg')

# Check the dimensions of the input image
max_width = 1920  # Maximum width for the input image
max_height = 1080  # Maximum height for the input image

if img.shape[1] > max_width or img.shape[0] > max_height:
    # Calculate the scaling factor to resize the image
    scale_factor = min(max_width / img.shape[1], max_height / img.shape[0])

    # Resize the image
    img = cv.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_AREA)

# Apply median filtering to reduce noise
median_filtered = cv.medianBlur(img, 5)

# Convert the filtered image to HSV color space
hsv = cv.cvtColor(median_filtered, cv.COLOR_BGR2HSV)

# Define the color ranges for the blue and red balls
lower_blue = np.array([110, 50, 50])  # Adjust the HSV range for blue
upper_blue = np.array([130, 255, 255])  # Adjust the HSV range for blue

lower_red = np.array([0, 50, 150])  # Adjust the HSV range for red
upper_red = np.array([9, 25500, 255])  # Adjust the HSV range for red

# Threshold the HSV image to get the blue and red balls' colors
blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
red_mask = cv.inRange(hsv, lower_red, upper_red)

# Find contours in the blue mask
blue_contours, _ = cv.findContours(blue_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Find contours in the red mask
red_contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Set a minimum contour area threshold for both blue and red balls
min_contour_area = 425  # Adjust as needed for both blue and red balls

# Set a minimum height and width for red ball detections
min_red_width = 55  # Adjust as needed for red balls
min_red_height = 55  # Adjust as needed for red balls

# Set a minimum height and width for blue ball detections
min_blue_width = 0  # Adjust as needed for blue balls
min_blue_height = 0  # Adjust as needed for blue balls

# Set a range of acceptable radii for detected balls
min_radius = 55
max_radius = 125

# Create empty lists to store outer rectangles for blue and red balls
blue_rectangles = []
red_rectangles = []

# Define the Y-coordinate threshold for removing rectangles in the lower part of the screen to eliminate noise
y_threshold = img.shape[0] * 0.8  # Adjust the threshold as needed

# Iterate through the detected blue contours and draw rectangles around blue balls
for contour in blue_contours:
    contour_area = cv.contourArea(contour)
    if contour_area > min_contour_area:
        x, y, w, h = cv.boundingRect(contour)
        
        # Check if the center of the rectangle is above the Y-coordinate threshold to eliminate noise
        if (y + h // 2) < y_threshold:
            is_outer = True
            
            # Check if the width and height are above the minimum for blue balls
            if w > min_blue_width and h > min_blue_height:
                for rect in blue_rectangles:
                    # Check if the current rectangle is completely contained within another
                    if x >= rect[0] and y >= rect[1] and x + w <= rect[0] + rect[2] and y + h <= rect[1] + rect[3]:
                        is_outer = False
                        break

                if is_outer:
                    # Remove any inner rectangles that are already in the list tp eliminate noise
                    blue_rectangles = [rect for rect in blue_rectangles if not (rect[0] >= x and rect[1] >= y and rect[0] + rect[2] <= x + w and rect[1] + rect[3] <= y + h)]
                    blue_rectangles.append((x, y, w, h))

# Iterate through the detected red contours and draw rectangles around red balls
for contour in red_contours:
    contour_area = cv.contourArea(contour)
    x, y, w, h = cv.boundingRect(contour)

    # Check if the center of the rectangle is above the Y-coordinate threshold
    if (y + h // 2) < y_threshold:
        is_outer = True

        # Check if the width and height are above the minimum for red balls
        if contour_area > min_contour_area and w > min_red_width and h > min_red_height:
            for rect in red_rectangles:
                # Check if the current rectangle is completely contained within another
                if x >= rect[0] and y >= rect[1] and x + w <= rect[0] + rect[2] and y + h <= rect[1] + rect[3]:
                    is_outer = False
                    break

            if is_outer:
                # Remove any inner rectangles that are already in the list to eliminate noise from overlapping balls
                red_rectangles = [rect for rect in red_rectangles if not (rect[0] >= x and rect[1] >= y and rect[0] + rect[2] <= x + w and rect[1] + rect[3] <= y + h)]
                red_rectangles.append((x, y, w, h))

# Filter red rectangles by radius
red_rectangles = [rect for rect in red_rectangles if min_radius <= (rect[2] + rect[3]) / 2 <= max_radius]

# Draw the outermost rectangles around blue balls in green and red balls in pink on a copy of the original image
result_image = median_filtered.copy()
for x, y, w, h in blue_rectangles:
    cv.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw blue rectangles
    cv.putText(result_image, "Blue Ball", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Add label

for x, y, w, h in red_rectangles:
    cv.rectangle(result_image, (x, y), (x + w, y + h), (255, 192, 203), 2)  # Draw red rectangles
    cv.putText(result_image, "Red Ball", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 192, 203), 2)  # Add label

# Display the original image with rectangles and labels around the blue and red balls
cv.imshow('Image with Ball Detection', result_image)
# Display the original image with rectangles and labels around the blue and red balls
cv.imshow('Image with Ball Detection', result_image)

# Get the filename without the extension
filename_without_extension, _ = os.path.splitext(os.path.basename('images/rb_021.jpg'))

# Specify the output directory
output_directory = 'output/'


# Save the output image with the same name as the input file in the "output" folder
output_path = os.path.join(output_directory, f'{filename_without_extension}_output.jpg')
cv.imwrite(output_path, result_image)

cv.waitKey(0)
cv.destroyAllWindows()
