from flask import Flask
from dotenv import load_dotenv
import os
import time
import requests
from multiprocessing import Process

from entry import loader, run_model, check_alarm, alarm_monitor, models, model_config, model_endpoint

app = Flask(__name__)

@app.route('/upload_recording/<model_name>')
def upload_recording(model_name):
    recording = models[model_name].export_recording()
    url = model_config[model_name].upload_url
    # Upload at this url
    return {
        'model_name' : model_name,
        'url' : url
    }

@app.route('/run/<model_name>')
def run(model_name):
    return run_model(model_name=model_name)

@app.route('/alarm')
def alarm():
    alarms = check_alarm()
    ret = {
        'values': []
    }
    for key, value in alarms:
        if value:
            ret['values'].append({
                'model_name' : key,
                'time' : time.time(),
                'upload_url' : model_config[key].upload_url
            })
    requests.post(f"{os.environ['URL']}:{os.environ['NODE_PORT']}/alarm", data=ret)

if __name__ == '__main__':
    load_dotenv('.env')
    loader()
    process = Process(target=alarm_monitor, args=(f"{os.environ['URL']}:{os.environ['MODEL_PORT']}"))
    process.start()
    app.run(host=os.environ['URL'], port=os.environ['MODEL_PORT'], debug=True)
    process.join()