import cv2
import numpy as np

url = "http://192.168.21.112:8080/video"
video = cv2.VideoCapture(url)

cv2.namedWindow('red1', cv2.WINDOW_NORMAL)
cv2.namedWindow('red1Bis', cv2.WINDOW_NORMAL)

cv2.namedWindow('red2', cv2.WINDOW_NORMAL)
cv2.namedWindow('red2Bis', cv2.WINDOW_NORMAL)

cv2.namedWindow('yellow', cv2.WINDOW_NORMAL)
cv2.namedWindow('yellowBis', cv2.WINDOW_NORMAL)

cv2.namedWindow('blue', cv2.WINDOW_NORMAL)
cv2.namedWindow('blueBis', cv2.WINDOW_NORMAL)

cv2.namedWindow('yellow', cv2.WINDOW_NORMAL)
cv2.namedWindow('yellowBis', cv2.WINDOW_NORMAL)
cv2.namedWindow('original', cv2.WINDOW_NORMAL)

yellow_bajo = np.array([15, 100, 20], np.uint8)
yellow_alto = np.array([55, 255, 255], np.uint8)

green_bajo = np.array([46, 100, 20], np.uint8)
green_alto = np.array([90, 255, 255], np.uint8)

blue_bajo = np.array([91, 100, 20], np.uint8)
blue_alto = np.array([130, 255, 255], np.uint8)

red_bajo1 = np.array([0, 100, 20], np.uint8)
red_alto1 = np.array([10, 255, 255], np.uint8)

red_bajo2 = np.array([175, 100, 20], np.uint8)
red_alto2 = np.array([180, 255, 255], np.uint8)

while (True):
    ref, frame = video.read()

    if ref == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Deteccion de color verde
        mask_green = cv2.inRange(hsv, green_bajo, green_alto)
        mask_greenbis = cv2.bitwise_and(frame, frame, mask=mask_green)

        cv2.imshow('green', mask_green)
        cv2.imshow('greenBis', mask_greenbis)

        # Deteccion de color amarillo
        mask_yellow = cv2.inRange(hsv, yellow_bajo, yellow_alto)
        mask_yellowbis = cv2.bitwise_and(frame, frame, mask=mask_yellow)

        cv2.imshow('yellow', mask_yellow)
        cv2.imshow('yellowBis', mask_yellowbis)

        # Deteccion de color azul
        mask_blue = cv2.inRange(hsv, blue_bajo, blue_alto)
        mask_bluebis = cv2.bitwise_and(frame, frame, mask=mask_blue)

        cv2.imshow('blue', mask_blue)
        cv2.imshow('blueBis', mask_bluebis)

        # Deteccion de color rojo1
        mask_red1 = cv2.inRange(hsv, red_bajo1, red_alto1)
        mask_red1bis = cv2.bitwise_and(frame, frame, mask=mask_red1)

        cv2.imshow('red1', mask_red1)
        cv2.imshow('red1Bis', mask_red1bis)

        # Deteccion de color rojo1
        mask_red2 = cv2.inRange(hsv, red_bajo2, red_alto2)
        mask_red2bis = cv2.bitwise_and(frame, frame, mask=mask_red2)

        cv2.imshow('red2', mask_red2)
        cv2.imshow('red2Bis', mask_red2bis)

        # Video original
        cv2.imshow('original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
