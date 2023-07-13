'''
    All models to be added to ./models/
    Any pretrained model files should be added to ./models/utils/
'''
import requests
# Imports models here
from models.humanDetection import HumanDetection, HumanDetectionConfig

# model name : endpoint
model_endpoint = {}

# model_name : model_object
models = {}

# model_name : configs
model_config = {}

def loader():
    # Add objects here
    human_detection_config = HumanDetectionConfig(yolo_pretrained_file="./models/utils/yolov8n.pt", video_stream=0)
    human_detection = HumanDetection(human_detection_config=human_detection_config)
    model_endpoint['thor'] = '0.0.0.0'
    models['thor'] = human_detection
    model_config['thor'] = human_detection_config

def run_model(model_name):
    '''
    Executes the run() function in the model class. Please Ensure you have a run function
        Args:
            model_name : Name of the model that you want to execute
        Returns:
            model_endpoint : Endpoint of the running model
            upload_url : URL at which the recordings will be updated
    '''
    models[model_name].run()
    return {
        'model_endpoint' : model_endpoint[model_name],
        'upload_url': model_config[model_name].upload_url
    }

def check_alarm():
    '''
    Checks all running models for any alarms.
        Returns a Key-Value pair of model_name : alarm. alarm being a Boolean
    '''
    ret_dict = {}
    for key, value in models:
        ret_dict[key] = value.is_alarm()
    return ret_dict

def alarm_monitor(url):
    '''
    Continously Monitors all Models for any alarms.
        Args: 
            url : URL to send updates to
    '''
    while True:
        requests.get(url)