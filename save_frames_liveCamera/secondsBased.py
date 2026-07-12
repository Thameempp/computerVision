import cv2 as cv
import time
import os

name = input('enter folder name: ')
folder = f'/Users/thameem/Desktop/thameem/computer_vision/captured_frames/{name}'
os.makedirs(folder, exist_ok=True)

cam = cv.VideoCapture(0)
fps = 5 
seconds = 1 / fps
last = time.time()
count = len(os.listdir(folder))

while True:
    success, frame = cam.read()

    if not success:
        break

    cv.imshow("camera", frame)

    if time.time() - last >= seconds:
        saved = cv.imwrite(f'{folder}/frame_{count}.jpg', frame)
        print(f'frame{count}', saved)
        count += 1
        last = time.time()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()