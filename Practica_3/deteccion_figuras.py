import cv2
import numpy as np


def fig_color(figura_hsv):
    yellow_bajo = np.array([15, 100, 20], np.uint8)
    yellow_alto = np.array([35, 255, 255], np.uint8)

    green_bajo = np.array([36, 100, 20], np.uint8)
    green_alto = np.array([90, 255, 255], np.uint8)

    blue_bajo = np.array([91, 100, 20], np.uint8)
    blue_alto = np.array([130, 255, 255], np.uint8)

    red_bajo1 = np.array([0, 100, 20], np.uint8)
    red_alto1 = np.array([10, 255, 255], np.uint8)

    red_bajo2 = np.array([175, 100, 20], np.uint8)
    red_alto2 = np.array([180, 255, 255], np.uint8)

    mask_green = cv2.inRange(figura_hsv, green_bajo, green_alto)
    mask_yellow = cv2.inRange(figura_hsv, yellow_bajo, yellow_alto)
    mask_blue = cv2.inRange(figura_hsv, blue_bajo, blue_alto)

    mask_red1 = cv2.inRange(figura_hsv, red_bajo1, red_alto1)
    mask_red2 = cv2.inRange(figura_hsv, red_bajo2, red_alto2)
    mask_red = cv2.add(mask_red1, mask_red2)

    cntr_yellow, _ = cv2.findContours(
        mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntr_green, _ = cv2.findContours(
        mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntr_blue, _ = cv2.findContours(
        mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntr_red, _ = cv2.findContours(
        mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    color = 'x'

    if len(cntr_red) > 0:
        color = 'rojo'
    elif len(cntr_green) > 0:
        color = 'verde'
    elif len(cntr_blue) > 0:
        color = 'azul'
    elif len(cntr_yellow) > 0:
        color = 'amarilla'

    return color


def figura(contorno, width, heigth):
    nombre_figura = 'x'
    epsilon = 0.01 * cv2.arcLength(contorno, True)
    aprox = cv2.approxPolyDP(contorno, epsilon, True)

    if len(aprox) == 3:
        nombre_figura = 'Triangulo'
    elif len(aprox) == 4:
        res = float(width/heigth)
        print(width, res)
        if res < 1.2:
            nombre_figura = 'Cuadrado'
        else:
            nombre_figura = 'Rectangulo'
    elif len(aprox) == 5:
        nombre_figura = 'Pentagono'
    elif len(aprox) == 6:
        nombre_figura = 'Hexagono'
    elif len(aprox) > 10:
        nombre_figura = 'Circulo'

    return nombre_figura


img = cv2.imread('Practica_3/figuras_rgb.png')

gris = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
canny = cv2.Canny(gris, 10, 150)
kernel = np.ones((3, 3), np.uint8)
canny = cv2.dilate(canny, kernel, iterations=1)

contornos, _ = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

for c in contornos:
    x, y, w, h = cv2.boundingRect(c)
    img_aux = np.zeros(img.shape[:2], dtype='uint8')
    img_aux = cv2.drawContours(img_aux, [c], -1, 255, -1)
    mask_hsv = cv2.bitwise_and(img_hsv, img_hsv, mask=img_aux)
    fill_all = figura(c, w, h) + ' ' + fig_color(mask_hsv)
    cv2.putText(img, fill_all, (x, y + 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

cv2.imshow('imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
