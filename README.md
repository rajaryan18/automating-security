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

### The Backend Section<
Run the following command in the terminal,  

`cd backend`  

`docker run`  

An admin page will open at `http://localhost:5500` You will be prompted for your data and then the admin page will open with more options.  

Here you can add devices, check device log etc.  

The blockchain is handled by the application.  

### The Model Section
Add your model that contains a `run()` function responsible for running the model. It can have getter function that returns the current state of detection/tracking.  

In `app.py` import the model and create it's object in the `main()` function.  

In the terminal, run the following commands.  

`cd models`  

`docker run`  

Anytime you wish to add a new model, interrupt the process (using `Ctrl C`) and repeat the above steps.