import cv2
import numpy as np


def aplicar_agcwd(imagen, alpha=0.75):
    """
    Aplica Adaptive Gamma Correction with Weighting Distribution (AGCWD).
    """
    # Paso 1: histograma y probabilidad p(x)
    histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256]).flatten()
    p = histograma / histograma.sum()

    # Paso 2: probabilidad ponderada p_w(x)
    p_max = p.max()
    p_min = p.min()
    p_w = p_max * ((p - p_min) / (p_max - p_min)) ** alpha

    # Paso 3: CDF ponderada c_w(x)
    c_w = np.cumsum(p_w) / np.sum(p_w)

    # Paso 4: gamma por nivel de intensidad
    gamma = 1 - c_w

    # Paso 5: armar la tabla (LUT) de 256 valores y aplicarla
    niveles = np.arange(256)
    tabla = 255 * (niveles / 255) ** gamma
    tabla = tabla.astype(np.uint8)

    imagen_agcwd = cv2.LUT(imagen, tabla)
    return imagen_agcwd