# Taller Práctico: Fundamentos de Análisis de Sentimientos y NLP

## Introducción

Este directorio contiene una serie de ejercicios prácticos y autocontenidos diseñados para enseñar los conceptos fundamentales del Procesamiento de Lenguaje Natural (NLP) y el análisis de sentimientos desde cero. Cada script es un "laboratorio" independiente que aborda una técnica específica, permitiendo un aprendizaje incremental y enfocado.

El objetivo no es construir una aplicación compleja, sino entender la **mecánica interna** de cada paso del proceso, desde la limpieza de texto hasta la aplicación de algoritmos de Machine Learning para descubrir patrones.

## El Corpus: Nuestro Laboratorio de Texto

Todos los ejercicios utilizan un pequeño conjunto de frases en español definido directamente en el código. Esto nos permite centrarnos exclusivamente en las técnicas de NLP sin la complejidad de la recolección de datos.

```python
corpus = [
    "Me encanta este producto, es fantástico y muy útil.",
    "El servicio al cliente fue terrible, muy decepcionante.",
    "El precio es adecuado, ni caro ni barato.",
    "No volvería a comprar, la calidad es pésima.",
    "Una experiencia increíble, lo recomiendo totalmente.",
    "El envío tardó más de lo esperado.",
    "Fantástico, simplemente fantástico.",
    "No está mal, pero podría mejorar.",
    "La batería dura poquísimo, un desastre."
]
```

---

## Guía de Ejercicios

### Ejercicio 1: `01_conteo_palabras.py`

*   **Objetivo:** Comprender que el primer paso del NLP es convertir el texto en datos numéricos. Aprender a tokenizar, normalizar y contar frecuencias de palabras.
*   **Técnicas Clave:**
    1.  **Normalización:** Convertir todo el texto a minúsculas (`.lower()`).
    2.  **Tokenización:** Usar expresiones regulares (`re.findall`) para dividir el texto en una lista de palabras (tokens), eliminando la puntuación.
    3.  **Conteo de Frecuencias:** Utilizar la clase `Counter` del módulo `collections` para contar eficientemente las apariciones de cada palabra.
*   **Visualización:** Se genera un **gráfico de barras** con `matplotlib` que muestra las 10 palabras más frecuentes.
*   **Lección Principal:** Al ejecutar este script, se observa que las palabras más comunes son "stopwords" (`es`, `el`, `y`, `muy`), que no aportan significado sobre el tema o sentimiento. Esto demuestra la necesidad del siguiente paso: la limpieza.

### Ejercicio 2: `02_limpieza_texto.py`

*   **Objetivo:** Aprender a eliminar el "ruido" del texto mediante la filtración de *stopwords* y visualizar el impacto directo de esta limpieza.
*   **Técnicas Clave:**
    1.  **Creación de un Set de Stopwords:** Se define un `set` de palabras comunes en español para una búsqueda y filtrado eficientes.
    2.  **Filtrado:** Se recorren los tokens y se descartan aquellos que están presentes en el set de stopwords.
*   **Visualización:** Se crea una figura con dos **gráficos de barras comparativos**. El de la izquierda muestra las frecuencias *antes* de la limpieza y el de la derecha las muestra *después*.
*   **Lección Principal:** La comparación visual es drástica. El segundo gráfico revela las palabras con verdadero contenido semántico (`fantástico`, `producto`, `calidad`, `terrible`), demostrando que la limpieza de texto es un paso indispensable para un análisis significativo.

### Ejercicio 3: `03_sentimiento_por_lexicon.py`

*   **Objetivo:** Construir un primer clasificador de sentimientos funcional utilizando un método basado en reglas (léxicos).
*   **Técnicas Clave:**
    1.  **Léxicos de Sentimiento:** Se crean dos `set` de palabras: uno con términos positivos y otro con términos negativos.
    2.  **Puntuación (Scoring):** Para cada frase, se cuenta el número de palabras positivas y negativas. El puntaje final se calcula como `(palabras positivas) - (palabras negativas)`.
    3.  **Clasificación:** Las frases se etiquetan como "Positiva", "Negativa" o "Neutra" basándose en si su puntaje es mayor, menor o igual a cero.
*   **Visualización:** Se genera un **gráfico de tarta (pie chart)** que muestra la distribución porcentual de los sentimientos en todo el corpus.
*   **Lección Principal:** Este método es simple, rápido e interpretable (sabemos exactamente por qué una frase fue clasificada de cierta manera). Sin embargo, también expone sus limitaciones, como su incapacidad para entender el contexto o la negación (ej. "No está mal" es clasificado como negativo).

### Ejercicio 4: `04_similitud_jaccard.py`

*   **Objetivo:** Aprender a cuantificar cuán similares son dos documentos de texto entre sí.
*   **Técnicas Clave:**
    1.  **Conjuntos de Palabras:** Cada frase se convierte en un `set` de sus palabras únicas (después de la limpieza).
    2.  **Similitud de Jaccard:** Se implementa la fórmula `|A ∩ B| / |A ∪ B|` para calcular un puntaje de similitud entre 0 y 1 para cada par de frases.
    3.  **Matriz de Similitud:** Se construye una matriz cuadrada donde cada celda `(i, j)` contiene el puntaje de similitud entre la frase `i` y la frase `j`.
*   **Visualización:** Se utiliza `seaborn` para crear un **mapa de calor (heatmap)** de la matriz de similitud. Los colores más "cálidos" (rojos) indican una alta similitud.
*   **Lección Principal:** La visualización nos permite identificar patrones de similitud de un vistazo. Es una herramienta fundamental para tareas de agrupación y búsqueda de información.

### Ejercicio 5: `05_vectorizacion_y_clustering.py`

*   **Objetivo:** Dar el salto al Machine Learning no supervisado, agrupando automáticamente las frases por su contenido semántico sin conocimiento previo de su sentimiento.
*   **Técnicas Clave:**
    1.  **Vectorización TF-IDF:** Se utiliza `TfidfVectorizer` de `scikit-learn` para transformar cada frase en un vector numérico. A diferencia del conteo simple, TF-IDF da más importancia a las palabras que son frecuentes en un documento pero raras en el resto del corpus.
    2.  **Clustering K-Means:** Se aplica el algoritmo `KMeans` sobre la matriz TF-IDF para agrupar los vectores de las frases en un número predefinido de clusters (en nuestro caso, 3).
    3.  **Reducción de Dimensionalidad (PCA):** Se usa `PCA` (Análisis de Componentes Principales) para reducir los vectores TF-IDF de alta dimensionalidad a solo 2 dimensiones, para que puedan ser representados en un gráfico.
*   **Visualización:** Se genera un **gráfico de dispersión (scatter plot)**. Cada punto en el gráfico es una frase. La posición del punto viene determinada por sus 2 componentes principales, y su color por el cluster que K-Means le asignó.
*   **Lección Principal:** Este ejercicio demuestra el poder del aprendizaje no supervisado. Sin decirle nada sobre sentimientos, el algoritmo es capaz de agrupar las frases positivas, negativas y neutras, revelando la estructura latente en los datos. Es el puente perfecto entre el NLP clásico y las aplicaciones de Machine Learning más avanzadas.
