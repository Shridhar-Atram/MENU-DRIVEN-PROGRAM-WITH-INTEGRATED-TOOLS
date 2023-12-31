from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
import os

def mesh():
    os.system("espeak-ng 'Hold on. Opening camera...'")
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector(maxFaces=2)
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if faces:
            print(faces[0])
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == 13 :
            break
    cap.release()
    cv2.destroyAllWindows()
