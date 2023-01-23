import numpy as np
import dlib, imutils, cv2

#cap = cv2.VideoCapture(0) #Use webcam
cap = cv2.VideoCapture("http://172.23.24.166:5000/video_feed") #Insert flask video stream IP 

#Draw line
color = (0,0,255) #Image is in BGR
stroke = 2