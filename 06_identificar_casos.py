import pandas as pd

tabla = pd.read_csv("resultados_consolidados.csv")

# Buscar la imagen con el AMBE más alto en HE (el outlier que vimos en el boxplot)
he = tabla[tabla["tecnica"] == "HE"]
outlier_he = he.loc[he["ambe"].idxmax()]
print("Outlier de AMBE en HE:")
print(outlier_he)

# Buscar la imagen más oscura y más clara del dataset (usando contraste_original como referencia)
he_original = pd.read_csv("resultados_he.csv")
print("\nImagen con menor contraste original (más 'plana'):")
print(he_original.loc[he_original["contraste_original"].idxmin(), ["imagen", "contraste_original"]])

print("\nImagen con mayor contraste original (ya bien contrastada):")
print(he_original.loc[he_original["contraste_original"].idxmax(), ["imagen", "contraste_original"]])