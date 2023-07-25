import cv2
import math
import os

def dist():
    os.system("espeak-ng 'Hold on. Opening Camera...'")
    face_cascade = cv2.CascadeClassifier('myhaarcascade_frontalface_default.xml')
    focal_length = 600
    def calculate_distance(face_width, focal_length, pixel_width):
        return (face_width * focal_length) / pixel_width
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            distance = calculate_distance(16, focal_length, w)
            cv2.putText(frame, f"Distance: {distance:.2f} cm", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
