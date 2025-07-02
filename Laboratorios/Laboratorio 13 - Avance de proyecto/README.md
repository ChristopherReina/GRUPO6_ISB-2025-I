# **LABORATORIO 13: Avance de proyecto**

## **Síndrome del túnel carpiano en trabajadores de oficina**

---

### **Tabla de contenidos**

1. [Introducción](#id0)
2. [Bases de datos](#id1)
3. [Características e investigación](#id2)
4. [Base de datos adicional](#id3)
5. [Avances y siguientes pasos](#id4)

---

## **Introducción** <a name="id0"></a>

El **síndrome del túnel carpiano (STC)** es una dolencia provocada por la inflamación y la presión en el interior del túnel formado por el carpo y el ligamento carpiano transverso en la muñeca, donde se encuentran diversos tendones y el nervio mediano. Esta condición es común en personas que realizan movimientos repetitivos con las manos y muñecas, como trabajadores de oficina, lo que puede generar síntomas como dolor, entumecimiento y debilidad en la mano.

---

## **Bases de datos** <a name="id1"></a>

### **Gesture Recognition and Biometrics ElectroMyogram (GRABMyo) v1.1.0**

- **Tipo**: Electromiografía de superficie (sEMG).
- **Descripción**: Los electrodos se colocaron en forma de anillos alrededor del antebrazo y la muñeca, abarcando flexores y extensores del antebrazo.
- **Rango de edad**: 24–35 años.
- **Frecuencia de muestreo**: 2048 Hz.
- **Duración por gesto**: 5 segundos por repetición.
- **Total de repeticiones por gesto**: 7.

Esta base de datos fue seleccionada debido a su alta densidad de señales sEMG (448 canales), contenido de señales relacionadas a movimientos del antebrazo y muñeca, fundamentales para detectar patrones musculares asociados al síndrome del túnel carpiano. Además de tratarse de señales sin filtrar ni procesar de personas sanas.

### **A database of hand kinematics, high-density sEMG of forearm and wrist for motion intent recognition v1.0.0**

- **Tipo**: sEMG de alta densidad (HD-sEMG).
- **Descripción**: Los electrodos fueron colocados en anillos alrededor del antebrazo y muñeca, cubriendo tanto flexores como extensores.
- **Rango de edad**: 21 a 35 años.
- **Frecuencia de muestreo**: 200 Hz.
- **Dispositivo**: Guante 5DT Data Glove 14 Ultra.

Este conjunto de datos contiene información tanto de señales neuromusculares como de la cinemática del movimiento de la mano, lo cual es clave para el análisis de intenciones de movimiento, en particular, para la identificación de patrones asociados a trastornos como el STC.

### **Dataset on Bilateral Idiopathic Carpal Tunnel Syndrome: Crossover Study of Two Combined Physiotherapeutic Treatment Methods on Chirurgical and Clinical Patients**

Este dataset incluye 73 participantes con **síndrome del túnel carpiano bilateral idiopático** que fueron sometidos a dos métodos de tratamiento fisioterapéutico combinados: **movilización miofascial (IASTM)** y **estiramiento**. Se incluye tanto a pacientes clínicos como quirúrgicos.

La adición de esta base de datos nos permitirá una comparación entre los **trabajadores sanos** y **los pacientes con STC**, para poder clasificar y detectar patrones específicos de esta enfermedad en los trabajadores de oficina.

---

### **Complex Upper-Limb Movements v1.0.0**

- **Tipo**: Captura de movimiento 3D (VICON).
- **Descripción**: Uso de cámaras con marcadores reflectantes para reconstruir la trayectoria 3D de la mano.
- **Edad promedio**: 26.4 ± 45.2 años.
- **Enfoque**: Cinética de la mano (movimiento externo), no señales neuromusculares.

Este conjunto de datos se utiliza para estudiar el movimiento de la mano, sin embargo, no está relacionado directamente con las señales musculares, lo que complementa los datos de EMG con información adicional sobre la biomecánica del movimiento.

---

## **Características e investigación** <a name="id2"></a>

### **Coeficientes de Aproximación (A) y Detalle (D)**

- **Aproximación (A)**: Captura las tendencias de baja frecuencia, representando la actividad muscular real. Es crucial para analizar la activación de los músculos.
- **Detalle (D)**: Captura frecuencias altas que pueden incluir tanto ruido como eventos rápidos de contracción. Es útil para detectar eventos de alta frecuencia si se manejan adecuadamente.

Utilizando **escalas de 16 y 32** (Mexican Hat y Symlet 6 respectivamente), es posible ajustar la resolución temporal y la capacidad de detección de eventos, con **escala 16** siendo ideal para eventos rápidos y **escala 32** para patrones más lentos o suaves.

### **Características estadísticas para el análisis de EMG**:
- **MAV (Valor absoluto medio)**: Medida de la amplitud de la señal EMG y se calcula sumando el valor absoluto de todas las muestras de la señal y dividiendo por el número total de muestras. Mide el nivel de activación muscular.
- **WL (Variación de la longitud)**: Evalúa la complejidad de la contracción.
- **RMS (Raíz cuadrada media)**: Calcula la energía muscular. Valores altos de RMS indican una mayor cantidad de actividad muscular (más contracción), mientras que valores bajos indican una contracción más débil o relajación muscular.
- **Media y Varianza**: Indicadores básicos para entender la distribución de la actividad muscular.

---


## **Avances y siguientes pasos** <a name="id4"></a>

### **Avances hasta la fecha**:

#### **Pruebas del modelo con señales de pacientes con STC**:

Se probó el modelo de clasificación en **5 señales de una base de datos con características de pacientes con STC**. Para ello, se extrajeron las siguientes características importantes de las señales: **mean, std, RMS, skewness, entropy, y kurtosis**.

Estas características se mostraron en un gráfico PCA para visualizar su distribución en un espacio reducido de características.

Posteriormente, se entrenó un modelo de **Random Forest** para clasificar las señales como pertenecientes a un caso **sano (0)** o de **STC (1)**.

El modelo fue evaluado y se obtuvo una **precisión de 1**, lo que indica una **gran efectividad** en la clasificación. Además, se generaron **curvas ROC** para evaluar la capacidad del modelo para distinguir entre los dos grupos.

Para probar el modelo de clasificación, se generaron **5 señales artificiales** con características de **STC**. El algoritmo de clasificación proporcionó resultados afirmativos para todas las señales, confirmando su efectividad en la detección del STC.

#### **Evaluación del modelo**:

- **Precisión**: El modelo logró una precisión de 1, lo que indica que tiene una alta efectividad para clasificar señales de **STC** y **sanas**.


- **Curvas ROC**: Las curvas ROC generadas mostraron un rendimiento excelente del modelo, 

<image src="/Laboratorios/Laboratorio 13 - Avance de proyecto/archivos/ROC_random_forest.jpeg">
  Esta característica del modelo también aplica para la diferenciación entre señales normales y con STC.
<image src="/Laboratorios/Laboratorio 13 - Avance de proyecto/archivos/roc_normal_vs_STC.png">

**Gráfico PCA de características**:

- Las características principales de las 5 señales fueron extraídas, estas son entradas del modelo entrenado para que determine si se trata de un patrón normal o de STC

 <image src="/Laboratorios/Laboratorio 13 - Avance de proyecto/archivos/Extracción_características_5señales.png">
   
- Se visualizó un gráfico PCA de las características importantes extraídas (mean, std, RMS, skewness, entropy, kurtosis) para observar la distribución de las señales y cómo se separan las señales sanas de las de STC.

 <image src="/Laboratorios/Laboratorio 13 - Avance de proyecto/archivos/PCA_5señales.png">
   
   Se observan 5 puntos debido a las 5 señales analizadas con STC

**Resultados de predicción para las señales**:
Se observa el ploteo de la señal generada con características de STC para observar el resultado y la efectividad del modelo
 <image src="/Laboratorios/Laboratorio 13 - Avance de proyecto/archivos/Señal1.png">


---

### **Siguientes pasos**:

- **Comparación de datos**: Se realizará un análisis comparativo entre los datos de **personas sanas** y **personas con síndrome del túnel carpiano (STC)**. Este análisis nos permitirá identificar diferencias clave en las señales EMG asociadas con el STC.
  
- **Clasificación**: El siguiente paso es entrenar modelos de clasificación (como **Random Forest** y otros algoritmos de aprendizaje automático) para **distinguir entre personas sanas y pacientes con STC** usando los datos obtenidos de las bases de datos mencionadas.

- **Optimización de procesamiento**: El código ha sido migrado a **Visual Studio Code** para aprovechar una máquina de mayor rendimiento, acelerando el procesamiento de los cientos de archivos de señales EMG. Esto también ayuda a evitar las limitaciones de Google Colab para el procesamiento de datos a gran escala.

---
