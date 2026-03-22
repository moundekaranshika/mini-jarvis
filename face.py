import face_recognition
import cv2

def recognize_user():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # (simple version: just detect face)
    face_locations = face_recognition.face_locations(frame)

    cap.release()

    if face_locations:
        return True
    return False
