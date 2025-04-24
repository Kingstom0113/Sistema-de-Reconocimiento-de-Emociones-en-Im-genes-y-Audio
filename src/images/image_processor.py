import numpy as np

def preprocess_image(image):
    import cv2
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    image = cv2.resize(image, (48, 48))  # Resize to 48x48 for emotion detection
    return image / 255.0  # Normalize the image

def detect_faces(image):
    import cv2
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
    return faces

def crop_faces(image, faces):
    # Crop detected faces from the image
    cropped_faces = [image[y:y+h, x:x+w] for (x, y, w, h) in faces]
    return cropped_faces