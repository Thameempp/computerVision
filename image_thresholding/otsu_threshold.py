import cv2 as cv

img = cv.imread('/Users/thameem/Desktop/thameem/computer_vision/resources/image.jpeg', cv.IMREAD_GRAYSCALE)

# applying otsu thresholding
threshold_value, otsu = cv.threshold(
    img, 
    0,
    255,
    cv.THRESH_BINARY + cv.THRESH_OTSU
)

print(f"threshold value : {threshold_value}")

cv.imshow('original', img)
cv.imshow('otsu', otsu)

cv.waitKey(0)
cv.destroyAllWindows()