import cv2 as cv
from ultralytics import YOLO

# build a model from scratch 

model = YOLO("yolov8n.pt")  # pretrained weights
metrics = model.val(data="fine_tune_model/config.yaml", split="val")