# Advanced Ball Detection Program Readme

**Author:** Amir Kasseb

## Description

This program is a versatile tool for detecting and highlighting blue and red balls within input images. It employs computer vision techniques to identify the balls and draws bounding rectangles around them while labeling them as either "Blue Ball" or "Red Ball." The output image is then saved in a dedicated "output" folder with the same name as the input file, making it easy to locate and review the results.

## Requirements

To run this program, ensure you have the following components installed:

- **Python**: The programming language used for this script.
- **OpenCV (cv2)**: A powerful computer vision library that aids in image processing.
- **NumPy**: A fundamental library for numerical operations in Python.
- **An Input Image**: You must provide an image containing blue and red balls. Place this image in the 'images' folder.

## Installation

1. **Python Installation**: If you don't have Python installed, download it from the official website and follow the installation instructions for your operating system.

2. **Python Package Installation**: Install the required Python packages using pip if you haven't already:

   ```bash
   pip install opencv-python numpy
Create 'images' Folder: Create a folder named 'images' in the same directory as the script. This is where you'll place your input image(s).
Usage
Prepare Your Input Image: Place your input image in the 'images' folder. Ensure the image contains blue and red balls you want to detect.

Update Input Image Path: Open the script and locate the line:

python
Copy code
img = cv.imread('images/rb_021.jpg')
Replace 'images/rb_021.jpg' with the correct filename of your input image.

Run the Program: Execute the program.

Output
The program will generate an output image in the 'output' folder. The output image will have the same name as your input image, with '_output' appended to it. Detected balls will be highlighted with bounding rectangles and labeled as "Blue Ball" or "Red Ball."

Example
For instance, if you use an input image named 'rb_021.jpg', the program will save the output image as 'rb_021_output.jpg' in the 'output' folder.

Enjoy using the Advanced Ball Detection Program to enhance your image analysis tasks!
