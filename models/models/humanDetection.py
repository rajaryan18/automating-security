'''
    An example model.
    Detects Humans in the frame ans sounds an alarm that can be received by the application. 
    Please take a look at the run() function for reference.
    Contact 18aryan.raj@gmail.com for any queries.

    Avoiding dependancies is the key. If it's still required, add it in requirements.txt
    Ultralyics, torch and torchvision has been installed for your convenience.
'''

import cv2
from ultralytics import YOLO
import time

class HumanDetectionConfig():
    def __init__(self, yolo_pretrained_file, video_stream, upload_url='undefined', endpoint='192.168.0.1'):
        self.yolo_pretrained_file = yolo_pretrained_file
        self.video_stream = video_stream
        self.endpoint = endpoint
        self.upload_url = upload_url

class HumanDetection():
    def __init__(self, human_detection_config: HumanDetectionConfig):
        self.yolo_model = YOLO(human_detection_config.yolo_pretrained_file)
        self.video = cv2.VideoCapture(human_detection_config.video_stream)
        self.record = False
        self.recording = []
        self.recordings = []
        self.alarm = False
    
    def is_alarm(self):
        return self.alarm

    def beginRecording(self):
        self.record = True

    def stopRecording(self):
        self.recordings.append((self.recording, time.time()))
        self.recording = []
        self.alarm = False
        self.record = False

    def export_recording(self):
        cur_recordings = self.recordings
        self.recordings = []
        return cur_recordings
    
    def sound_alarm(self):
        self.alarm = True
        self.beginRecording()

    def run(self):
        while self.video.isOpened():
            ok, frame = self.video.read()
            if not ok:
                # Provide clean exits.
                print(f"Video ended, Closing")
                break
            if self.record:
                self.recording.append(frame)
            # Avoid verbose logs as it fills up memory
            results = self.yolo_model.predict(frame, classes=[0], stream=True, verbose=False)
            for result  in results:
                if result.boxes.data.size()[0] == 0:
                    # No detections
                    self.stopRecording()
                else:
                    # Detected human(s)
                    self.sound_alarm()