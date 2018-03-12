# Smart Reminder

## The Inspiration
Yesterday morning, we met two new friends, colleague, and peers. We are software people but they are hardware people, which we thought was unique and interesting and we wanted to integrate them into our team.  While we have our differences we all spend a lot of time on the computer, as I'm sure many of you do as well. 

## The Goal
We wanted to build something that would help ourselves and our user groups to minimally restrict themselves from computer use to both improve their health and maximize their productivity. We wanted to create a product which encourages people to take breaks from the computer. We generated many creative ideas but we felt this was both the most pertinent and the most important to us. 

## The Implementation
Our hardware, a raspberry pi (robot), has a camera which records images, then compresses the image (to a lower quality to support data transfer with poor connections) and sends the image with http post protocol to our server, specifically python server using flask, a micro web framework. The server then processes the image using a pre-trained deep learning AI based on the COCO dataset to determine if there is a person in the image. We also utilized bootstrap, a front-end website-building library, as well as vue js, a user-interface framework, into our ecosystem which has user-friendly buttons so that the customer can easily turn off notifications from the robot when desired, the website sends this user input to the server. The server communicates whether there is a person within view and whether notifications are enabled to the robot, and this data is used to set timers for user-interrupts to improve user-experience.
 
For our demo, we have it set to interrupt the user every three seconds of continuous work, but research suggests that in the real-world, it is best to set a timer every twenty minutes to take a fifteen second break. 
* We define 'continuous work' as the amount of time which the user spends in front of the camera. 
* Our server uses an nvidia GPU, but everything is made efficiently enough to work on any modern CPU as well.  


## The Future
* We would add more hardware, this hardware would speak to the user, it would move to bug the user to take breaks, have LEDs integrated into it, and wheels to follow users around their home/workplace.
* We would improve the software to:
  * Use eye-tracking to better determine if the user is actively working, and facial patterns to determine fatigue.
  * We would add timers to remind the user to eat, sleep, and workout throughout the day.
  * We would add a mobile app.
  * We would improve the error margins. 
  * We would add more controls to the user and more user-friendly and add authentication as well as deep learning to help learn the user's habits and patterns to optimize productivity.
* We would connect this device to the TV to be able to shut it off if children (or adults) have been watching TV for a pre-determined amount defined as too long.


## System Dependencies
You need to install python3, nodejs, and npm. *You might need to install GPU dependencies if you want to run tensorflow on your GPU*

## How to install and run?
Right now, we have a Makefile that only runs on Ubuntu. Later, we might support other platforms. If you are an ubuntu user, you can simply run the follow command to install the dependencies:
```sh
make
```

To run it, you can run the following command:
```sh
make run
```
