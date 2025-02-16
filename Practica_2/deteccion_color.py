import cv2
import numpy as np

url = "http://192.168.21.112:8080/video"
video = cv2.VideoCapture(url)

yellow_bajo = np.array([15, 100, 20], np.uint8)
yellow_alto = np.array([55, 255, 255], np.uint8)

while (True):
    ref, frame = video.read()
    if ref == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_yellow = cv2.inRange(hsv, yellow_bajo, yellow_alto)
        mask_yellowbis = cv2.bitwise_and(frame, frame, mask=mask_yellow)

        cv2.imshow('yellow', mask_yellow)
        cv2.imshow('yellowBis', mask_yellowbis)
        cv2.imshow('original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


video.release()
cv2.destroyAllWindows()
