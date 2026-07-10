from ultralytics import YOLO

model = YOLO("path/to/best.pt")
metrics = model.val(data="path/to/data.yaml", split="val")  