import cv2 as cv

img = cv.imread('photos/f1.jpg')
cv.imshow('car', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold inverse', thresh_inv)

#Adaptive Threshholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 5)
cv.imshow('Adaptive thresh', adaptive_thresh)

cv.waitKey(0)