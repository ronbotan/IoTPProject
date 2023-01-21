import os
import cv2
from PIL import Image
import numpy as np
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Trainfaces")
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') #Select xml based on which one provides better accuracy
recognizer = cv2.face.LBPHFaceRecognizer_Create()
recognizer.read("trained.yml")

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label,path)

            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1
                id_ = label_ids


            pil_image = Image.open(path).convert("L") #Convert to Grayscale
            size = (550,550)
            final_image = pil_image.resize(size,Image.ANTIALIAS) #Resize image to get a better accuracy in model
            image_array = np.array(pil_image, "uint8") #Convert grayscale image to numpy array, required for training of model
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5) #Detect face in image

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

print(y_labels)
print(x_train)

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trained.yml")