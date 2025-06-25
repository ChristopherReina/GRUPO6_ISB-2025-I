# **LABORATORIO 10: Procesamiento de señales ECG**

# **Tabla de contenidos**

1. [Introducción](#id0)
2. [Señales generadas](#id1)
3. [Caracteristicas extraídas](#id2)
4. [Proyección PCA](#id3)
5. [Conclusiones](#id4)

## **Introducción** <a name="id0"></a>

La actividad tiene el objetivo de simular y analizar diferentes señales ECG sintéticas para extraer las características y aplicar técnicas de reducción de dimensionalidad, en este caso se aplicará el análisis de componentes principales (PCA).

## **Señales generadas** <a name="id1"></a>

* El primer paso es generar una señal ECG con parámetros iniciales conocidos: 

<image src="/Laboratorios/Laboratorio 10/lab10/1.png">

<image src="/Laboratorios/Laboratorio 10/lab10/2.png">

* Seguidamente, se debe hacer dos primeras alteraciones a la señal original:

<image src="/Laboratorios/Laboratorio 10/lab10/3.png">

<image src="/Laboratorios/Laboratorio 10/lab10/4.png">

 * Para culminar con una alteración adicional a cada una de las 3 señales sintéticas anteriores:

<image src="/Laboratorios/Laboratorio 10/lab10/5.png">

<image src="/Laboratorios/Laboratorio 10/lab10/6.png">

<image src="/Laboratorios/Laboratorio 10/lab10/7.png">

## **Caracteristicas extraídas** <a name="id2"></a>

* El siguiente paso es extraer las características de cada señal. En este caso de extrajeron la media, mediana, desviación estándar, asimetría, curtosis y variabilidad entre intervalos RR. 

<image src="/Laboratorios/Laboratorio 10/lab10/8.png">
  
## **Proyección PCA** <a name="id3"></a>

* Se utiliza el PCA para reducir la dimensionalidad de las características extraídas. El siguiente gráfico representa cómo se agrupan y separan las clases de señales generadas: 

<image src="/Laboratorios/Laboratorio 10/lab10/9.png">

<image src="/Laboratorios/Laboratorio 10/lab10/10.png">

## **Conclusiones** <a name="id5"></a>

* Esta actividad nos demuestra cómo influyen las alteraciones de las señales en las características estadísticas y los datos que se analizaran en las señales biomédicas.
* Se demuestra que las señales pueden ser diferenciadas entre clases y se puede analizar de la misma manera una señal biológica. 


