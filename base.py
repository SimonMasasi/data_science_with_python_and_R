import cv2
import numpy as np

cap = cv2.VideoCapture("rtsp://admin:eg@s2022@172.17.17.64:554/cam/realmonitor?channel=1&subtype=0")

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()