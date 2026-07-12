import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg')

img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('Image', img)
cv.imshow('hsvImage', hsv)

cv.waitKey(0)
cv.destroyAllWindows()