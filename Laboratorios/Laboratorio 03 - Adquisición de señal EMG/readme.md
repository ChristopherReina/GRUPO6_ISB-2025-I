# **LABORATORIO 3: – USO DE BITalino PARA EMG y ECG**
# **Tabla de contenidos**

1. [Introducción](#id1)
2. [Propósito de la práctica](#id2)
3. [Materiales y metodología](#id3)\
     3.1 [Conexión usada](#id4)\
     3.2 [Video de la señal](#id5)\
     3.3 [Ploteo de la señal en OpenSignal](#id6)\
     3.4 [Archivos](#id7)
4. [Resultados y limitaciones](#id8)
5. [Referencias](#id9)



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

### Materiales Utilizados
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

### Metodología
### 1. Colocación de electrodos

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

### 2. Configuración del sistema

El kit **BITalino** fue encendido y vinculado mediante Bluetooth al dispositivo móvil. Se utilizó la aplicación **OpenSignals (r)evolution** para la adquisición y visualización en tiempo real de la señal EMG. Las grabaciones fueron almacenadas en archivos `.txt` para su posterior análisis.

---

### 3. Adquisición de datos

#### 3.1 Bíceps

La recolección de datos se dividió en tres etapas:

- **Reposo muscular**: tres sesiones de 30 segundos con el brazo completamente relajado sobre la mesa.  
- **Contracción dinámica libre**: tres sesiones de 30 segundos realizando movimientos de elevación y descenso del brazo sin peso.  
- **Contracción isométrica con resistencia**: tres sesiones de 30 segundos intentando levantar el brazo mientras se aplicaba una resistencia manual.

#### 3.2 Deltoides

- **Reposo**: tres sesiones de 30 segundos en estado de relajación.  
- **Contracción dinámica con peso**: tres sesiones de 20 segundos realizando elevaciones y descensos del brazo con una carga externa (aprox. 4 kg).

---

### 4. Procesamiento de datos

Los archivos obtenidos desde el software **OpenSignals (r)evolution** fueron transferidos a una computadora personal para su análisis. Se utilizó el entorno de desarrollo **Anaconda**, ejecutando un **Jupyter Notebook**, con un script en Python. Las bibliotecas empleadas fueron:

```python
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

```

### **Conexión usada** <a name="id4"></a>

### **Video de la señal** <a name="id5"></a>

### **Ploteo de la señal en OpenSignal** <a name="id6"></a>

### **Archivos** <a name="id7"></a>

## **Resultados y limitaciones** <a name="id8"></a>

## **Referencias** <a name="id9"></a>
[1] Sattar Y, Chhabra L. Electrocardiogram. En: StatPearls. Treasure Island (FL): StatPearls Publishing; 2025.\
[2] Ramani PK, Lui F, Arya K. Nerve conduction studies and electromyography. En: StatPearls. Treasure Island (FL): StatPearls Publishing; 2025.\
