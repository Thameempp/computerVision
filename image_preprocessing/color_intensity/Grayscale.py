import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg')

normal = cv.resize(img, (500, 800))
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Image', normal)
cv.imshow('GreyScaledImage', grey)

cv.waitKey(0)
cv.destroyAllWindows()