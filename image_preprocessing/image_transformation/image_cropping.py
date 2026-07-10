import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg')

cropped = img[0:150, 10:200] # ystart:yend, xstart:xend
cv.imshow('original', img)
cv.imshow('original', cropped)

cv.waitKey(0)
cv.destroyAllWindows()