import cv2 as cv

img = cv.imread("../resources/image.jpeg")

if img is None:
    raise FileNotFoundError("Image not found. Check the path.")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# simple 
thresholdvalue, binary = cv.threshold(
    gray,
    127, # threshold limit
    255, # max pixel value
    cv.THRESH_BINARY # thresholding method
    )

# binery thresholding
_, binary_inverse = cv.threshold(
    gray,
    127,
    255,
    cv.THRESH_BINARY_INV
)

# cv.imshow("Original", img)
# cv.imshow("Grayscale", gray)
cv.imshow("Binary Threshold", binary)
cv.imshow("Binary Threshold Inverse", binary_inverse)

cv.waitKey(0)
cv.destroyAllWindows()

# THRESH_BINARY       → black and white
# THRESH_BINARY_INV   → inverted black and white
# THRESH_TRUNC        → values above threshold become threshold value
# THRESH_TOZERO       → values below threshold become zero
# THRESH_TOZERO_INV   → values above threshold become zero