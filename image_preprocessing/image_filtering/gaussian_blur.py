# smooths noise but also blurs edges.
import cv2 as cv

img = cv.imread('../../resources/image.jpeg')
cv.imshow('Image', img)

blurred = cv.GaussianBlur(img, (15,15), 0)

cv.imshow('Image', img)
cv.imshow('ImageBlurred', blurred)

cv.waitKey(0)
cv.destroyAllWindows()