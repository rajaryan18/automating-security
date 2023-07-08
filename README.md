# All in One Security
<p>
Trackers, Detectors and other Deep Learning Tools are great for automating many tasks specially security. It is fast, reliable and very convenient to use. <br />
But we often require multiple models running simultaneously which can be rather cumbersome to maintain and synchronize requiring multiple devices or packages. <br />
This project aims at providing a solution for the above problem. <br />
</p>

<p>
<b>Note</b>: You will need Docker installed to run the project
</p>

<h3>To clone the Project</h3>
<p>
In the terminal, run the following the commands<br />
```
git clone https://github.com/rajaryan18/automating-security.git
```
<br />
```
git branch -M main
```
</p>

<p>
The project consists of 2 main parts. The <b>models</b> section where one can store all the Deep Learning models and the <b>backend</b> section that connects to all these models and provides APIs for the same. It also regularly uploads information on Blockchain so that it cannot be tampered with.
</p>

<h3>The Backend Section</h3>
<p>
Run the following command in the terminal,
```
cd backend
```
<br />
```
docker run
```
<br />
An admin page will open at ```http://localhost:5500``` You will be prompted for your data and then the admin page will open with more options. <br />
Here you can add devices, check device log etc.<br />
The blockchain is handled by the application.
</p>

<h3>The Model Section</h3>
<p>
Add your model that contains a ```run()``` function responsible for running the model. It can have getter function that returns the current state of detection/tracking. <br />
In ```app.py``` import the model and create it's object in the ```main()``` function. <br />
In the terminal, run the following commands. <br />
```
cd models
```
<br />
```
docker run
```
<br /><br />

Anytime you wish to add a new model, interrupt the process (using `Ctrl C`) and repeat the above steps.
</p>