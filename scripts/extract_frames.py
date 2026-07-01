import cv2 as cv

capture = cv.VideoCapture('data/traffic_vid6.mp4')

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
frame_counter = 0

while True:
    # this is to see if the frame was succesfully read
    ret, frame = capture.read()
    # to display an indivisual frame

    if not ret:
         break     
    cv.imshow('video', frame)
    #save framw every 10 frames 
    if frame_counter % 20 == 0:
        cv.imwrite(f'frames6/frameV6{frame_counter}.jpg', frame)
    frame_counter += 1
    #stop the video from playing forever 
    # if the key d is pressed it breaks out of the loop
    if cv.waitKey(5) & 0xFF==ord('d'):
        break
capture.release() 
cv.destroyAllWindows()

