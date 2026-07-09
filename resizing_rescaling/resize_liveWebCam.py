import cv2 as cv

# resizing a live video
def change_reso(width, height):
    capture.set(4, width)
    capture.set(3, height)

# reading videos
capture = cv.VideoCapture(1)
change_reso(520, 420)
while True:
    ret, frame = capture.read()

    if ret:
        cv.imshow('video', frame)
        key = cv.waitKey(20) & 0xFF == ord('q')
        if key:
            break

capture.release()
cv.destroyAllWindows()


