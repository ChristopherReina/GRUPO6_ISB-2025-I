# **LABORATORIO 10: Procesamiento de señales ECG**

# **Tabla de contenidos**

1. [Introducción](#id0)
2. [Señales generadas](#id1)
3. [Caracteristicas extraídas](#id2)


## **Introducción** <a name="id0"></a>

La actividad tiene el objetivo de simular y analizar diferentes señales ECG sintéticas para extraer las características y aplicar técnicas de reducción de dimensionalidad, en este caso se aplicará el análisis de componentes principales (PCA).

## **Señales generadas** <a name="id1"></a>

El primer paso es generar una señal ECG con parámetros iniciales conocidos: 
<image src="/Laboratorios/Laboratorio 10/lab10/1.png">
[foto 2]

Seguidamente, se debe hacer dos primeras alteraciones a la señal original:
[foto 3]
[foto 4]

 Para culminar con una alteración adicional a cada una de las 3 señales sintéticas anteriores:
[foto 5]
[foto 6]
[foto 7]

## **Caracteristicas extraídas** <a name="id2"></a>

El siguiente paso es extraer las características de cada señal. En este caso de extrajeron la media, mediana, desviación estándar, asimetría, curtosis y variabilidad entre intervalos RR. 

[foto 8]
  
## **Proyección PCA** <a name="id4"></a>

Se utiliza el PCA para reducir la dimensionalidad de las características extraídas. El siguiente gráfico representa cómo se agrupan y separan las clases de señales generadas: 

[foto 9]
[foto 10]

