import numpy as np
import random
from imutils.object_detection import non_max_suppression
import imutils
import cv2

cap = cv2.VideoCapture('video.mp4')
count = 0
#default HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while cap.isOpened():
    ret, frame = cap.read()
    img = imutils.resize(frame, width=400)

    cv2.rectangle(img, (15, 25), (130, 100), (0, 0, 255), 5)

    cv2.imshow('Image', img)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows