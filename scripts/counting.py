import cv2 as cv
import numpy as np
from ultralytics import YOLO

model = YOLO("runs/detect/train-7/weights/best.pt")
cap = cv.VideoCapture("count_experiment/video5.mp4")

fourcc = cv.VideoWriter_fourcc(*'avc1')
out = cv.VideoWriter("count_experiment/output/count_5.mp4", fourcc, 30, (int(cap.get(3)), int(cap.get(4))))

star_line = (865, 2493)
end_line = (1858, 2607)


region_points = [star_line, end_line]

previous = {}
count = 0

# your 4 clicked points, defining the region to block off
blocked_vertices = np.array([[
    (16, 2441),
    (30, 2777),
    (1005, 2187),
    (493, 2046)
]], dtype=np.int32)


def block_region(image, vertices):
    mask = np.full_like(image, 255)
    cv.fillPoly(mask, vertices, (0, 0, 0))
    masked_image = cv.bitwise_and(image, mask)
    return masked_image

def side_of_line(a, b, p):
    # a, b = line endpoints (star_line, end_line)
    # p = point to test (a centroid)
    # returns positive/negative/zero depending on which side of the line p is on
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    masked_frame = block_region(frame, blocked_vertices)
    # this will return a list of results, one for each frame
    results = model.track(masked_frame, persist=True)

    # print detections
    for box in results[0].boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        coords = box.xyxy[0].tolist()
        if conf < 0.5:
            continue  

        # mid point coordinates
        cx = (coords[0] + coords[2]) / 2
        cy_val = (coords[1] + coords[3]) / 2
        centroid = (cx, cy_val)

        # get track ID if available
        track_id = int(box.id[0]) if box.id is not None else None
        old_centroid = previous.get(track_id, None)
        print(f"track_id={track_id}, old_centroid={old_centroid}, centroid={centroid}")

        if old_centroid is not None:
            old_side = side_of_line(star_line, end_line, old_centroid)
            new_side = side_of_line(star_line, end_line, centroid)
            BUFFER = 15  # tune this based on how "jittery" your detections are
            min_x = min(star_line[0], end_line[0])
            max_x = max(star_line[0], end_line[0])

            if old_side > BUFFER and new_side < -BUFFER and min_x <= centroid[0] <= max_x:
                count += 1
            elif old_side < -BUFFER and new_side > BUFFER and min_x <= centroid[0] <= max_x:
                count += 1

        previous[track_id] = centroid
        print(f"ID {track_id} | {model.names[cls]} | conf: {conf:.2f} | {coords}")

    cv.line(frame, star_line, end_line, (255, 0, 0), 10)
    # draw detections ONCE per frame, on the original (unmasked) frame
    annotated_frame = results[0].plot(img=frame)

    cv.putText(annotated_frame, f"Count: {count}",  org=(30, 200),
               fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=3,
               color=(0, 0, 255), thickness=5)

    out.write(annotated_frame)
    cv.imshow("video", annotated_frame)

    # exit condition (fixed indentation)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
out.release()
cv.destroyAllWindows()