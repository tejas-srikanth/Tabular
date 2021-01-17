# Tabular
Tabular is a wireless person detection system that executes keyboard macros automatically.

## Features
Tabular has a wireless camera built on Raspberry Pi Zero W that sends frames to a computer for processing. The computer performs face detection on the frames and will execute keyboard macros if found. Tabular also includes a customization app that allows the user to choose a specific face to recognize and change the executed keystrokes.

## Video Demonstration
https://www.youtube.com/watch?v=kuES65eorVw

## Background
Tabular was created and submitted to Hack the North 2020++.

## Usage

### Computer
Install dependencies.

    pip install opencv-python
    pip install face-recognition
    pip install numpy
    pip install imutils
    pip install imagezmq
    pip install pynput

Depending on your Python configuration, you may need additional dependencies. Install those as well.

Start the application.

    python face-detection.py

If there is no output, it is working correctly.

### Raspberry Pi
Install OpenCV. Then, install the remaining dependencies.

    pip install numpy
    pip install imutils
    pip install imagezmq

As Raspberry Pi is not as full-featured, be careful for additional requirements.

Start the client

    python client.py --server-ip <your server ip>

## Contributors
Matthews Ma

Rohan Shetty

Tejas Srikanth

Kenny Lee