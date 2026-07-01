

yolo_model = {}
manual_annotations = {}
with open("detections/detection_threshold/detection_threshold.txt", "r") as file:
    for line in file:
        parts = line.split(",")
        if parts[1] == "person" or parts[1] == "traffic light":
             continue 

        if parts[0] in yolo_model:
            yolo_model[parts[0]] += 1
        else:
             yolo_model[parts[0]] = 1

    
with open("evaluation/labels_vehicle_10detections.csv", "r") as tested:
        next(tested)
        for tested_line in tested:
            parts = tested_line.split(",")
            if parts[5] in manual_annotations:
                manual_annotations[parts[5]] += 1
            else:
                manual_annotations[parts[5]] = 1
           
for frames in manual_annotations:
     true_positives = min(yolo_model[frames], manual_annotations[frames])
     precision = true_positives / yolo_model[frames]
     recall = true_positives / manual_annotations[frames]
     print(f"Frame: {frames}, Precision: {precision:.2f}, Recall: {recall:.2f}\n")