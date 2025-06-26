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

### Señal Concatenada: ###

* Carga de los datos crudos (EDF)
El primer paso realizado fue la carga de los datos crudos utilizando la función read_raw_edf de la librería MNE-Python. Esta función permite leer archivos en formato .edf, utilizado para almacenar señales biomédicas como EEG. Se especificó el parámetro preload=True para que los datos se carguen completamente en memoria, lo cual es necesario para aplicar filtros y análisis posteriores sin problemas de acceso. El resultado de este paso es una lista de objetos Raw correspondientes a las diferentes secciones o bloques de cada sujeto.

* Concatenación de registros por sujeto
Se concatenaron todas las grabaciones para cada sujeto de prueba con la función mne.concatenate_raws. Esto es importante porque recogemos muchos estudios del mismo sujeto (6 tareas para uno de los 3) en múltiples sesiones (“runs”) que, por separado, dificultarían el análisis continuo. Unificando estos datos se obtiene una única señal de EEG por sujeto que representa toda su actividad cerebral registrada.

* Visualización de señal original
Se realizó una visualización inicial de la señal cruda para cada sujeto para detectar de forma visual artefactos evidentes como ruidos de línea base, movimientos oculares, o interrupciones en la señal. Además, sirve como referencia para evaluar los efectos de los filtros y limpiezas que se aplicarán a continuación.

* Filtrado pasabanda (1–40 Hz)
Luego, se aplicó un filtro pasabanda entre 1 y 40 Hz. Este tipo de filtrado elimina componentes de muy baja frecuencia (como las derivaciones lentas del movimiento o la línea base) y frecuencias altas (como interferencias musculares o ruido de alta frecuencia). De esta manera, se conservan las bandas de interés del EEG (delta, theta, alfa, beta), facilitando un análisis más centrado en la actividad cerebral real del sujeto. El resultado es una señal significativamente más clara y específica.

* Filtro Notch (60 Hz)
Para eliminar el ruido producido por la red eléctrica, se utilizó un filtro notch centrado en 60 Hz, frecuencia típica de interferencia en la mayoría de países de América. Este tipo de interferencia suele ser constante y puede contaminar los registros de EEG, generando una distorsión artificial en la señal. Al aplicar el filtro notch, se atenúa esta frecuencia específica, mejorando aún más la limpieza de la señal.

* Análisis de Componentes Independientes (ICA)
Una vez filtrada la señal, se procedió a aplicar el Análisis de Componentes Independientes (ICA) para descomponer la señal en una serie de componentes estadísticamente independientes entre sí. Su utilidad radica en que muchos artefactos fisiológicos como los parpadeos, la actividad muscular o la señal del corazón tienden a aparecer como componentes independientes en la señal, por lo que pueden ser identificados y eliminados sin afectar el resto de la actividad cerebral. En este caso, se utilizaron 20 componentes para lograr una descomposición adecuada de la señal.

* Identificación y exclusión de componentes
Sse identificaron manualmente los componentes considerados artefactos (por ejemplo, los relacionados con parpadeos u otros ruidos fisiológicos) y se marcaron para su exclusión. Esto se hizo indicando los índices correspondientes (en este caso [0, 1]), que luego serían eliminados de la reconstrucción final de la señal. La identificación visual de estos componentes se basa en su forma característica y en su correlación con eventos específicos como movimientos oculares.

* Aplicación del ICA para limpiar la señal
Se reconstruyó la señal limpia aplicando el modelo ICA entrenado, eliminando los componentes indeseados. Esto permitió obtener una señal EEG depurada, más representativa de la actividad neuronal, y libre de interferencias provenientes del entorno o del propio cuerpo del sujeto. Esta señal limpia se visualizó nuevamente, lo cual permitió verificar de forma cualitativa que los artefactos habían sido eliminados con éxito, y que la forma general de la señal se había mantenido sin distorsiones.

### Señal sin concatenar: ###

* Carga de datos EEG (EDF)
Se cargaron archivos .edf para cada sujeto y tarea utilizando read_raw_edf con preload=True, lo que permitió tener los datos completos en memoria para un procesamiento más eficiente.

* Visualización inicial
Se visualizaron los primeros 10 segundos de la señal cruda para cada tarea con el fin de detectar artefactos evidentes y conocer la forma general de la señal antes del procesamiento.

* Filtrado pasabanda (1–40 Hz)
Se aplicó un filtro entre 1 y 40 Hz para conservar las bandas EEG de interés (delta, theta, alfa, beta), eliminando ruidos de baja y alta frecuencia.

* Filtro notch (60 Hz)
Se utilizó un filtro notch para eliminar interferencias eléctricas comunes a 60 Hz, mejorando la limpieza de la señal.

* Análisis ICA
Se aplicó el Análisis de Componentes Independientes (ICA) para separar y remover artefactos fisiológicos (como parpadeos). Se excluyeron los componentes considerados ruidos.

