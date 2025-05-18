# Análisis y Filtrado de Señales Biomédicas con Transformada Wavelet

## Índice

- [Objetivos](#objetivos)
- [Introducción](#introducción)
- [Materiales y Equipos](#materiales-y-equipos)
- [Metodología](#metodología)
- [Señales](#señales)
  - [EMG](#emg)
  - [ECG](#ecg)
  - [EEG](#eeg)
- [Resumen y Discusión](#resumen-y-discusión)
- [Bibliografía](#bibliografía)

---

## Objetivos

Aplicar la transformada wavelet para el análisis y reducción de ruido en señales biomédicas (EMG, ECG, EEG) destacando sus ventajas sobre otros métodos tradicionales y evaluando distintas variantes de wavelet para distintos tipos de señales.

## Introducción

La transformada wavelet es una herramienta poderosa en el procesamiento de señales debido a su capacidad de representar señales en el dominio tiempo-frecuencia. A diferencia de la transformada de Fourier, que pierde información temporal, la wavelet permite analizar fenómenos transitorios y no estacionarios, típicos en señales biomédicas como ECG, EMG y EEG.

Existen varios tipos de transformadas wavelet, cada una con características y aplicaciones específicas:

### Transformada Wavelet Continua (CWT)
<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/Captura de pantalla 2025-05-17 231538.png">  

La Transformada Wavelet Continua permite analizar señales de forma continua en el dominio del tiempo y la frecuencia, proporcionando una representación detallada de cómo varían las frecuencias a lo largo del tiempo. A diferencia de la DWT, la CWT no realiza decimación, lo que la hace más precisa para el análisis de señales con componentes transitorios o no estacionarios. Esta transformada es útil para estudios exploratorios y visualización detallada de patrones en señales biomédicas o geofísicas, aunque su alto costo computacional puede limitar su uso en aplicaciones en tiempo real.

---

### Transformada Wavelet Discreta (DWT)
<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/Captura de pantalla 2025-05-17 233949.png">  

Es la forma más básica y ampliamente utilizada de transformada wavelet. Permite analizar señales a diferentes escalas y resoluciones, combinando ventajas tanto del dominio del tiempo como del dominio de la frecuencia. A través de un banco de filtros de dos canales, la señal se descompone iterativamente en componentes de baja y alta frecuencia.

La parte de baja frecuencia representa la aproximación de la señal y contiene su estructura general.  
La parte de alta frecuencia captura los detalles de la señal y contiene información sobre los cambios rápidos, bordes o transiciones abruptas.

Su eficiencia computacional y capacidad de análisis multiescala la hacen adecuada para una variedad de señales unidimensionales como ECG, EEG y señales de audio. Sin embargo, presenta limitaciones cuando se aplica a señales multidimensionales como imágenes, debido a su pobre direccionalidad y falta de redundancia.

---

### Transformada Wavelet Estacionaria (SWT)
<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/Captura de pantalla 2025-05-17 231756.png">  

La Transformada Wavelet Estacionaria es una variante no decimada de la DWT que mantiene la longitud original de la señal en cada nivel de descomposición, lo que la hace especialmente adecuada para la reducción de ruido. Al conservar la alineación temporal, permite preservar características importantes como bordes o picos, siendo útil en contextos donde se requiere mantener la estructura temporal de la señal. Se aplica comúnmente junto con técnicas de *thresholding* (como *wavelet shrinkage*) para eliminar ruido sin perder información relevante.

### Filtro a utilizar:  Transformada wavelet estacionaria (SWT)

<p align="justify"> La transformada wavelet estacionaria (SWT) representa una de las mejores opciones para el filtrado de señales biomédicas, como el ECG, en comparación con otros tipos de transformadas wavelet, principalmente por su capacidad de mantener la alineación temporal de la señal original. 

<p align="justify">  A diferencia de la transformada wavelet discreta (DWT), que reduce la resolución temporal a medida que se incrementa el nivel de descomposición mediante un proceso de downsampling, la SWT omite esta etapa y, en cambio, replica los filtros en cada nivel. Esta estructura redundante asegura que no se pierda información temporal, lo que resulta en una reconstrucción más precisa de la señal tras el proceso de filtrado.


---

## Materiales y Equipos

- MATLAB 
- Señales biomédicas de clases anteriores (ECG, EEG, EMG)
- Computadora 

## Metodología

## Señales

### EMG

Reposo

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/EMG1.jpeg" >

Contracción leve

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/EMG2.jpeg" >

Contracción fuerte

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/EMG3.jpeg" >

### ECG

Reposo

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/ECG1.jpeg" >

Inhalando / Manteniendo / Exhalando

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/ECG2.jpeg" >

Después de ejercicio físico

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/ECG3.jpeg" >

### EEG

Reposo

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/EEG1.jpeg" >

Abriendo y cerrando los ojos

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/EEG2.jpeg" >

Leyendo y repitiendo trabalenguas

<img src="/Laboratorios/Laboratorio 8 - Wavelet/imagenes_wavelet/EEG3.jpeg" >

## Resumen y Discusión

El análisis de señales biomédicas mediante transformada wavelet demuestra ser altamente eficiente para la reducción de ruido sin comprometer la integridad de la señal original. La **DWT** resulta una opción atractiva por su bajo costo computacional y buen desempeño frente a ruido, especialmente en señales unidimensionales como ECG y EEG. En estudios revisados, la **SWT** también se destaca en tareas de reducción de ruido preservando los contornos, haciendo uso del método *wavelet shrinkage*.

En comparación con métodos tradicionales como la FFT, las wavelets permiten trabajar directamente en el dominio del tiempo, ofreciendo ventajas significativas en cuanto a localización temporal y tratamiento de transitorios.

## Bibliografía

- González, G. R. A. (s.f.). *Capítulo 3 - Transformada Wavelet*. Disponible en: [https://catarina.udlap.mx/u_dl_a/tales/documentos/mel/gonzalez_g_ra/capitulo3.pdf](https://catarina.udlap.mx/u_dl_a/tales/documentos/mel/gonzalez_g_ra/capitulo3.pdf)
- Juárez, M., & Sánchez, A. (2015). *Filtrado de ruido en una señal de radio de onda corta mediante transformada wavelet discreta*. Tesis IPN. Disponible en: [https://tesis.ipn.mx/bitstream/handle/123456789/21211/TESIS.pdf](https://tesis.ipn.mx/bitstream/handle/123456789/21211/TESIS.pdf)
- IEEE Xplore. *A Review of Wavelet Analysis and Its Applications*. Disponible en: [https://ieeexplore.ieee.org/document/9785993](https://ieeexplore.ieee.org/document/9785993)
- Unser, M., & Aldroubi, A. (1996). *A review of wavelets in biomedical applications*. Proceedings of the IEEE, 84(4), 626–638. doi: [10.1109/5.488704](https://doi.org/10.1109/5.488704)
- Vilimek, D., et al. (2022). *Comparative analysis of wavelet transform filtering systems for noise reduction in ultrasound images*. PLoS One, 17(7), e0270745. doi: [10.1371/journal.pone.0270745](https://doi.org/10.1371/journal.pone.0270745)
