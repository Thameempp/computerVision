import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg')

resized = cv.resize(img, (600,350)) # width, height

cv.imshow('original', img)
cv.imshow('original', resized)

cv.waitKey(0)
cv.destroyAllWindows()