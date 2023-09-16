# TASK8.2-Visual Depth Estimate

# Advanced Methods for Depth Estimation from Cameras

Depth estimation from cameras is a fundamental task in computer vision, with applications ranging from autonomous driving to virtual reality. This process involves determining the distance from the camera to each point in the scene, which can be achieved using various types of cameras and methods. In this article, we will explore three main types of cameras used for depth estimation: Mono Camera, Stereo Camera, and RGBD Camera.

# Mono Camera

Monocular depth estimation involves using a single camera to estimate depth. This method is challenging task due to the loss of depth information during the image formation process. However, with the advent of deep learning techniques, monocular depth estimation has seen significant advancements.

One approach is to use Convolutional Neural Networks (CNNs) trained on large datasets of paired RGB images and corresponding depth maps. Once trained, the network can estimate depth from a single image by inferring the scene's underlying 3D structure to predict depth maps from single images. These models learn to recognize patterns and features in the image that correlate with depth, such as object size and perspective. 


---

Another method Geometry-based Methods  Geometry-based approaches utilize certain geometric cues and assumptions to estimate depth from a single camera image. These methods often rely on the principles of perspective projection, which state that objects farther away from the camera appear smaller in the image. By analyzing the size, position, and relationships between objects in the image, depth can be estimated. Techniques such as vanishing points, scale estimation, and texture gradients are commonly used in geometry-based methods.

Another way is Monocular Visual SLAM Visual Simultaneous Localization and Mapping (SLAM) is a technique that combines depth estimation with camera pose estimation to reconstruct the 3D structure of the environment in real-time. Monocular visual SLAM algorithms track visual features across frames, estimate camera motion, and simultaneously build a map of the scene. By leveraging the camera trajectory and feature tracking, depth information can be inferred.

# Stereo Camera

Stereo camera systems consist of two cameras placed side by side, similar to the human eyes, to capture a scene from two different viewpoints. These systems are widely used for depth perception and 3D reconstruction because they provide binocular vision, allowing for accurate depth estimation. Here are some features or aspects of stereo cameras:

- Disparity and Depth Estimation: The main idea behind stereo cameras is triangulation. By comparing differences between corresponding pixels in the left and right camera images, depth information can be calculated. The greater the disparity, the closer the corresponding object is to the camera. This depth information is stored in a disparity map.
- Real-Time Depth Estimation: Stereo camera systems can perform depth estimation in real-time, making them suitable for applications that require immediate feedback or control.
- Accurate Depth Perception: Stereo cameras provide more accurate depth perception compared to monocular camera methods. Since stereo cameras capture the scene from two slightly different viewpoints, they can better perceive depth.

However, there are some limitations to consider:

1. Baseline Distance Requirement: Stereo cameras require a certain baseline distance between the cameras to capture sufficient parallax for accurate depth estimation.
2. Challenging in Textureless or Occluded Regions: Stereo depth estimation can be challenging in areas with little texture or regions that are occluded, where matching corresponding pixels becomes difficult.
3. Lighting Conditions and Reflective Surfaces: Bright lighting conditions or reflective surfaces can also affect the performance of stereo vision systems.

## To get depth map and real measurements from the stereo cam you will need some steps:

1.  **Camera Calibration:** The first step is to calibrate the stereo camera system. This involves determining the intrinsic parameters (focal length, principal point, distortion coefficients) and extrinsic parameters (relative position and orientation) of each camera. Calibration can be done using a calibration pattern, such as a checkerboard, and a dedicated calibration algorithm or toolbox.
2.  **Image Rectification:** Once the stereo camera system is calibrated, the left and right images are rectified to ensure that corresponding points lie on the same scanline. Rectification simplifies the stereo correspondence process by aligning the epipolar lines in the rectified images.
3. **Stereo Correspondence**: Stereo correspondence refers to finding corresponding points between the rectified left and right images. Various algorithms can be used for this task, such as block matching, semi-global matching, or graph cuts. These algorithms search for the best matching pixel in the other image by comparing image patches or optimizing an energy function.
4.  **Disparity Calculation:** After stereo correspondence, the disparity map is calculated. The disparity map represents the horizontal shift between corresponding points in the left and right images. It is typically represented as pixel disparities or disparity values, where larger disparities indicate closer objects. The disparity values can be converted to depth values using the camera baseline and focal length.
5. **Depth Calculation:** With the disparity map and known camera parameters, the depth values for each pixel can be calculated using triangulation. Triangulation utilizes the disparity, baseline, and camera focal length to determine the 3D coordinates of each pixel in the scene. The closer an object is to the camera, the larger the disparity and the smaller the corresponding depth value.
6.  **Real Measurements:** To obtain real measurements from the depth map, you need to convert the depth values to physical units. This requires knowledge of the scale factor, which can be determined based on the scene or through additional measurements of known objects. By multiplying the depth values by the scale factor, you can obtain real-world measurements, such as distances or sizes of objects in the scene.

