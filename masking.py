import cv2 as cv
import numpy as np

img = cv.imread('photos/sad.jpeg')
cv.imshow('Sadness', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank img', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 - 90, img.shape[0]//2 -200), 100, 255, -1)
cv.imshow('Circle', circle)

masked= cv.bitwise_and(img, img,mask=circle)
cv.imshow('Masked img', masked)

cv.waitKey(0)