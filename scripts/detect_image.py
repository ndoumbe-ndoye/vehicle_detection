from ultralytics import YOLO
import cv2 as cv
import os


model = YOLO("yolov8n.pt")
output_dir = "detections/detection_threshold"
os.makedirs(output_dir, exist_ok=True)
all_detections = []
frames = {
    "frameV180.jpg": "frames",
    "frameV1900.jpg": "frames",
    "frameV1840.jpg": "frames",
    "frameV1560.jpg": "frames",
    "frameV62360.jpg": "frames6",
    "frameV5360.jpg": "frames5",
    "frameV660.jpg": "frames6",
    "frameV6320.jpg": "frames6",
    "frameV20.jpg": "frames2",
    "frameV260.jpg": "frames2",
    "frameV3900.jpg": "frames3",
    "frameV4640.jpg": "frames4",
    "frameV40.jpg": "frames4",
    "frameV41020.jpg": "frames4",
    "frameV41040.jpg": "frames4",
    "frameV5120.jpg": "frames5",
    "frameV2200.jpg": "frames2",
    "frameV11780.jpg": "frames",

 # annoation of the frames that we are going to be looking at and compare with mannual annotation. 
 # these frames were fully annotated    
    "frameV1140.jpg" : "frames",
    "frameV1760.jpg" : "frames",
    "frameV3200.jpg" : "frames3",
    "frameV3460.jpg" : "frames3",
    "frameV6280.jpg" : "frames6",
    "frameV6340.jpg" : "frames6",
    "frameV6580.jpg" : "frames6",
    "frameV5140.jpg" : "frames5",
    "frameV51120.jpg" : "frames5",
    "frameV20.jpg" : "frames2",
# 27 annotated frames in total.
}

with open("detections/detection_threshold/detection_threshold.txt", "w") as file:
    for filename, folder in frames.items():
        image_path = os.path.join(folder, filename)
        # this is to read the image from the path
        image = cv.imread(image_path)

        results = model(image, conf=0.4)
        single_result = results[0]

        save_path = os.path.join('detections/detection_threshold', f"{filename[:-4]}_threshold_detection.jpg")
        single_result.save(filename=save_path)
        # where looking at each box in results 
        for box in single_result.boxes:
            # this is to get the class label of the object 
            cls = int(box.cls[0])
            # this is to get the confidence score 
            conf = float(box.conf[0])
            # This is the get the coordinates of the boundding boxes 
            coords = box.xyxy[0].tolist()
            label = single_result.names[cls]
            #prints out all that information 
            #print(f"Class: {results[0].names[cls]}")
            #print(f"Confidence: {conf:.2f}")
            #print(f"Box: {coords}")
            #print()

            all_detections.append({
                "filename": filename,
                "class": label,
                "confidence": conf,
                "box": coords
            })
# now where looking at the image as a whole so we can save the results 
# saving the image with the detections drawn on it and saving the plots
            x1, y1, x2, y2 = coords
            file.write(f"{filename}, {label}, {conf:.3f}, {x1:.1f}, {y1:.1f}, {x2:.1f}, {y2:.1f}\n")
        print(f"Processed: {filename}  →  {len(single_result.boxes)} detections")

