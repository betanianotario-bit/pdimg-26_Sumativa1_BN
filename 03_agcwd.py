import cv2
import pandas as pd
import os
from agcwd import aplicar_agcwd
from metricas import calcular_ambe, calcular_psnr, calcular_contraste, calcular_entropia

carpeta = "data"
resultados = []

for nombre_archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, nombre_archivo)
    
    imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    imagen_agcwd = aplicar_agcwd(imagen, alpha=0.75)
    
    resultados.append({
        "imagen": nombre_archivo,
        "ambe": calcular_ambe(imagen, imagen_agcwd),
        "psnr": calcular_psnr(imagen, imagen_agcwd),
        "contraste_original": calcular_contraste(imagen),
        "contraste_agcwd": calcular_contraste(imagen_agcwd),
        "entropia_original": calcular_entropia(imagen),
        "entropia_agcwd": calcular_entropia(imagen_agcwd)
    })

tabla = pd.DataFrame(resultados)
print(tabla)

tabla.to_csv("resultados_agcwd.csv", index=False)
print("\n¡Listo! Resultados guardados en resultados_agcwd.csv")