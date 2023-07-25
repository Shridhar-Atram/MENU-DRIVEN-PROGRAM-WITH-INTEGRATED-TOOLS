from cvzone.PoseModule import PoseDetector
import cv2
import os

def detect():
    os.system("Hold on. Opening Camera...")
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
        if bboxInfo:
            center = bboxInfo["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        cv2.imshow("Image", img)
        if cv2.waitKey(50)== 13:
            break
    cap.release()
    cv2.destroyAllWindows()