# RGBD Camera


An RGBD camera, also known as a depth camera, is a specialized type of camera that can provide real-time output of both depth (D) and color (RGB) data. The term RGB refers to the color model that combines red, green, and blue primary colors of light to create a wide range of colors.

One popular example of an RGBD camera is Microsoft's Kinect, which uses an infrared projector and sensor to capture depth information. This combination of color and depth capture allows for a wealth of information about the scene, making RGBD cameras ideal for tasks such as object recognition, gesture recognition, and 3D reconstruction. **Let me explain how it works:** An RGB camera captures images in red, green, and blue wavelengths, providing colored images of people and objects. On the other hand, depth information can be obtained using a depth map or image, which is created by a 3D depth sensor such as a stereo sensor or time of flight sensor.

What sets RGBD cameras apart is their ability to merge the RGB data and depth information at a pixel level, providing both types of data in a single frame. For example, DepthVista, an RGBD camera developed by e-con Systems, can deliver both depth and RGB data in a single frame.

However, it is important to note that using RGBD cameras also presents challenges, such as dealing with missing or noisy depth values. These challenges must be effectively addressed in order to achieve optimal performance.

# Comparison

| Camera Type | Advantages | Disadvantages |
| --- | --- | --- |
| Stereo Camera | - Simulates human binocular vision, giving it the ability to perceive depth. - Suitable for applications with a large field of view and for outdoor usage. | - Mediocre performance in low light. - Mediocre performance in non-textured scenes. - Active stereo will lose its effectiveness in direct sunlight and in regions with high interference of the same external light source technology used. |
| Monocular Camera | - Portability and convenience due to their small size and lightweight. - Affordable. - Reduced eye strain. | - Limited depth perception. - Narrow field of view. - Unstable image. - Limited comfort. - Limited magnification. |
| RGBD Camera | - Provides both depth (D) and color (RGB) data as the output in real-time. - Improves the accuracy of correct matching, especially for objects with similar shapes. | - The weaknesses and limitations that they present are especially from a technological point of view but also due to their principle of operation. |

## Sources

- [What are RGBD cameras? Why RGBD cameras are preferred in some embedded vision applications? - e-con Systems](https://www.e-consystems.com/blog/camera/technology/what-are-rgbd-cameras-why-rgbd-cameras-are-preferred-in-some-embedded-vision-applications/)
- [2022-01-17-monocular-depth-estimation.ipynb - Colaboratory (google.com)](https://colab.research.google.com/github/kargarisaac/blog/blob/master/_notebooks/2022-01-17-monocular-depth-estimation.ipynb)
- [https://www.connectedpapers.com/main/41c722cac91efc7ae51503969b3bc1ac40736d12/Mono Camera-3D-Multi Object-Tracking-Using-Deep-Learning-Detections-and-PMBM-Filtering/graph](https://www.connectedpapers.com/main/41c722cac91efc7ae51503969b3bc1ac40736d12/Mono%20Camera-3D-Multi%20Object-Tracking-Using-Deep-Learning-Detections-and-PMBM-Filtering/graph)
- [https://www.analyticsvidhya.com/blog/2022/01/convolutional-neural-network-an-overview/](https://www.analyticsvidhya.com/blog/2022/01/convolutional-neural-network-an-overview/)