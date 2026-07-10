import cv2 as cv

img = cv.imread('../resources/hrimage.jpg')

def rescaleFrame(frame, scale=0.25):
    height =  int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

rescaled_image = rescaleFrame(img)
cv.imshow('Image', rescaled_image)

while True:
    key = cv.waitKey(5) & 0xFF == ord('q')

    if key == True:
        break

cv.destroyAllWindows()

