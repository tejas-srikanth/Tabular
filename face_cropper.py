import face_recognition
import cv2
import numpy
import pickle
import os
from time import sleep
import face_encoder

# TEJAS: import this file and call crop(filepath) in your frontend. It will return exception if there are the wrong number of faces, and will return True if successful. Image will be automatically created in the folder and will also update the encoding.dat file.


def crop(filepath): #takes path to file as input
    img = cv2.imread(filepath)

    face_locations = []
    face_encodings = []

    with open(os.path.join(os.path.dirname(__file__), "encoding.dat"), 'rb') as f:
        known_faces = pickle.load(f)
    

    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    found_face = False

    if len(face_encodings) == 0:
        return Exception("No faces found.")
        
    elif len(face_encodings) > 1:
        return Exception("More than one face found. Please submit an image with only one face.")
    
    for (top, right, bottom, left) in face_locations:
        
        frame = img[top:bottom, left:right]
        
    cv2.imwrite(os.path.join(os.path.dirname(__file__), "images/") + os.path.basename(filepath), frame)

    face_encoder.encode()
    return True

