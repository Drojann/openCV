import cv2 as cv
import numpy as np

#blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

#1 paint the image a certain color
blank[200:300, 300:400]= 0,255,0
cv.imshow('green', blank)

#2 draw a rectangle
cv.rectangle(blank,(0,0), (250,500), (0,255,0), thickness=-1)
cv.imshow('rectangle', blank)

#3 draw a circle
cv.circle(blank, (250,250), 60, (0,0,255), thickness=-1)
cv.imshow("circle", blank)

#4 draw a line
cv.line(blank,(250,250), (350,400), (255,255,255), thickness=3)
cv.imshow('line', blank)

#5 write text on img
cv.putText(blank, 'Hello World', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text',blank)


cv.waitKey(0)