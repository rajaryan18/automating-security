import requests
import json
from dotenv import load_dotenv
import os

# from humanDetection import HumanDetection, HumanDetectionConfig

def send_message(data, headers=None):
    if headers is None:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(f"{os.environ['URL']}:{os.environ['PORT']}", data=json.dumps(data), headers=headers, timeout=10)

def main():
    load_dotenv('../.env')
    # human_detection_config = HumanDetectionConfig(yolo_pretrained_file="yolov8n.pt", video_stream=0)
    # human_detection = HumanDetection(human_detection_config=human_detection_config)
    # human_detection.run()

if __name__ == "__main__":
    main()