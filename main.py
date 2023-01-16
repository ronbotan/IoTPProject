# pip install cmake dlib==19.22
# pip install face_recognition
# pip install python-ffmpeg-video-streaming

#This code is the push the openCV Webcam to Flask Web Server

import cv2
from flask import Flask, Response, render_template

app = Flask(__name__)
cam = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')

def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():  
    while True:
        success, frame = cam.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

#Start flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    