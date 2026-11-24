# sylfish-dl

Clasificación y segmentación de peces con deep learning, sobre la base de datos SylFishBD. Es el proyecto final de Inteligencia Artificial (Universidad del Magdalena, 2026-2). Entrega: sábado 21 de noviembre de 2026.

El sistema recibe la fotografía de un pez y responde dos cosas: de qué especie es, con qué confianza, y dónde está. La demo es una interfaz Gradio ejecutada en Colab (`share=True`, enlace público temporal): se sube una imagen y se obtiene la imagen con el contorno del pez y una leyenda con la especie y el porcentaje de confianza, más un resumen con el área del pez.

## Cómo funciona

```
              ┌─► CNN (EfficientNetB0)  ─► especie + confianza ─┐
foto del pez ─┤                                                  ├─► imagen con contorno y leyenda
              └─► U-Net v2 (binaria)    ─► máscara pez/fondo  ───┘
```

Son dos modelos independientes que solo se unen en la demo. Se entrenan, validan y guardan por separado, de modo que el fallo de uno no contamina al otro y cada uno tiene sus propias métricas.

## Datos

SylFishBD tiene 9075 fotografías JPG a color de 500×500 píxeles. La única anotación es la clase, dada por la carpeta; no hay máscaras de segmentación. Las clases siguen este orden:

| boal | ilish | kalibaush | katla | koi | mrigel | pabda | rui | telapia | Total |
|---|---|---|---|---|---|---|---|---|---|
| 885 | 789 | 525 | 1133 | 592 | 1293 | 862 | 1670 | 1326 | 9075 |

La razón entre la clase mayor y la menor es $1670/525\approx3.18$. Hay copias exactas y casi duplicadas, así que la partición se hace **por grupos de duplicados** (MD5 y dHash con distancia de Hamming $\le 5$), 70/15/15 y con semilla 42: una foto y sus copias nunca quedan en conjuntos distintos. Quedan 8975 imágenes (train 6246, val 1359, test 1370); 100 se excluyeron por ruido de etiqueta. Las imágenes, las máscaras, los `.npz` y los modelos no están en este repositorio: viven en Drive ([enlace a la carpeta de Drive]). Referencia del dataset: [completar referencia del dataset].

## Segmentación: máscaras con SAM 2 y U-Net v2 (módulo 05)

**Problema.** Como el dataset no trae máscaras, la primera versión de la U-Net (`unet_v1`) se entrenó con pseudo-máscaras de GrabCut (OpenCV). GrabCut dejó 640 máscaras vacías y su control de calidad descartó 1857 de 8975 (20.7 %), sobre todo escenas con plato, balde o mesa; solo 7118 máscaras quedaron aptas.

**Idea.** Usar **SAM 2** (Segment Anything Model 2, de Meta) como herramienta de **etiquetado offline**: genera máscaras nuevas una sola vez y no forma parte del sistema entregado. La U-Net se reentrena desde cero con esas máscaras.

**Pipeline** (cuadernos `05_preparacion_mascaras_sam2_{A_prompts,B_sam2,C_unet_v2}`):

1. **A (TensorFlow).** La `unet_v1` predice una caja y un centroide por imagen; esos son los prompts de SAM 2. Se sortea una muestra de 30 imágenes de val para revisar a ojo.
2. **B (PyTorch).** Piloto visual con dos prompts (P1: caja fija; P3: caja de la v1 ampliada 5 % más un punto positivo en el centroide). P3 acertó en 27 de 30 imágenes (a ojo) y se aplicó al lote completo de 8975 imágenes (34 min en una T4). Posproceso con OpenCV (componente conexa mayor y relleno de huecos) y control de calidad recalibrado solo con val: $0.02 \le$ área $\le 0.35$ y banda de borde $\le 0.08$.
3. **C (TensorFlow).** Se entrena la **U-Net v2**, con arquitectura, hiperparámetros y semilla idénticos a la v1 (1,946,993 parámetros, BCE + Dice, Adam $10^{-3}$, lote 16, semilla 42); solo cambian las etiquetas. Se elige $\tau$ en val y el test se evalúa una sola vez.

**Resultado del control de calidad.** La retención sube de 7118 a 8702 de 8975 imágenes (79.3 % a 97.0 %). Por clase, `boal` pasa de 63.3 % a 94.3 % e `ilish` de 62.6 % a 93.9 %.

