import cv2
import numpy as np

image = cv2.imread('Practica_4/images.jpg')

if image is None:
    print("Nose pudo cargar la imagen")
else:
    # filtro de suavizado
    blur_image = cv2.blur(image, (5, 5))
    cv2.imshow('Imagen Original', image)
    cv2.imshow('Imagen Blur', blur_image)

    # fitro negativo
    row, col, _ = image.shape
    negativo = np.zeros((row, col, 3), dtype=np.uint8)
    for a in range(0, row):
        for b in range(0, col):
            negativo[a, b, :] = 255 - image[a, b, :]
    cv2.imshow('Imagen Negative', negativo)

    # filtro pencilSketch
    gris, color = cv2.pencilSketch(
        image, sigma_s=60, sigma_r=0.7, shade_factor=0.05)
    cv2.imshow('Imagen Gris', gris)
    cv2.imshow('Imagen Color', color)

    # filtro septia
    # copia = image.copy()
    # copia = cv2.transform(copia, np.matrix([0.272, 0.534, 0.131],
    #                                        [0.249, 0.286, 0.168],
    #                                         [0.393, 0.769, 0.189]))
    # copia[np.where(copia > 255)] = 255
    # copia = np.array(copia, dtype=cv2.uint8)
    # cv2.imshow('Imagen Sepia', copia)

    sepia_matrix = np.array([
        [0.272, 0.534, 0.131],
        [0.249, 0.286, 0.168],
        [0.393, 0.769, 0.189]
    ], dtype=np.float32)

    # Apply the sepia transformation
    copia = image.copy()
    copia = cv2.transform(copia, sepia_matrix)
    copia[np.where(copia > 255)] = 255
    copia = np.array(copia, dtype=np.uint8)
    # copia = np.clip(copia, 0, 255)
    # Convert the result to uint8
    # copia = np.uint8(copia)
    cv2.imshow('Imagen Sepia', copia)

    # filtro catoon
    borde = cv2.bitwise_not(cv2.Canny(image, 100, 200))
    grisB = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grisB = cv2.medianBlur(grisB, 5)
    borde2 = cv2.adaptiveThreshold(
        grisB, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
    dst = cv2.edgePreservingFilter(image, flags=2, sigma_s=64, sigma_r=0.25)

    cartoon1 = cv2.bitwise_and(dst, dst, mask=borde)
    cartoon2 = cv2.bitwise_and(dst, dst, mask=borde2)
    cv2.imshow('Imagen Cartoon1', cartoon1)
    cv2.imshow('Imagen Cartoon2', cartoon2)

    # mascara border sobel
    grad_x = cv2.Sobel(grisB, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(grisB, cv2.CV_64F, 0, 1, ksize=3)
    gradiant_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    cv2.imshow('Imagen Sobel', gradiant_magnitude)

    key = cv2.waitKey()
    if key == ord('q'):
        cv2.destroyAllWindows()
7
