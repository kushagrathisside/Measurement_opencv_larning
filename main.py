import cv2
import numpy as np
import utlis
##################

webcam = False
path = '1.jpg.jpeg'
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    if webcam:
        success, img = cap.read()
    else: img = cv2.imread(path)

    img, finalContours = utlis.getContours(img, showCanny=True,minArea=50000,filter=4)

    if len(finalContours)!=0:
        biggest = finalContours[0][2]
        print(biggest)

    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    cv2.imshow('original', img)
    cv2.waitKey(1)