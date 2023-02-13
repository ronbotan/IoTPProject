import cv2, os, time

Path = os.path.dirname(os.path.abspath(__file__))
imgPath = os.path.join(Path, "./train_img/new")
cameraBrightness = 190
moduleval = 10  # SAVE EVERY ITH FRAME TO AVOID REPETITION
minBlur = 200  # SMALLER VALUE MEANS MORE BLURRINESS PRESENT
grayImage = False  # IMAGES SAVED COLORED OR GRAY
saveData = True  # SAVE DATA FLAG
showImage = True  # IMAGE DISPLAY FLAG
imgwidth = 250
imgHeight = 250
count = 0

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, cameraBrightness)

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(imgPath + str(countFolder)):
        countFolder = countFolder + 1
    os.makedirs(imgPath + str(countFolder))

if saveData:saveDataFunc()

while True:
    success, img = cap.read()
    if grayImage:img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if saveData:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % moduleval == 0:
            countSave = count
            currentTime = time.time()
            cv2.imwrite(imgPath + str(countFolder) + "/" + str(countSave)+"_"+ str(int(blur))+"_"+str(currentTime)+".png", img)
            countSave = countSave + 1
        count += 1

    if showImage:
        cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
