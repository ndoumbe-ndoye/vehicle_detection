import cv2 as cv
cap = cv.VideoCapture("count_experiment/video5.mp4")
ret, frame = cap.read()
cap.release()

def show_coordinates(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"Clicked at: ({x}, {y})")

cv.namedWindow("frame")
cv.setMouseCallback("frame", show_coordinates)
star_line =  (511, 1862)
end_line = (1736, 1942)
cv.line(frame, star_line, end_line, (0, 255, 0), 3)

cv.imshow("frame", frame)
cv.waitKey(0)
cv.destroyAllWindows()
