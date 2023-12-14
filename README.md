Import Libraries:

import cv2
import numpy as np
import random
import time

Load Haar Cascade Classifier:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Load the Haar Cascade classifier for face detection.

Start Webcam:

cap = cv2.VideoCapture(0)
Start capturing video from the webcam (adjust the index if you have multiple cameras).

Wait for 5 Seconds:
start_time = time.time()
while time.time() - start_time < 5:
    # ... Capture frames and display in grayscale
    
Release Webcam:
cap.release()

Release the webcam after capturing for 5 seconds.

Perform Face Detection:

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
Use the Haar Cascade classifier to detect faces in the captured frames.

Load Stickers and Set Frame Decoration:

santa = cv2.imread('santa.png', -1)
# ... (load other stickers similarly)

red_frame_color = (0, 0, 139)
red_frame_thickness_horizontal = 80

green_frame_color = (0, 100, 0)
green_frame_thickness_vertical = 80

8번부터 이어서 쓰기
