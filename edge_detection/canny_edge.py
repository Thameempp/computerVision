import cv2 as cv

img = cv.imread('../resources/image.jpeg')

gray = cv.cvtColor(img,  cv.COLOR_BGR2GRAY)

blurred = cv.GaussianBlur(gray, (5,5), 0)

edges = cv.Canny(
    blurred,
    50,
    150
)
# The values 50 and 150 are threshold values.
# Below 50        → rejected as an edge
# Above 150       → accepted as a strong edge
# Between 50–150  → accepted only when connected to a strong edge

cv.imshow('Original', img)
cv.imshow('canny edges', edges)

cv.waitKey(0)
cv.destroyAllWindows()