import cv2 as cv

img = cv.imread('../resources/image.jpeg')
print(img.shape)
cv.imshow("Image", img)

while True:
    key = cv.waitKey(1)
    if key == ord('q'):
        break


cv.destroyAllWindows()