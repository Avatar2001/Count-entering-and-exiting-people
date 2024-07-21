import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *

model=YOLO('yolov8s.pt')



def RGB(event,x,y,flags,param):
    if event==cv2.EVENT_MOUSEMOVE:
        colorsBGR=[x,y]
        print(colorsBGR)
        
        
cap = cv2.VideoCapture('peoplecount.mp4')



# Check if video file opened successfully
if not cap.isOpened():
    
    exit()

# Create a window named 'Video'
cv2.namedWindow('Video')

# Set mouse callback function for the 'Video' window
cv2.setMouseCallback('Video', RGB)

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Display the frame
        cv2.imshow('Video', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(6) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
