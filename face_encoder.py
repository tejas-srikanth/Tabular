import face_recognition
import pickle
import os

encodings = []

for filename in os.listdir(os.path.join(os.path.dirname(__file__), "images/")):
    img = face_recognition.load_image_file(os.path.join(os.path.dirname(__file__), "images/" + filename)) #will encode all images in this folder
    encodings.append(face_recognition.face_encodings(img)[0])

with open(os.path.join(os.path.dirname(__file__), "encoding.dat"), 'wb') as f:
    pickle.dump(encodings, f)