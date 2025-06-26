# **LABORATORIO 11: – Procesamiento y análisis de señales EEG**
# **Tabla de contenidos**

1. [Introducción y Origen de los datos](#id0)
2. [Preprocesamiento](#id1)
3. [Extracción de características](#id2)
4. [Optimización y selección de features](#id3)
5. [Análisis Integrado con MNEPython](#id4)
6. [Referencias](#id5)


## **Introducción y Origen de los datos** <a name="id0"></a>

Para el desarrollo del presente trabajo se utilizaron datos de la base pública EEG Motor Movement/Imagery Dataset (EEGBCI), la cual forma parte del repositorio PhysioNet. Esta base fue creada por el grupo de investigación del sistema BCI2000, y contiene registros EEG de 109 voluntarios mientras realizaban diversas tareas motoras y de imaginación motora.

Los datos fueron adquiridos utilizando el sistema BCI2000 junto con un equipo de registro EEG de 64 canales, siguiendo el sistema internacional 10-10 (con algunas exclusiones). Las señales fueron muestreadas a una frecuencia de 160 Hz y están almacenadas en el formato EDF+ (.edf), compatible con herramientas como MNE-Python para análisis de neurofisiología.

Cada sujeto realizó 14 sesiones (runs), que incluyen:

* 2 sesiones de línea base (ojos abiertos y ojos cerrados)
* 6 sesiones de movimiento real (manos izquierda/derecha o manos/pies)
* 6 sesiones de imaginación motora de las mismas tareas.

Estas sesiones están organizadas por números de ejecución (runs), donde por ejemplo:

* runs 3, 7, 11: movimiento real de mano izquierda vs. derecha
* runs 4, 8, 12: imaginación de movimiento de mano izquierda vs. derecha
* runs 6, 10, 14: imaginación de manos vs. pies.

Para este laboratorio tomaremos en cuenta el análisis de los 3 primeros sujetos en las 6 primeras tareas:

* Basal: ojos abiertos
* Basal: ojos cerrados
* Tarea 1: abrir y cerrar el puño derecho o izquierdo
* Tarea 2: imaginar que se abre y cierra el puño derecho o izquierdo
* Tarea 3: abrir y cerrar ambos puños o ambos pies
* Tarea 4: imaginar que se abren y cierran ambos puños o ambos pies

Los archivos .edf incluyen un canal adicional de anotaciones que indica el momento de inicio de cada estímulo o tarea (marcadores T0, T1, T2).

La base de datos se encuentra disponible en acceso libre a través del siguiente enlace:

* https://physionet.org/content/eegmmidb/1.0.0/ 


## **Preprocesamiento** <a name="id1"></a>


## **Extracción de características** <a name="id2"></a>

  
## **Optimización y selección de features** <a name="id3"></a>


## **Análisis Integrado con MNEPython** <a name="id5"></a>


## **Referencias** <a name="id5"></a>



