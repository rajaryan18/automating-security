# All in One Security
Trackers, Detectors and other Deep Learning Tools are great for automating many tasks specially security. It is fast, reliable and very convenient to use.  

But we often require multiple models running simultaneously which can be rather cumbersome to maintain and synchronize requiring multiple devices or packages.  

This project aims at providing a solution for the above problem.  


**Note**: You will need Docker installed to run the project  


### To clone the Project
In the terminal, run the following the commands  

`git clone https://github.com/rajaryan18/automating-security.git`  

`git branch -M main`  

The project consists of 2 main parts. The **models** section where one can store all the Deep Learning models and the **backend** section that connects to all these models and provides APIs for the same. It also regularly uploads information on Blockchain so that it cannot be tampered with.  

### The Backend Section
Run the following command in the terminal,  

`cd backend`  

`docker run`  

An admin page will open at `http://localhost:5500` You will be prompted for your data and then the admin page will open with more options.  

Here you can add devices, check device log etc.  

The blockchain is handled by the application.  

### The Model Section
Add your model that contains a `run()` function responsible for running the model, `sound_alarm()` that triggers an emergency message and `export recording()` that can be used to take the recordings from time to time. The last 2 are not necessay but recommended. It can have getter functions that return the current state of detection/tracking. An example model (Human Detector in `/models/models/humanDetection.py`) has been already set up.  

In `app.py` import the model and create it's object in the `main()` function.  

In the terminal, run the following commands.  

`cd models`  

`docker run`  

Anytime you wish to add a new model, interrupt the process (using `Ctrl C`) and repeat the above steps.  
Take special care of the number of models being added to your application. The device running the application must also be considered while adding models.