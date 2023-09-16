# Image Depth

# Question

if you know the actual diameter of each pole **(15cm, 10cm)**, and the Horizontal field of view**(HFOV=72)** of the camera that take the photo could you know the depth from the camera to each pole?

![poles.jpg](Image%20Depth%20a2f6c94948a941478b171e0551a35cdb/poles.jpg)

---

to get the depth of an image using the data given we will need to convert the image to black and white outlined image we could do that using the following code:

```python
import numpy as np 
import cv2

# Use a raw string for the file path
src = cv2.imread(r"Your Image")
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
```

Then we use any progroam to measure the width of the pole in pixels 

# Answer

![output.jpg](Image%20Depth%20a2f6c94948a941478b171e0551a35cdb/output.jpg)

If we assume that the the poles diameters are (15cm,10cm) and the HFOV is 72 using the the following formula 

D = (d * W) / (2 * tan(FOV / 2))


- `D` is the distance from the camera to the object.
- `d` is the actual diameter of the object.
- `W` is the width of the object in the image.
- `FOV` is the field of view of the camera.

If we assume that the average width **`W`** of the poles in the image is 40 pixels, and given that the actual diameters **`d`** of the poles are 15cm and 10cm respectively, and that the horizontal field of view **`FOV`** is 72 degrees, we can calculate the depth **`D`** for each pole using this formula. However, please note that this calculation assumes that the camera lens does not distort the image, which might not be accurate in real-world scenarios. Also, this method might not be very precise if the object is too close or too far from the camera.

## The answer is 38cm for the big pole and for the the smaller one it is 12cm