**Modelo final.** Tras evaluar la opción SAM 2, el modelo de segmentación seleccionado es **`unet_v2`** (`models/unet_v2.keras`, `models/unet_v2_umbral.json`, $\tau = 0.6$). Se eligió por juicio visual directo: la v2 acertó en 27 de 30 imágenes de val (a ojo) y SAM 2 resultó mejor que GrabCut en las 30 comparadas; la v1 no se calificó y la regla de ventaja fijada de antemano no se evaluó. `unet_v1` queda como respaldo.

| Modelo | Etiquetas de referencia | mIoU por imagen (val) | mIoU por imagen (test) | Imágenes evaluadas (test) |
|---|---|---|---|---|
| `unet_v1` | GrabCut | 0.8334 | 0.8344 | 1119 |
| **`unet_v2`** (final) | SAM 2 | 0.8962 | 0.8944 | 1335 |

**Esas dos filas no son comparables:** cada mIoU se mide contra las máscaras con que se entrenó el modelo (GrabCut o SAM 2) y sobre un conjunto distinto de imágenes (`qc_ok` 7118 contra `sam2_qc_ok` 8702). La evidencia de que la v2 es mejor es visual y de una sola persona, no una cifra.

## Evaluación

Todas las decisiones (arquitectura, umbral $\tau$, prompt, umbrales del control de calidad, selección de modelo) se toman en validación. El test se evalúa una sola vez, con el modelo congelado. El test ya se había evaluado con la `unet_v1` antes de entrenar la v2, y eso se declara. La U-Net se evalúa con IoU por imagen (media y mediana) y, para la v1, también con Dice global y matriz de confusión de píxeles.

## Limitaciones de la segmentación

- Las máscaras de SAM 2 siguen siendo pseudo-máscaras, no verdad de terreno; la comparación v1/v2 es visual, sobre 30 imágenes de val y calificada por una persona.
- Con el prompt P3, la v2 hereda dónde localizó el pez la v1 (circularidad parcial); P1 no se calificó imagen por imagen.
- En una auditoría a ojo, 2 de 12 máscaras aprobadas estaban contaminadas (plato o mancha extra) y 2 de 12 descartadas eran peces grandes bien segmentados que el umbral de área elimina.
- El entrenamiento de la v2 llegó al tope de 40 épocas (mejor época 37) y se hizo una sola corrida.
- La decisión de adoptar la v2 se tomó después de ver las cuadrículas, por juicio visual directo y sin aplicar la regla fijada antes.
- SAM 2 corre con PyTorch, fuera del pipeline de Keras; es solo etiquetado offline.
- El cambio de la demo a `unet_v2` y su prueba con fotos externas están pendientes.

El detalle completo, con decisiones, cifras y glosario, está en `05_SAM2.md`.

## Estructura del repositorio

```text
sylfish-dl/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_preparacion_datos/         cuaderno, GUIA.md y 01_PREPARACION_DATOS.md
│   ├── 02_cnn/                       cuaderno, GUIA.md y 02_CNN.md
│   ├── 03_unet/                      cuaderno, GUIA.md y 03_UNET.md
│   ├── 04_demo/                      cuaderno, GUIA.md y 04_DEMO.md
│   └── 05_sam2/                      cuadernos A, B y C y 05_SAM2.md
└── reports/
    ├── figures/                      figuras de los informes
    └── tables/                       tablas de resultados (.csv, .json)
```

El repositorio solo contiene los cuadernos, sus guías y los resultados. Los datos y los modelos están en la carpeta de Drive: [\[enlace a la carpeta de Drive\]](https://drive.google.com/drive/folders/1taTrSyyyjND9iM3SYT313Oj7lgGljFiC?hl=es). Los cuadernos del 05 requieren PyTorch y SAM 2 (cuaderno B) además de TensorFlow, en sesiones de Colab separadas; esas dependencias se documentan aparte de `requirements.txt`.

## Cómo ejecutar

Se copia la carpeta de Drive ([\click acá\]](https://drive.google.com/drive/folders/1taTrSyyyjND9iM3SYT313Oj7lgGljFiC?hl=es)) a `MyDrive/sylfish/` y se monta en Colab. Los módulos 01 a 04 se abren en orden; el 01 deja `splits.csv`, las máscaras y los `.npz` en Drive. El módulo 05 se ejecuta después, en tres sesiones nuevas de Colab con GPU T4 (A, B y C, en ese orden), y deja `unet_v2.keras` y `unet_v2_umbral.json` en `models/`. La demo usa la U-Net v2: carga `unet_v2.keras` y `unet_v2_umbral.json`, con el mismo preprocesamiento de entrada que la v1 (RGB 256×256, `INTER_AREA`, dividido entre 255).

## Autores
- Jairo de Jesús Blanco Pérez
- Luis Angel Rojas Peralza
