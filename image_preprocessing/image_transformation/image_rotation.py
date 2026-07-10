import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg')

rotated90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
rotated180 = cv.rotate(img, cv.ROTATE_180)

cv.imshow('Image90', rotated90)
cv.imshow('Image180', rotated180)

cv.waitKey(0)
cv.destroyAllWindows()