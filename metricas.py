import cv2
import numpy as np


def calcular_ambe(imagen_original, imagen_procesada):
    """
    Calcula el Absolute Mean Brightness Error (AMBE) entre dos imágenes.
    Mide cuánto cambió el brillo promedio tras aplicar una técnica.
    """
    media_original = np.mean(imagen_original)
    media_procesada = np.mean(imagen_procesada)
    return abs(media_original - media_procesada)


def calcular_psnr(imagen_original, imagen_procesada):
    """
    Calcula el Peak Signal-to-Noise Ratio (PSNR) entre dos imágenes.
    Mide cuánta distorsión se introdujo respecto a la imagen original.
    """
    original = imagen_original.astype(np.float64)
    procesada = imagen_procesada.astype(np.float64)

    mse = np.mean((original - procesada) ** 2)

    if mse == 0:
        return float('inf')  # Imágenes idénticas, no hay distorsión

    return 10 * np.log10((255 ** 2) / mse)


def calcular_contraste(imagen):
    """
    Calcula el contraste de una imagen como la desviación estándar
    de sus niveles de intensidad.
    """
    return np.std(imagen)


def calcular_entropia(imagen):
    """
    Calcula la entropía de Shannon de una imagen, midiendo la
    cantidad de información/detalle presente en su distribución de grises.
    """
    histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256])
    histograma_normalizado = histograma / histograma.sum()

    probabilidades = histograma_normalizado[histograma_normalizado > 0]

    return -np.sum(probabilidades * np.log2(probabilidades))