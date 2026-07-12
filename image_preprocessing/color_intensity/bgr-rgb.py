import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg')

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) # swaping the color channel 

cv.imshow('Image', rgb)

cv.waitKey(0)
cv.destroyAllWindows()