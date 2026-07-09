import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

blank2 = np.zeros((800,700,3), dtype='uint8')
blank2[:] = 0,255,0
cv.imshow('Green', blank2)

while True:
    if cv.waitKey(5) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

