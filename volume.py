import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import os

def volu():
    os.system("espeak-ng 'Hold on. Opening Camera...'")
    detector = HandDetector(detectionCon=0.8)
    min_volume = 0
    max_volume = 100
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.flip(frame, 1)
        hands, frame = detector.findHands(frame)
        if hands:
            for hand in hands:
                landmarks = hand["lmList"]
                bbox = hand["bbox"]
                thumb_tip = landmarks[4]
                index_tip = landmarks[8]
                thumb_index_distance = np.linalg.norm(np.subtract(thumb_tip, index_tip))
                volume = np.interp(thumb_index_distance, [20, 200], [min_volume, max_volume])
                volume = int(max(min(volume, max_volume), min_volume))
                pyautogui.press('volumedown') if volume < 50 else pyautogui.press('volumeup')
                cv2.putText(frame, f"Volume: {volume}%", (bbox[0], bbox[1] - 20),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        cv2.imshow("Volume Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
