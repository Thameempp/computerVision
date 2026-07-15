import cv2 as cv

img = cv.imread('../resources/image.jpeg')

if img is None:
    raise FileNotFoundError('Image path error,Check the image file path')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
adaptive = cv.adaptiveThreshold(
    gray,
    255, # max value
    cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv.THRESH_BINARY,
    11, # neighbourhood size :  must be odd
    2 # constant substracted from the calculated threshold
)

cv.imshow('Adaptive threshold',  adaptive)

cv.waitKey(0)
cv.destroyAllWindows()