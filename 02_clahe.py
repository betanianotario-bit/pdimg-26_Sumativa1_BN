import cv2
import pandas as pd
import os
from metricas import calcular_ambe, calcular_psnr, calcular_contraste, calcular_entropia

carpeta = "data"
resultados = []

# Creamos el objeto CLAHE una sola vez, fuera del loop
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) #explicar estos valores 

for nombre_archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, nombre_archivo)
    
    imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    imagen_clahe = clahe.apply(imagen)
    
    resultados.append({
        "imagen": nombre_archivo,
        "ambe": calcular_ambe(imagen, imagen_clahe),
        "psnr": calcular_psnr(imagen, imagen_clahe),
        "contraste_original": calcular_contraste(imagen),
        "contraste_clahe": calcular_contraste(imagen_clahe),
        "entropia_original": calcular_entropia(imagen),
        "entropia_clahe": calcular_entropia(imagen_clahe)
    })

tabla = pd.DataFrame(resultados)
print(tabla)

tabla.to_csv("resultados_clahe.csv", index=False)
print("\n¡Listo! Resultados guardados en resultados_clahe.csv")