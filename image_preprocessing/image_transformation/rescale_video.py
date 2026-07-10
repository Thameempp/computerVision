import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    height =  int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('../resources/video.mp4')

while True:
    isTrue, frame = capture.read()

    frame_rescaled = rescaleFrame(frame)
    
    # scale before rescaling
    cv.imshow('Video', frame)
    # rescaled frame
    cv.imshow('Frame rescaled', frame_rescaled)
    
    # stop the process when we click a specific key
    key = cv.waitKey(5) & 0xFF == ord('q')
    if key == True:
        break

cv.destroyAllWindows()

