import cv2
import pandas as pd
import os
from metricas import calcular_ambe, calcular_psnr, calcular_contraste, calcular_entropia

carpeta = "data"
resultados = [] #colecciones

for nombre_archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, nombre_archivo)
    
    imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    imagen_he = cv2.equalizeHist(imagen)
    
    resultados.append({
        "imagen": nombre_archivo,
        "ambe": calcular_ambe(imagen, imagen_he),
        "psnr": calcular_psnr(imagen, imagen_he),
        "contraste_original": calcular_contraste(imagen),
        "contraste_he": calcular_contraste(imagen_he),
        "entropia_original": calcular_entropia(imagen),
        "entropia_he": calcular_entropia(imagen_he)
    })

tabla = pd.DataFrame(resultados)
print(tabla)

tabla.to_csv("resultados_he.csv", index=False)
print("\n¡Listo! Resultados guardados en resultados_he.csv")