import cv2 as cv

img = cv.imread('../../resources/image.jpeg')
cv.imshow('Image', img)

blurred = cv.blur(img, (5,5))

cv.imshow('Image', img)
cv.imshow('ImageBlurred', blurred)

cv.waitKey(0)
cv.destroyAllWindows()