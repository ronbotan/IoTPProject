import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w] #(ycord_start, ycord_end)
        roi_color = frame[y:y+h,x:x+w]

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