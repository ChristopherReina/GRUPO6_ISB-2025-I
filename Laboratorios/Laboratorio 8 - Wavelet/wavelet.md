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

- **Transformada Wavelet Continua (CWT):** permite un análisis continuo en el tiempo, útil para exploración detallada.
- **Transformada Wavelet Discreta (DWT):** ideal para procesamiento digital eficiente. Permite separar la señal en componentes de alta y baja frecuencia.
- **Transformada Wavelet Estacionaria (SWT):** evita la decimación, manteniendo los valores en el tiempo, siendo especialmente útil para la reducción de ruido sin perder características de borde.

## Materiales y Equipos

- MATLAB 
- Señales biomédicas de clases anteriores (ECG, EEG, EMG)
- Computadora 

## Metodología

## Señales

### EMG

Reposo


Contracción leve


Contracción fuerte


### ECG

Reposo


Inhalando / Manteniendo / Exhalando


Después de ejercicio físico

### EEG

Reposo


Abriendo y cerrando los ojos


Leyendo y repitiendo trabalenguas


## Resumen y Discusión

El análisis de señales biomédicas mediante transformada wavelet demuestra ser altamente eficiente para la reducción de ruido sin comprometer la integridad de la señal original. La **DWT** resulta una opción atractiva por su bajo costo computacional y buen desempeño frente a ruido, especialmente en señales unidimensionales como ECG y EEG. En estudios revisados, la **SWT** también se destaca en tareas de reducción de ruido preservando los contornos, haciendo uso del método *wavelet shrinkage*.

En comparación con métodos tradicionales como la FFT, las wavelets permiten trabajar directamente en el dominio del tiempo, ofreciendo ventajas significativas en cuanto a localización temporal y tratamiento de transitorios.

## Bibliografía

- González, G. R. A. (s.f.). *Capítulo 3 - Transformada Wavelet*. Disponible en: [https://catarina.udlap.mx/u_dl_a/tales/documentos/mel/gonzalez_g_ra/capitulo3.pdf](https://catarina.udlap.mx/u_dl_a/tales/documentos/mel/gonzalez_g_ra/capitulo3.pdf)
- Juárez, M., & Sánchez, A. (2015). *Filtrado de ruido en una señal de radio de onda corta mediante transformada wavelet discreta*. Tesis IPN. Disponible en: [https://tesis.ipn.mx/bitstream/handle/123456789/21211/TESIS.pdf](https://tesis.ipn.mx/bitstream/handle/123456789/21211/TESIS.pdf)
- IEEE Xplore. *A Review of Wavelet Analysis and Its Applications*. Disponible en: [https://ieeexplore.ieee.org/document/9785993](https://ieeexplore.ieee.org/document/9785993)
- Unser, M., & Aldroubi, A. (1996). *A review of wavelets in biomedical applications*. Proceedings of the IEEE, 84(4), 626–638. doi: [10.1109/5.488704](https://doi.org/10.1109/5.488704)
- Vilimek, D., et al. (2022). *Comparative analysis of wavelet transform filtering systems for noise reduction in ultrasound images*. PLoS One, 17(7), e0270745. doi: [10.1371/journal.pone.0270745](https://doi.org/10.1371/journal.pone.0270745)
