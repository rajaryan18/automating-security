import cv2
from ultralytics import YOLO
import torch
import time

class HumanDetectionConfig():
    def __init__(self, yolo_pretrained_file, video_stream):
        self.yolo_pretrained_file = yolo_pretrained_file
        self.video_stream = video_stream

class HumanDetection():
    def __init__(self, human_detection_config: HumanDetectionConfig):
        self.yolo_model = YOLO(human_detection_config.yolo_pretrained_file)
        self.video = cv2.VideoCapture(human_detection_config.video_stream)
        self.record = False
        self.recording = []
        self.recordings = []
    
    def beginRecording(self):
        self.record = True

    def stopRecording(self):
        self.recordings.append((self.recording, time.time()))
        self.recording = []
        self.record = False

    def export_recording(self):
        cur_recordings = self.recordings
        self.recordings = []
        return cur_recordings
    
    def sound_alarm(self):
        self.beginRecording()

    def run(self):
        while self.video.isOpened():
            ok, frame = self.video.read()
            if not ok:
                print(f"Video ended, Closing")
                break
            if self.record:
                self.recording.append(frame)
            results = self.yolo_model.predict(frame, classes=[0], stream=True, verbose=False)
            for result  in results:
                if result.boxes.data.size()[0] == 0:
                    self.stopRecording()
                else:
                    self.sound_alarm()