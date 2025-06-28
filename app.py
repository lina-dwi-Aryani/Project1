from flask import Flask, render_template, Response
import cv2
import numpy as np
import yaml
import os

app = Flask(__name__)

# Your existing code for YOLO setup and object detection goes here...

def generate_frames():
    while True:
        success, img = cap.read()
        if not success:
            break

        # Your existing code for object detection goes here...

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Your existing code for camera setup goes here...
    cap = cv2.VideoCapture(0)

    app.run(debug=True)