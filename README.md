# Comparación de Técnicas de Mejora de Contraste: HE vs. CLAHE vs. AGCWD

Proyecto para la materia de Análisis y Procesamiento de Imágenes. Se implementan y comparan tres técnicas de mejora de contraste — Ecualización de Histograma (HE), CLAHE y Adaptive Gamma Correction with Weighting Distribution (AGCWD) — evaluadas sobre 50 imágenes en escala de grises del dataset BSDS300, usando las métricas AMBE, PSNR, Contraste (desviación estándar) y Entropía.

## Requisitos

Instalar las siguientes librerías antes de correr los scripts:

```
pip install opencv-python pandas matplotlib numpy
```

## Estructura del proyecto

```
codigo_final/
├── data/                          # 50 imágenes en escala de grises (BSDS300)
├── resultados/                    # Gráficos generados (boxplots, comparaciones visuales)
│
├── metricas.py                    # Módulo: funciones de AMBE, PSNR, Contraste, Entropía
├── agcwd.py                       # Módulo: función que implementa AGCWD
├── ejecutar_todo.py                # Corre los 7 scripts en orden, uno tras otro
│
├── 01_ecualizacion_he.py          # Aplica HE a las 50 imágenes → resultados_he.csv
├── 02_clahe.py                    # Aplica CLAHE a las 50 imágenes → resultados_clahe.csv
├── 03_agcwd.py                    # Aplica AGCWD a las 50 imágenes → resultados_agcwd.csv
├── 04_consolidacion.py            # Unifica los 3 CSV + calcula promedio/desvío estándar
├── 04_promedios.py                # Muestra promedios simples de cada técnica por separado
├── 05_graficos_boxplot.py         # Genera boxplots comparativos de las 4 métricas
├── 06_identificar_casos.py        # Identifica imágenes representativas (outliers, extremos)
├── 07_comparacion_visual.py       # Genera comparación visual Original/HE/CLAHE/AGCWD
│
├── resultados_consolidados.csv    # Tabla final: 1 fila por imagen x técnica (se genera al correr 04)
└── resumen_estadistico.csv        # Promedio y desvío estándar por técnica (se genera al correr 04)
```

Todo el proyecto vive dentro de una única carpeta `codigo_final/`, autocontenida: no depende de rutas fuera de sí misma.

## Cómo correr el proyecto (en orden)

**Importante**: parate (con `cd`) dentro de la carpeta `codigo_final/` antes de correr cualquier script, ya que las rutas a `data/` y `resultados/` son relativas a esa ubicación.

**Atajo**: para correr todo el pipeline de una sola vez, en el orden correcto, usar:
```
python ejecutar_todo.py
```
Esto ejecuta los 7 scripts en secuencia y se detiene automáticamente si alguno falla.

1. **Colocar las 50 imágenes** en escala de grises dentro de la carpeta `data/` (ya incluidas en esta entrega).

2. **Aplicar cada técnica y calcular métricas:**
   ```
   python 01_ecualizacion_he.py
   python 02_clahe.py
   python 03_agcwd.py
   ```
   Cada script genera su propio CSV con los resultados por imagen (`resultados_he.csv`, `resultados_clahe.csv`, `resultados_agcwd.csv`).

3. **Consolidar resultados y obtener estadísticas:**
   ```
   python 04_consolidacion.py
   ```
   Genera `resultados_consolidados.csv` (formato largo, 1 fila por imagen x técnica) y `resumen_estadistico.csv` (promedio y desvío estándar por técnica).

   Opcionalmente, `python 04_promedios.py` muestra un resumen rápido de promedios por técnica, leyendo directamente los 3 CSV individuales.

4. **Generar gráficos:**
   ```
   python 05_graficos_boxplot.py
   python 06_identificar_casos.py
   python 07_comparacion_visual.py
   ```
   Los gráficos quedan guardados en `resultados/`. `06_identificar_casos.py` solo imprime en consola los nombres de las imágenes representativas usadas en `07_comparacion_visual.py`.

## Parámetros utilizados

- **CLAHE**: `clipLimit=2.0`, `tileGridSize=(8, 8)`
- **AGCWD**: `alpha=0.75` (valor estándar propuesto en Huang et al., 2013)

## Dataset

Berkeley Segmentation Dataset (BSDS300), 50 imágenes en escala de grises seleccionadas de los subconjuntos de test (imágenes 1-25 y 26-50).
Fuente: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/

## Métricas implementadas (`metricas.py`)

| Función | Métrica | Qué mide |
|---|---|---|
| `calcular_ambe` | AMBE | Cambio de brillo promedio respecto al original |
| `calcular_psnr` | PSNR | Distorsión introducida respecto al original |
| `calcular_contraste` | Contraste (σ) | Dispersión de los niveles de intensidad |
| `calcular_entropia` | Entropía | Información/detalle contenido en la imagen |

## Autor

Betania Notario — "Procesamiento Digital de Imágenes" - Maestría en Inteligencia Artificial y Análisis de Datos, [Facultad Politécnica - Universidad Nacional de Asunción]
