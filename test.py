
import cv2

img = cv2.imread('C:/Users/Alfred/Pictures/EDD_prototipos/img/equipo.PNG')
cv2.imshow('Imagen', img)
cv2.waitKey(0)

#Modelos de color
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagen en gris', gris)
cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Imagen en hsv', hsv)
cv2.waitKey(0)

yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow('Imagen en yuv', yuv)
cv2.waitKey(0)

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('Imagen en ycrcb', ycrcb)
cv2.waitKey(0)

#Dividir la imagen en canales de color(RGB)
b, g, r = cv2.split(img)
cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)
cv2.waitKey(0)

src = cv2.merge([r, g, b])
cv2.imshow('Imagen en RGB', src)
cv2.waitKey(0)

src2 = cv2.merge([b, g, r])
cv2.imshow('Imagen en BGR', src2)
cv2.waitKey(0)

cv2.destroyAllWindows()

