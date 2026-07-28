import pandas as pd

# Cargar los 3 CSVs
he = pd.read_csv("resultados_he.csv")
clahe = pd.read_csv("resultados_clahe.csv")
agcwd = pd.read_csv("resultados_agcwd.csv")

print("=== PROMEDIOS - HE ===")
print(he[["ambe", "psnr", "contraste_he", "entropia_he"]].mean())

print("\n=== PROMEDIOS - CLAHE ===")
print(clahe[["ambe", "psnr", "contraste_clahe", "entropia_clahe"]].mean())

print("\n=== PROMEDIOS - AGCWD ===")
print(agcwd[["ambe", "psnr", "contraste_agcwd", "entropia_agcwd"]].mean())