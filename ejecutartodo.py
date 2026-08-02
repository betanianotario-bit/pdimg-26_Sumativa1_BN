#Arreglé la extensión "_py" a ".py"
import subprocess
import sys

scripts = [
    "01_ecualizacion_he.py",
    "02_clahe.py",
    "03_agcwd.py",
    "04_consolidacion.py",
    "05_graficos_boxplot.py",
    "06_identificar_casos.py",
    "07_comparacion_visual.py"
]

for script in scripts:
    print(f"\n{'='*50}")
    print(f"Ejecutando: {script}")
    print('='*50)
    
    resultado = subprocess.run([sys.executable, script])
    
    if resultado.returncode != 0:
        print(f"\n⚠️  Error al ejecutar {script}. Deteniendo ejecución.")
        break
else:
    print("\n✅ ¡Todos los scripts se ejecutaron correctamente!")