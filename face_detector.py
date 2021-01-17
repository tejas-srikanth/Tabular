import face_recognition
import cv2
import sys
import pickle
from time import sleep
import os
import imagezmq
from infi.systray import SysTrayIcon
import interface1
import keyboard

def on_quit_callback(systray):
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

def open_settings(systray):
    interface1.main()

menu_options = (("Settings", None, open_settings),)
systray = SysTrayIcon(os.path.join(os.path.dirname(__file__), "sketch.ico"), "Facial Recognition", menu_options, on_quit=on_quit_callback)
systray.start()


# # Open the input movie file
# input_video = cv2.VideoCapture("input.mp4")
# length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))

image_hub = imagezmq.ImageHub()

source = 0
if len(sys.argv) > 1:
    source = sys.argv[1]

# cap = cv2.VideoCapture(source)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 375)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 250)
# hasFrame, frame2 = cap.read()
# frame = cv2.flip( frame2, 0 )
# frame_count = 0

# Initialize some variables
face_locations = []
face_encodings = []
frame_number = 0

with open(os.path.join(os.path.dirname(__file__), "encoding.dat"), 'rb') as f:
    known_faces = pickle.load(f)

while True:
    pi_name, rgb_frame = image_hub.recv_image() # currently bricks the thread, do not run
    image_hub.send_reply(b'OK')

    #THE FOLLOWING COULD BE DONE ON THE PI
    # hasFrame, frame2 = cap.read()
    # frame = cv2.flip( frame2, 1 )

    # frame_count += 1

    # # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    # rgb_frame = frame[:, :, ::-1]
    

    #Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    found_face = False

    # if len(face_encodings) > 0:
    #     print("i c face")

    for face_encoding in face_encodings:
        # See if the face is a match
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        if any(match):
            found_face = True
            # call trigger here
            keyboard.press_and_release('alt+tab')

    # Label the results
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     if not name:
    #         continue
    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    #     # Draw a label with a name below the face
    #     cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
    #     font = cv2.FONT_HERSHEY_DUPLEX
    #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow(pi_name, rgb_frame)
    cv2.waitKey(1)