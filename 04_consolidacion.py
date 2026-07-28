import pandas as pd

# Cargar los 3 CSVs individuales
he = pd.read_csv("resultados_he.csv")
clahe = pd.read_csv("resultados_clahe.csv")
agcwd = pd.read_csv("resultados_agcwd.csv")

# Armamos una tabla "larga": una fila por combinación de imagen + técnica
filas = []

for _, fila in he.iterrows():
    filas.append({
        "imagen": fila["imagen"],
        "tecnica": "HE",
        "ambe": fila["ambe"],
        "psnr": fila["psnr"],
        "contraste": fila["contraste_he"],
        "entropia": fila["entropia_he"]
    })

for _, fila in clahe.iterrows():
    filas.append({
        "imagen": fila["imagen"],
        "tecnica": "CLAHE",
        "ambe": fila["ambe"],
        "psnr": fila["psnr"],
        "contraste": fila["contraste_clahe"],
        "entropia": fila["entropia_clahe"]
    })

for _, fila in agcwd.iterrows():
    filas.append({
        "imagen": fila["imagen"],
        "tecnica": "AGCWD",
        "ambe": fila["ambe"],
        "psnr": fila["psnr"],
        "contraste": fila["contraste_agcwd"],
        "entropia": fila["entropia_agcwd"]
    })

tabla_consolidada = pd.DataFrame(filas)
print(tabla_consolidada.head(10))

tabla_consolidada.to_csv("resultados_consolidados.csv", index=False)
print("\n¡Listo! Guardado en resultados_consolidados.csv")

# Bonus: promedio y desvío estándar por técnica, ya consolidado
print("\n=== Promedio y desvío estándar por técnica ===")
resumen = tabla_consolidada.groupby("tecnica")[["ambe", "psnr", "contraste", "entropia"]].agg(["mean", "std"])
print(resumen)
resumen.to_csv("resumen_estadistico.csv")