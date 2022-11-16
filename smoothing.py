import cv2 as cv

img = cv.imread('photos/f1.jpg')
cv.imshow('car', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average image', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)