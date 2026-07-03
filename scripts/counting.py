import cv2 as cv
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
cap = cv.VideoCapture("counts/counting_video.mp4")

fourcc = cv.VideoWriter_fourcc(*'avc1')
out = cv.VideoWriter("counts/cout.mp4", fourcc, 30, (int(cap.get(3)), int(cap.get(4))))

star_line =  (1086, 1568)
end_line = (1853, 1664)

region_points = [star_line, end_line]
previous = {}
in_count = 0
out_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # this will return a list of results, one for each frame
    results = model.track(frame, persist=True)

    # print detections
    # print detections
    for box in results[0].boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        coords = box.xyxy[0].tolist()
        
        #mid point coordinates
        cx = (coords[0] + coords[2]) / 2
        cy = (coords[1] + coords[3]) / 2
        centroid = (cx, cy)
        track_id = int(box.id[0]) if box.id is not None else None
        
        old_centroid = previous.get(track_id, None)
        print(f"track_id={track_id}, old_centroid={old_centroid}, centroid={centroid}")

        if old_centroid is not None:
            old_y = old_centroid[1]
            new_y = centroid[1]
            line_y = (star_line[1] + end_line[1]) / 2
            print(line_y)
            if old_y < line_y and new_y >= line_y:
                out_count += 1
            elif old_y >= line_y and new_y < line_y:
                in_count += 1

        # get track ID if available
        previous[track_id] = centroid

        print(f"ID {track_id} | {model.names[cls]} | conf: {conf:.2f} | {coords}")
    cv.line(frame, star_line, end_line, (255, 0, 0), 10)
    
    # draw detections ONCE per frame
    annotated_frame = results[0].plot()

    # draw detections ONCE per frame
    cv.putText(annotated_frame, f"Count {out_count}" ,  org=(100, 300),
               
               fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=3,
               color=(0, 0, 255), thickness= 7)
    
    out.write(annotated_frame)

    cv.imshow("video", annotated_frame)
    # exit condition (fixed indentation)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()

out.release()
cv.destroyAllWindows()

