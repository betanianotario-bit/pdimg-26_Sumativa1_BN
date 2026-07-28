import cv2
import matplotlib.pyplot as plt
from agcwd import aplicar_agcwd

imagenes_interes = ["45096.jpg", "296007.jpg", "167062.jpg"]
etiquetas_casos = ["Outlier AMBE (HE)", "Menor contraste original", "Mayor contraste original"]

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

fig, ejes = plt.subplots(len(imagenes_interes), 4, figsize=(16, 4 * len(imagenes_interes)))

for fila, (nombre_img, etiqueta) in enumerate(zip(imagenes_interes, etiquetas_casos)):
    imagen = cv2.imread(f"data/{nombre_img}", cv2.IMREAD_GRAYSCALE)
    imagen_he = cv2.equalizeHist(imagen)
    imagen_clahe = clahe.apply(imagen)
    imagen_agcwd = aplicar_agcwd(imagen, alpha=0.75)

    versiones = [imagen, imagen_he, imagen_clahe, imagen_agcwd]
    titulos = ["Original", "HE", "CLAHE", "AGCWD"]

    for col in range(4):
        ejes[fila, col].imshow(versiones[col], cmap="gray")
        ejes[fila, col].set_title(f"{titulos[col]}" if fila == 0 else "")
        ejes[fila, col].axis("off")

    # Etiqueta del caso a la izquierda de la fila
    ejes[fila, 0].set_ylabel(etiqueta, fontsize=9)

plt.tight_layout()
plt.savefig("resultados/comparacion_visual_casos.png", dpi=150)
plt.show()

print("¡Listo! Guardado en resultados/comparacion_visual_casos.png")