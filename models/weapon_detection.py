# models/weapon_detection.py
import torch
import cv2


def detect_weapons(frame):
    # Load YOLOv5 model from ultralytics
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Smallest pre-trained model

    # Perform detection on the frame
    results = model(frame)

    # Process the detections
    detections = results.xyxy[0]  # Extract bounding boxes, confidence, class

    weapon_classes = ['gun', 'knife']  # Define weapons of interest

    weapons_detected = []
    for *box, conf, cls in detections:
        class_name = model.names[int(cls)]
        if class_name in weapon_classes:
            weapons_detected.append((class_name, box))

    return weapons_detected
