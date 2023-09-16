from ultralytics import YOLO
model = YOLO(r"best.pt")
model.predict(source="test\d (1).jpg", classes=[0, 1, 2], show=False,save=True)