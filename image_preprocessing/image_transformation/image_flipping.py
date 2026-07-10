import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg')

flipped = cv.flip(img, 1)
# 1 - left to right flipping
# 0 - top to bottom
# -1 - in both direction

cv.imshow('Original', img)
cv.imshow('Flipped', flipped)

cv.waitKey(0)
cv.destroyAllWindows()