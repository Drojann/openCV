import cv2 as cv
import numpy as np

img = cv.imread('photos/f1.jpg')
cv.imshow('car', img)

blank = np.zeros(img.shape, dtype= 'uint8')
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

#finding edges cascades with canny(1)
canny = cv.Canny (blur, 125, 175)
cv.imshow("Canny", canny)

#binarize image with threshold(2)
""" ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh) """

#get contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)

