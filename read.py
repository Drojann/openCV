import cv2 as cv

img = cv.imread('photos/sad.jpeg')

cv.imshow('Sadness', img)

capture = cv.VideoCapture('videos/Toy_dog.mov')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release()
cv.destroyAllWindows

