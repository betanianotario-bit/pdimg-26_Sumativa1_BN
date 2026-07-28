import os
os.makedirs("resultados", exist_ok=True)

import pandas as pd
import matplotlib.pyplot as plt

# Cargar la tabla consolidada (formato largo, ya lista para graficar por grupo)
tabla = pd.read_csv("resultados_consolidados.csv")

metricas = ["ambe", "psnr", "contraste", "entropia"]
titulos = ["AMBE", "PSNR (dB)", "Contraste (σ)", "Entropía (bits)"]

fig, ejes = plt.subplots(2, 2, figsize=(12, 10))
ejes = ejes.flatten()  # para poder recorrerlos con un for simple

for i, metrica in enumerate(metricas):
    datos_por_tecnica = [
        tabla[tabla["tecnica"] == "HE"][metrica],
        tabla[tabla["tecnica"] == "CLAHE"][metrica],
        tabla[tabla["tecnica"] == "AGCWD"][metrica]
    ]
    
    ejes[i].boxplot(datos_por_tecnica, tick_labels=["HE", "CLAHE", "AGCWD"])
    ejes[i].set_title(titulos[i])
    ejes[i].set_ylabel(titulos[i])
    ejes[i].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("resultados/boxplots_comparacion.png", dpi=150)
plt.show()

print("¡Listo! Gráfico guardado en resultados/boxplots_comparacion.png")