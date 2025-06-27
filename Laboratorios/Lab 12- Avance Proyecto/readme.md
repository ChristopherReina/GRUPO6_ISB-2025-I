# **LABORATORIO 12: Avance de proyecto**

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

Esta base de datos fue seleccionada debido a su alta densidad de señales sEMG (448 canales), contenido de señales relaciondas a movimientos del antebrazo y muñeca, fundamentales para detectar patrones musculares asociados al síndrome del túnel carpiano. Además de tratarse de señales sin filtrar ni procesar de personas sanas.

### **A database of hand kinematics, high-density sEMG of forearm and wrist for motion intent recognition v1.0.0**

- **Tipo**: sEMG de alta densidad (HD-sEMG).
- **Descripción**: Los electrodos fueron colocados en anillos alrededor del antebrazo y muñeca, cubriendo tanto flexores como extensores.
- **Rango de edad**: 21 a 35 años.
- **Frecuencia de muestreo**: 200 Hz.
- **Dispositivo**: Guante 5DT Data Glove 14 Ultra.

Este conjunto de datos contiene información tanto de señales neuromusculares como de la cinemática del movimiento de la mano, lo cual es clave para el análisis de intenciones de movimiento, en particular, para la identificación de patrones asociados a trastornos como el STC.

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
- **MAV (Valor absoluto medio)**: Mide el nivel de activación muscular.
- **WL (Variación de la longitud)**: Evalúa la complejidad de la contracción.
- **RMS (Raíz cuadrada media)**: Calcula la energía muscular.
- **Media y Varianza**: Indicadores básicos para entender la distribución de la actividad muscular.

---

## **Base de datos adicional** <a name="id3"></a>

### **Dataset on Bilateral Idiopathic Carpal Tunnel Syndrome: Crossover Study of Two Combined Physiotherapeutic Treatment Methods on Chirurgical and Clinical Patients**

Este dataset incluye 73 participantes con **síndrome del túnel carpiano bilateral idiopático** que fueron sometidos a dos métodos de tratamiento fisioterapéutico combinados: **movilización miofascial (IASTM)** y **estiramiento**. Se incluye tanto a pacientes clínicos como quirúrgicos.

La adición de esta base de datos nos permitirá una comparación entre los **trabajadores sanos** y **los pacientes con STC**, para poder clasificar y detectar patrones específicos de esta enfermedad en los trabajadores de oficina.

---

## **Avances y siguientes pasos** <a name="id4"></a>

### **Avances hasta la fecha**:

#### **Procesamiento de datos y PCA**:
Se ha utilizado la técnica de **Análisis de Componentes Principales (PCA)** para reducir las dimensiones de los datos y visualizar la distribución de las señales EMG. Los resultados incluyen:

1. **Distribución de gestos musculares**: Tras aplicar PCA, se observó cómo los diferentes gestos musculares se distribuyen en el espacio de características reducido. Cada punto representa un canal EMG, y se ha utilizado la reducción dimensional para facilitar el análisis visual. Para agilizar el análisis de los cientos de archivos pertenecientes a la base de datos encontrada se migró de Google Colab a Visual Studio Code para aprovechar las capacidades de procesamiento locales de la computadora usada. 
   PCA usando Visual Studio Code. Presentó mayor capacidad de procesamiento y se logró incluir más archivos y más datos.
 <image src="/Laboratorios/Lab 12- Avance Proyecto/1.png">
   PCA usando Google Colab. Encontramos limitaciones para incluir la cantidad necesaria de información
 <image src="/Laboratorios/Lab 12- Avance Proyecto/3.png">

2. **Curva ROC**: Tras entrenar un clasificador **Random Forest** utilizando señales EMG de personas "sanas", se ha generado una curva ROC para evaluar el rendimiento del clasificador en términos de sensibilidad y especificidad. Esto para lograr medir la efectividad de la clasificación de señales EMG.

<image src="/Laboratorios/Lab 12- Avance Proyecto/2.png">


### **Siguientes pasos**:

- **Comparación de datos**: Se realizará un análisis comparativo entre los datos de **personas sanas** y **personas con síndrome del túnel carpiano (STC)**. Este análisis nos permitirá identificar diferencias clave en las señales EMG asociadas con el STC.
  
- **Clasificación**: El siguiente paso es entrenar modelos de clasificación (como **Random Forest** y otros algoritmos de aprendizaje automático) para **distinguir entre personas sanas y pacientes con STC** usando los datos obtenidos de las bases de datos mencionadas.

- **Optimización de procesamiento**: El código ha sido migrado a **Visual Studio Code** para aprovechar una máquina de mayor rendimiento, acelerando el procesamiento de los cientos de archivos de señales EMG. Esto también ayuda a evitar las limitaciones de Google Colab para el procesamiento de datos a gran escala.
