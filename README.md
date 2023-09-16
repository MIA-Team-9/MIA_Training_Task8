# M.I.A Training 23/24 - Electrical Team 9 - TASK 8


## Table of Contents

1. [Preface](#preface)
2. [TASK 8.1: Classical View](#task-81-classical-view)
   - [About](#about)
   - [Requirement](#requirement)
   - [Output](#output)
   - [Branch](https://github.com/MIA-Team-9/MIA_Training_Task8/blob/Task-8.1)
3. [TASK 8.2: Visual Depth Estimate](#task-82-visual-depth-estimate)
   - [About](#about-1)
   - [Requirement](#requirement-1)
   - [Output](#output-1)
   - [Branch](https://github.com/MIA-Team-9/MIA_Training_Task8/blob/Task-8.2)
4. [TASK 8.3: You Only Look Once](#task-83-you-only-look-once)
   - [About](#about-2)
   - [Requirement](#requirement-2)
   - [Output](#output-2)
   - [Branch](https://github.com/MIA-Team-9/MIA_Training_Task8/blob/Task-8.3)

---

## Preface

In the ever-evolving mission to rehabilitate their beloved planet, WALL-E and EVE encountered a new challenge. WALL-E, their steadfast and aging robot companion, had diligently served as the primary environmental caretaker for years. However, the passage of time had taken its toll on his computer vision algorithms, which were now struggling to efficiently detect and assess environmental changes.

WALL-E's optical sensors, once at the forefront of technology, were no longer keeping pace with the demands of the mission. The intricate details of the ecosystem's restoration required a higher level of precision, and WALL-E's aging algorithms simply couldn't provide the accuracy needed to identify subtle shifts in the environment. To address this critical issue, EVE, with her advanced technology and unwavering dedication to the mission, decided to step in and offer her expertise. She knew that enhancing WALL-E's computer vision algorithms was essential to the success of their ongoing efforts.

---

## TASK 8.1: Classical View

### About

The classical computer algorithms that WALL-E relied on in the past encountered limitations as the complexity of the environmental restoration mission increased, struggling to adapt to the evolving challenges such as precise object recognition in cluttered landscapes and dynamic path planning in the ever-changing terrain.

### Requirement

- There are 20 images that contain red and blue balls, implementing a classical algorithm using OpenCV, that detects the balls in the images (Classical means any).
- Detection could be a circle or bounding box around the object.

### Output

- (.py) file added to Group repo.
- The images with detections.


## TASK 8.2: Visual Depth Estimate

### About

WALL-E's depth estimate algorithm, enhanced with EVE's technological expertise, provided precise and real-time measurements of the environment's three-dimensional characteristics, enabling him to navigate challenging terrains and assess ecological changes with remarkable accuracy.

### Requirement

- Write an article about different methods to estimate depth from cameras and get a 3D view of the world, using different approaches and cameras such as Mono Camera, stereo camera, and RGBD Camera (you could use Latex, MD, or any other software).
- (BONUS) Implement Block matching using Python (algorithm that could give us a depth map from stereo images).
- **Q:** In the following image, if you know the actual diameter of each pole (15cm, 10cm), and the Horizontal field of view (HFOV=72) of the camera that took the photo, could you know the depth from the camera to each pole?



### Output

- (.pdf) file that contains the depth estimation article.
- (.py) file that contains the block-matching implementation.
- (.pdf) file showing the explanation of the question and the distances.


## TASK 8.3: You Only Look Once

### About

One day, while sifting through a particularly ancient and dilapidated pile of debris, WALL-E made an astonishing discovery. Nestled among the corroded artifacts was a collection of coins, bearing the unmistakable markings of Egyptian currency from a time when humans still called Earth home.

These coins were no ordinary currency; they were crafted from a rare alloy, known for its durability and historical significance. They had survived the ages remarkably well, offering a glimmer of the planet's once-vibrant past.

WALL-E, always the diligent collector of objects with historical value, gently scooped up the coins and brought them to EVE. With her advanced sensors and analytical capabilities, EVE quickly recognized the significance of the find. These coins were not just relics; they were a tangible link to a time when humans had thrived on Earth.

### Requirement

- Create an Object detection model (using YOLOv8 Ultralytics framework) that detects Egyptian coins. There are three classes: One pound, Half pound, Quart pound.
- Preferably collect some of all data by team members, not from the internet.
- Document each step in data collection and the training process, and show how the team collaborated on this project.

### Output

- Link to the dataset (Google Drive).
- (.pt) model weights.
- (.ipynb) training notebook.
- (.py) deployment script.
- (.pdf or .md) that includes documentation about the process.


**NOTE:**
- for more details [click me](https://drive.google.com/file/d/1vrQNU0HT5KkXrrh1A1IaT0v4LIcQsYSd/view?fbclid=IwAR3JajgHT1zKwqEH0P_u6FUzZIp3xz4TCQaFTGVx9ZIMXNHAL2X4SEYrjmY)
