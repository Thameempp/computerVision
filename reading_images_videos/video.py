import cv2 as cv

vid = cv.VideoCapture('../resources/video.mp4')

while True:
    isTrue,  frame = vid.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()


