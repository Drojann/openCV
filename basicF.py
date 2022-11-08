import cv2 as cv

img = cv.imread('photos/f1.jpg')

cv.imshow('car', img)

#converting to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge cascade
canny= cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating image
dilated= cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding
eroded= cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

#Resize
resize= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)

#Cropping
cropped= img[100:300, 300:600]
cv.imshow('Cropped', cropped)

cv.waitKey(0)