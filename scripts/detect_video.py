from ultralytics import YOLO
import cv2 as cv

model = YOLO("yolov8n.pt")
cap = cv.VideoCapture("data/traffic_vid1.mp4")

fourcc = cv.VideoWriter_fourcc(*'avc1')
out = cv.VideoWriter("data/output_tracking.mp4", fourcc, 30, (int(cap.get(3)), int(cap.get(4))))
print("VideoWriter opened:", out.isOpened())
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # this will return a list of results, one for each frame
    results = model.track(frame, persist=True)

    # print detections
    for box in results[0].boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        coords = box.xyxy[0].tolist()

        # get track ID if available
        track_id = int(box.id[0]) if box.id is not None else None
        print(f"ID {track_id} | {model.names[cls]} | conf: {conf:.2f} | {coords}")

    # draw detections ONCE per frame
    annotated_frame = results[0].plot()
    # show frame
    

    out.write(annotated_frame)
    cv.imshow("video", annotated_frame)
    # exit condition (fixed indentation)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
out.release()
cv.destroyAllWindows()