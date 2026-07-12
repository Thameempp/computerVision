import cv2 as cv
import os

cam = cv.VideoCapture(0)
count = 0

while True:
    _, frame = cam.read()
    cv.imshow('camera', frame)

    key = cv.waitKey(1)

    if key == ord('s'):
        cv.imwrite(f'captured_frames/keyframe_{count}.jpg', frame)
        count += 1

    if key == ord('q'):
        break

cam.release()
cv.destroyAllWindows()