# **LABORATORIO 3: – USO DE BITalino PARA EMG y ECG**
# **Tabla de contenidos**

1. [Introducción](#id1)
2. [Propósito de la práctica](#id2)
3. [Materiales y metodología](#id3)\
     3.1 [Materiales Utilizados](#id4)\
     3.2 [Metodología](#id5)\
          3.2.1 [Colocación de electrodos](#id6)\
          3.2.2 [Configuración del sistema](#id7)\
          3.2.3 [Adquisición de datos](#id8)
4. [Procesamiento de datos](#id9)\
     4.1 [Lectura de archivos](#id10)\
     4.2 [Preprocesamiento de la señal](#id11)\
     4.3 [Análisis en ventana de 100 ms](#id12)\
     4.4 [Visualización](#id13)
6. [Resultados y limitaciones](#id14)
7. [Referencias](#id15)



## **Introducción** <a name="id1"></a>

**ECG**

El electrocardiograma (abreviado como ECG o EKG) representa un trazado eléctrico del corazón y se registra de forma no invasiva desde la superficie del cuerpo.

La máquina de ECG convencional consta de 12 derivaciones divididas en dos grupos, es decir, derivaciones de extremidades y derivaciones precordiales. Las derivaciones de extremidades se clasifican a su vez como derivaciones de extremidades bipolares estándar (I, II y III) y derivaciones unipolares aumentadas (aVL, aVF y aVR). Las derivaciones precordiales incluyen V1 a V6. Las derivaciones de extremidades ven el corazón en un plano vertical, y las derivaciones precordiales registran la actividad eléctrica del corazón en el plano horizontal. El ECG representa un registro gráfico de la actividad cardíaca eléctrica trazada en el papel del electrocardiógrafo.
El principio fundamental detrás del registro de un ECG es una fuerza, corriente o vector electromagnético con magnitud y dirección. Cuando una corriente de despolarización viaja hacia el electrodo, se registra como una deflexión positiva, y cuando se aleja del electrodo, aparece como una deflexión negativa. [1]

- Una corriente de repolarización que se aleja del electrodo positivo se considera una desviación positiva y que se dirige hacia un electrodo positivo se considera una desviación negativa.
- Cuando la corriente es perpendicular al electrodo, toca la línea base y produce una onda bifásica.

**EMG**

Las pruebas electro-diagnósticas son técnicas electrofisiológicas que se utilizan para evaluar la función y la integridad de los componentes neuromusculares, incluyendo los nervios periféricos, las raíces nerviosas, los plexos, la unión neuromuscular (UNM) y los músculos. Estas pruebas se clasifican en dos tipos principales: electromiografía de aguja (EMG) y estudios de conducción nerviosa (ECN).

La EMG evalúa la excitabilidad y las contracciones musculares tanto en condiciones fisiológicas como patológicas. Se clasifica principalmente en dos tipos: EMG de superficie no invasiva y EMG intramuscular con aguja invasiva. La EMG de superficie evalúa una amplia zona muscular accesible y se utiliza principalmente durante los registros NCS de CMAP. La EMG intramuscular con aguja, realizada por médicos con formación en electrodiagnóstico, proporciona una evaluación más detallada de la función muscular y nerviosa.


## **Propósito de la práctica** <a name="id2"></a>

* Adquirir y entender la obtención de señales EMG y ECG.
* Realizar una correcta configuración de BiTalino.
* Extraer la información de las señales EMG del software OpenSignals (r)evolution.
* Analizar los resultados obtenidos.

## **Materiales y metodología** <a name="id3"></a>

### Materiales Utilizados  <a name="id4"></a>
Para la realización del presente laboratorio se utilizaron los siguientes equipos y materiales:

- 1 Kit **BITalino (r)evolution** (versión Bluetooth)  
- 1 Módulo de electromiografía (EMG) incluido en el BITalino  
- 1 Cable de tres conductores  
- 3 Electrodos adhesivos de superficie  
- 1 Batería recargable **LiPo de 3.7V y 500 mA**  
- 1 Dispositivo móvil (celular) con Bluetooth y el software **OpenSignals (r)evolution** instalado  
- 1 Computadora personal (PC) para el procesamiento de datos  
- Pesos manuales para resistencia (aproximadamente 5 kg)

<p align="center">

  <img src="/Laboratorios/Laboratorio 03 - Adquisición de señal EMG/Fotos_EMG/materiales_1.png" alt="BITalino frontal y posterior" width="400"><br>
  <img src="/Laboratorios/Laboratorio 03 - Adquisición de señal EMG/Fotos_EMG/materiales_2.png" alt="Kit completo con electrodos y celular" width="400">
</p>

### Metodología  <a name="id5"></a>
### 1. Colocación de electrodos <a name="id6"></a>

#### 1.1 Bíceps  

Se posicionaron los tres electrodos sobre el bíceps del sujeto de prueba, siguiendo las siguientes referencias anatómicas:

- **Electrodo positivo**: sobre el vientre muscular del bíceps.  
- **Electrodo de referencia**: en la parte distal del músculo, cerca del codo.  
- **Electrodo negativo**: por encima del electrodo positivo.  

**Figura 1.** Colocación de electrodos en bíceps  
<image src="/Laboratorios/Laboratorio 03 - Adquisición de señal EMG/Fotos_EMG/electrodos_biceps.png">

---

#### 1.2 Deltoides  

De igual manera, se colocaron tres electrodos sobre el deltoides del sujeto de prueba:

- **Electrodo positivo**: sobre el vientre muscular del deltoides.  
- **Electrodo de referencia**: en el codo.  
- **Electrodo negativo**: por encima del electrodo positivo.  

**Figura 2.** Colocación de electrodos en deltoides  
<image src="/Laboratorios/Laboratorio 03 - Adquisición de señal EMG/Fotos_EMG/electrodo_deltoides.png">

---

### 2. Configuración del sistema  <a name="id7"></a>

El kit **BITalino** fue encendido y vinculado mediante Bluetooth al dispositivo móvil. Se utilizó la aplicación **OpenSignals (r)evolution** para la adquisición y visualización en tiempo real de la señal EMG. Las grabaciones fueron almacenadas en archivos `.txt` para su posterior análisis.

---

### 3. Adquisición de datos  <a name="id8"></a>

#### 3.1 Bíceps

La recolección de datos se dividió en tres etapas:

- **Reposo muscular**: tres sesiones de 30 segundos con el brazo completamente relajado sobre la mesa.  
- **Contracción dinámica libre**: tres sesiones de 30 segundos realizando movimientos de elevación y descenso del brazo sin peso.  
- **Contracción isométrica con resistencia**: tres sesiones de 30 segundos intentando levantar el brazo mientras se aplicaba una resistencia manual.

#### 3.2 Deltoides

- **Reposo**: tres sesiones de 30 segundos en estado de relajación.  
- **Contracción dinámica con peso**: tres sesiones de 20 segundos realizando elevaciones y descensos del brazo con una carga externa (aprox. 4 kg).

---

### 4. Procesamiento de datos  <a name="id9"></a>

Los archivos obtenidos desde el software **OpenSignals (r)evolution** fueron transferidos a una computadora personal para su análisis. Se utilizó el entorno de desarrollo **Anaconda**, ejecutando un **Jupyter Notebook**, con un script en Python. Las bibliotecas empleadas fueron: 
- `os` : Proporciona funciones para interactuar con el sistema operativo, como listar archivos en un directorio. [3]
- `pandas`: Permite la manipulación y el análisis de datos. Se utiliza para leer los datos de los archivos .txt. [4]
- `numpy`: Proporciona soporte para arrays, funciones matemáticas y más. [5]
- `matplotlib.pyplot`: Permite crear visualizaciones como gráficos. [6]
- `scipy.signal`: Un sub-módulo de SciPy que proporciona herramientas de procesamiento de señales, incluyendo funciones para diseñar y aplicar filtros. `butter` se utiliza para crear un filtro Butterworth, y `filtfilt` aplica el filtro. [7]

#### 4.1 Lectura de archivos

- Se recorrieron los archivos `.txt` almacenados localmente.
- Se identificó la cabecera `"EndOfHeader"` para ubicar el inicio de los datos.
- La señal EMG se extrajo del canal analógico **A1**.

#### 4.2 Preprocesamiento de la señal

- **Centrado**: se eliminó el componente de continua (DC) restando la media de la señal.
- **Normalización**: la señal fue escalada entre -1 y 1.
- **Filtrado pasa banda**: se aplicó un filtro Butterworth de orden 4 con un rango de 20 a 450 Hz, eliminando frecuencias no representativas del EMG.

#### 4.3 Análisis en ventana de 100 ms

- Se seleccionó una ventana de 0.1 segundos desde el inicio de la señal filtrada.
- Se generó un eje de tiempo correspondiente a dicho intervalo.
- Se graficó la señal EMG en el dominio del tiempo.
- Se calculó la **Transformada Rápida de Fourier (FFT)** y se representó en escala de decibelios (dB).

#### 4.4 Visualización

- Se representó la señal EMG filtrada correspondiente a los primeros 100 ms.
- Se graficó el espectro de frecuencias obtenido mediante la FFT.
- El análisis frecuencial se limitó hasta la **frecuencia de Nyquist** (500 Hz), de acuerdo con la frecuencia de muestreo de 1000 Hz del dispositivo BITalino.

## **Resultados y limitaciones** <a name="id10"></a>

## **Referencias** <a name="id11"></a>
[1] Sattar Y, Chhabra L. Electrocardiogram. En: StatPearls. Treasure Island (FL): StatPearls Publishing; 2025.\
[2] Ramani PK, Lui F, Arya K. Nerve conduction studies and electromyography. En: StatPearls. Treasure Island (FL): StatPearls Publishing; 2025.\
[3] Python documentation [Internet]. [citado el 12 de abril de 2025]. os — Miscellaneous operating system interfaces. \
[4] The pandas development team. pandas-dev/pandas: Pandas [Internet] 2025. \
[5] numpy/numpy: The fundamental package for scientific computing with Python. [Internet]. \
[6] Hunter JD. Matplotlib: A 2D graphics environment [Internet]. Vol. 9, Computing in Science & Engineering. 2007. p. 90–5. \
[7] scipy/scipy [Internet]. SciPy; 2025.