* Señal limpia
Se reconstruyó la señal limpia tras aplicar ICA y se visualizó nuevamente para verificar la eliminación efectiva de los artefactos sin perder la información cerebral relevante.


### Montaje de los electrodos ###

<image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/1.png">

### Señal concatenada (2s por cada tarea, 10 s en total): ###
### Sujeto 1 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/2.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/3.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/4.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/5.png">      |   
|   Señal limpia ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/6.png">      |    

### Señal por cada tarea (10s): ###

### Sujeto 1 - Basal 1 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/7.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/8.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/9.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/10.png">      |   

### Sujeto 1 - Basal 2 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/11.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/12.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/13.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/14.png">      |   

### Sujeto 1 - Tarea 1 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/1.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/2.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/3.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/4.png">      |   

### Sujeto 1 - Tarea 2 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/5.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/6.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/7.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/8.png">      |   

### Sujeto 1 - Tarea 3 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/9.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/10.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/11.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/12.png">      |   

### Sujeto 1 - Tarea 4 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/13.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/14.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/15.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj1/tarea/16.png">      |   

-----------------------------------------------------------------------------------------

### Señal concatenada (2s por cada tarea, 10 s en total): ###
### Sujeto 2 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/1.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/2.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/3.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/4.png">      |   
|   Señal limpia ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/5.png">      |    

### Señal por cada tarea (10s): ###

### Sujeto 2 - Basal 1 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/6.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/7.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/8.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/9.png">      |   

### Sujeto 2 - Basal 2 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/10.png">  | 
| Filtro pasabandas |   <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/11.png">  |     
|    Notch    |      <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/12.png">     |   
|   Artefactos ICA    |     <image src="/Laboratorios/Laboratorio 11 - Procesamiento y análisis de señales EEG/fotos/suj2/13.png">      |   

### Sujeto 2 - Tarea 1 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto 1]  | 
| Filtro pasabandas |   [foto2]  |     
|    Notch    |      [foto3]     |   
|   Artefactos ICA    |     [foto4]      |   

### Sujeto 2 - Tarea 2 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto5]  | 
| Filtro pasabandas |   [foto6]  |     
|    Notch    |      [foto7]     |   
|   Artefactos ICA    |     [foto8]      |   

### Sujeto 2 - Tarea 3 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto9]  | 
| Filtro pasabandas |   [foto10]  |     
|    Notch    |      [foto11]     |   
|   Artefactos ICA    |     [foto12]      |   

### Sujeto 2 - Tarea 4 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto13]  | 
| Filtro pasabandas |   [foto14]  |     
|    Notch    |      [foto15]     |   
|   Artefactos ICA    |     [foto16]      |   

-----------------------------------------------------------------------------------------

### Señal concatenada (2s por cada tarea, 10 s en total): ###
### Sujeto 3 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto1]  | 
| Filtro pasabandas |   [foto2]  |     
|    Notch    |      [foto3]     |   
|   Artefactos ICA    |     [foto4]      |   
|   Señal limpia ICA    |     [foto5]      |    

### Señal por cada tarea (10s): ###

### Sujeto 3 - Basal 1 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto6]  | 
| Filtro pasabandas |   [foto7]  |     
|    Notch    |      [foto8]     |   
|   Artefactos ICA    |     [foto9]      |   

### Sujeto 3 - Basal 2 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto10]  | 
| Filtro pasabandas |   [foto11]  |     
|    Notch    |      [foto12]     |   
|   Artefactos ICA    |     [foto13]      |   

### Sujeto 3 - Tarea 1 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto 1]  | 
| Filtro pasabandas |   [foto2]  |     
|    Notch    |      [foto3]     |   
|   Artefactos ICA    |     [foto4]      |   

### Sujeto 3 - Tarea 2 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto5]  | 
| Filtro pasabandas |   [foto6]  |     
|    Notch    |      [foto7]     |   
|   Artefactos ICA    |     [foto8]      |   

### Sujeto 3 - Tarea 3 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto9]  | 
| Filtro pasabandas |   [foto10]  |     
|    Notch    |      [foto11]     |   
|   Artefactos ICA    |     [foto12]      |   

### Sujeto 3 - Tarea 4 ###

|  **Proceso**  | **Ploteo** | 
|:------------:|:---------------:|
| Original |   [foto13]  | 
| Filtro pasabandas |   [foto14]  |     
|    Notch    |      [foto15]     |   
|   Artefactos ICA    |     [foto16]      |   

------------------------------------------------------------------------------

## **Extracción de características** <a name="id2"></a>

  
## **Optimización y selección de features** <a name="id3"></a>


## **Análisis Integrado con MNEPython** <a name="id5"></a>


## **Referencias** <a name="id5"></a>



