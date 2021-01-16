import face_recognition
import pickle
import os

rohan_image = face_recognition.load_image_file(os.path.join(os.path.dirname(__file__), "images/rohan.png"))
rohan_face_encoding = face_recognition.face_encodings(rohan_image)[0]


known_faces = [
    rohan_face_encoding,
]

with open(os.path.join(os.path.dirname(__file__), "encoding.dat"), 'wb') as f:
    pickle.dump(known_faces, f)