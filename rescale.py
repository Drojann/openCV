import cv2 as cv

#reading img
img = cv.imread('photos/sad.jpeg')
cv.imshow('Sadness', img)

#videos, images  and live video
def rescaleFrame(frame, scale=0.75):
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize (frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('resized image', resized_image)

#live video
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

#reading video
capture = cv.VideoCapture('videos/Toy_dog.mov')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release()
cv.destroyAllWindows