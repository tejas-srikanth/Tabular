import face_recognition
import cv2
import sys
import pickle
from time import sleep
import os
import imagezmq
from infi.systray import SysTrayIcon
import interface1
from pynput.keyboard import Controller, Key

keyboard = Controller()
found_face = False
previous_frames = [False, False]

def on_quit_callback(systray):
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

def open_settings(systray):
    interface1.main()

menu_options = (("Settings", None, open_settings),)
systray = SysTrayIcon(os.path.join(os.path.dirname(__file__), "sketch.ico"), "Tabular", menu_options, on_quit=on_quit_callback)
systray.start()

image_hub = imagezmq.ImageHub()

source = 0
if len(sys.argv) > 1:
    source = sys.argv[1]

# Initialize some variables
face_locations = []
face_encodings = []
frame_number = 0

with open(os.path.join(os.path.dirname(__file__), "encoding.dat"), 'rb') as f:
    known_faces = pickle.load(f)

while True:
    pi_name, rgb_frame = image_hub.recv_image() # currently bricks the thread, do not run
    image_hub.send_reply(b'OK')   

    #Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    previous_frames[-2], previous_frames[-1] = previous_frames[-1], found_face
    found_face = False

    for face_encoding in face_encodings:
        # See if the face is a match
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        if any(match):
            found_face = True

            # call trigger here
            if (previous_frames[-1] == False and previous_frames[-2] == False):

                print("Face detected!")

                for key in interface1.recorded:
                    print(interface1.recorded)
                    keyboard.press(key)
                for key in interface1.recorded:
                    keyboard.release(key)

    cv2.imshow(pi_name, rgb_frame)
    cv2.waitKey(1)