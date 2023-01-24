import numpy as np
import cv2, pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') #OpenCV Face cascade

#cap = cv2.VideoCapture(0) #Use webcam
cap = cv2.VideoCapture("http://172.23.24.166:5000/video_feed") #Insert flask video stream IP 

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trained.yml") #Trained data file
labels = {"person_name": 1}

with open("labels.pickle", 'rb') as f:
    labels = pickle.load(f) #Load labels
    labels = {v:k for k,v in labels.items} #Inverting of labels to get the proper name structure

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w] #(ycord_start, ycord_end)
        roi_color = frame[y:y+h,x:x+w]

        #Recognizer where id_ is a label and conf is a level of confidence
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 70: #Output when confidence is above 70
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_PLAIN
            name= labels[id_]
            color = (0,0,255)
            stroke = 3
            cv2.putText(frame,name,(x,y),font,color,stroke,cv2.LINE_AA)
        
        else:
            font = cv2.FONT_HERSHEY_PLAIN
            name= "Unknown"
            color = (0,0,255)
            stroke = 3
            cv2.putText(frame,name,(x,y),font,color,stroke,cv2.LINE_AA)

        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_color)
        
        #Draw box
        color = (0,0,255) #Image is in BGR
        stroke = 2
        end_x = x + w
        end_y = y + h
        cv2.rectangle(frame, (x,y), (end_x, end_y), color, stroke)

    #showImage
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()