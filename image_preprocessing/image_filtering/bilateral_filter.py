# smooths noise while keeping edges sharper.
import cv2 as cv

img = cv.imread('../../resources/image.jpeg')
cv.imshow('Image', img)

if img is None:
    raise FileNotFoundError('Image not found. check the image path')
else:
    bilat = cv.bilateralFilter(
        img, 
        d = 9, 
        sigmaColor=75.0, 
        sigmaSpace=75.0
        )

cv.imshow('Image', img)
cv.imshow('Bilateral filter', bilat)

cv.waitKey(0)
cv.destroyAllWindows()