# Object Detection Model for Egyptian Coins using YOLOv8 Ultralytics Framework

## Introduction

This project aims to create an object detection model capable of identifying Egyptian coins, specifically One pound, Half pound, and Quart pound coins, using the YOLOv8 Ultralytics framework. This README document outlines the key steps in the process, including data collection, model training, and team collaboration.

## Data Collection

### Step 1: Data Collection

- Team members contributed by collecting a diverse set of Egyptian coins.
- Coins were photographed against a different background to create a diverse dataset.
- All of this images was uploaded in a drive in order to label this images.
- [Drive where images were collected](https://github.com/your-username/your-repo)


### Step 2: Image Annotation

- Open-source annotation tools like LabelImg were used to create txt annotation files.
- Bounding boxes were drawn around each coin class (One pound, Half pound, Quart pound).

## Training the Model

### Step 3: Data Preparation

- The dataset was split into training and validation sets, ensuring balanced representation of coin classes.
- Data was organized into the YOLO format, including text files with class and bounding box information.

### Step 4: YOLOv8 Model Configuration

- YOLOv8 was selected as the object detection framework.
- Hyperparameters like learning rate, batch size, and the number of epochs were tuned for optimal performance.

### Step 5: Model Training

- The model was trained using GPUs and cloud-based services to expedite the process on google colab.
- Regular evaluation on the validation set was performed to monitor and fine-tune the model.
- The model was retrained on the same data in order to improve it's 
### Step 6: Model Evaluation

- The trained model was evaluated on a separate test dataset.
- Evaluation metrics such as precision, recall, and F1 score were calculated to assess its accuracy.

## Conclusion

This project successfully developed an object detection model using the YOLOv8 Ultralytics framework to detect and classify Egyptian coins (One pound, Half pound, Quart pound). The process involved thorough data collection, annotation, model training, and collaborative efforts among team members.

For detailed steps, code and implementation, please refer to [Drive of the model training](https://github.com/your-username/your-repo).
