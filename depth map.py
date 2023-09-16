import numpy as np
import cv2

def block_matching(left_image, right_image, block_size=5, search_range=30):
    # Get the dimensions of the images
    height, width = left_image.shape

    # Create an output depth map with the same dimensions as the input images
    depth_map = np.zeros_like(left_image, dtype=np.float32)

    # Compute half the block size for convenience
    half_block_size = block_size // 2

    # Iterate over each pixel in the left image
    for y in range(half_block_size, height - half_block_size):
        for x in range(half_block_size, width - half_block_size):
            # Extract the block from the left image
            left_block = left_image[y - half_block_size: y + half_block_size + 1,
                                    x - half_block_size: x + half_block_size + 1]

            # Initialize the best disparity and minimum cost
            best_disparity = 0 # difference in position of corresponding points between a pair of stereo images due to different view points.
            min_cost = float('inf') # difference between corresponding blocks in the left and right images.

            # Compute the search range limits
            min_x = max(x - search_range, half_block_size)
            max_x = min(x + search_range, width - half_block_size)

            # Iterate over the search range in the right image
            for d in range(min_x, max_x):
                # Extract the block from the right image
                right_block = right_image[y - half_block_size: y + half_block_size + 1,
                                          d - half_block_size: d + half_block_size + 1]

                # Compute the sum of absolute differences (SAD) between the blocks
                cost = np.sum(np.abs(left_block - right_block))

                # Update the best match if the cost is lower
                if cost < min_cost:
                    min_cost = cost
                    best_disparity = d - x

            # Perform sub-pixel interpolation
            if best_disparity > min_x and best_disparity < max_x - 1:
                # Compute the sub-pixel disparity using parabolic interpolation
                disparity_left = depth_map[y, x - 1]
                disparity_right = depth_map[y, x + 1]
                delta = (disparity_right - disparity_left) / 2.0
                subpixel_disparity = best_disparity + delta
                depth_map[y, x] = subpixel_disparity
            else:
                # Use the best integer disparity if sub-pixel interpolation is not possible
                depth_map[y, x] = best_disparity

    return depth_map

def refine_disparity(depth_map, left_image):
    # Set the parameters for bilateral filtering
    sigma_color = 20
    sigma_spatial = 20
    iterations = 3

    # Convert the depth map to 8-bit for bilateral filtering
    depth_map_8bit = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Perform bilateral filtering on the depth map
    for _ in range(iterations):
        depth_map_8bit = cv2.bilateralFilter(depth_map_8bit, 5, sigma_color, sigma_spatial)

    # Convert the filtered depth map back to float32
    refined_depth_map = cv2.normalize(depth_map_8bit, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_32F)

    # Resize the refined depth map to match the original image size
    refined_depth_map = cv2.resize(refined_depth_map, left_image.shape[::-1])

    return refined_depth_map

# Load the left and right images
# 'left_image.png' and 'right_image.png' should be replaced with the actual paths of left and right stereo images.
left_image = cv2.imread('left_image.png', cv2.IMREAD_GRAYSCALE)
right_image = cv2.imread('right_image.png', cv2.IMREAD_GRAYSCALE)

# Apply block matching to generate the initial depth map
depth_map = block_matching(left_image, right_image, block_size=5, search_range=30)

# Perform disparity refinement
refined_depth_map = refine_disparity(depth_map, left_image)

# Display the refined depth map
cv2.imshow('Refined Depth Map', refined_depth_map / np.max(refined_depth_map))
cv2.waitKey(0)
cv2.destroyAllWindows()