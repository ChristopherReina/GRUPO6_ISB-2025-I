# **LABORATORIO 12: Avance de proyecto**

# Sindrome del túnel carpiano en trabajadores de oficina #

# **Tabla de contenidos**

1. [Introducción](#id0)
2. [Bases de datos](#id1)
3. [Características e investigación](#id2)
4. [Base de datos adicional](#id3)
5. [Proyecciones](#id4)

## **Introducción** <a name="id0"></a>

El síndrome del tunel carpiano es una dolencia provocada por la inflamación y la presión en el interior del túnel formado por el carpo y el ligamento carpiano transverso en la muñeca, donde se encuentran diversos tendones y el nervio mediano. 

## **Bases de datos** <a name="id1"></a>

### Gesture Recognition and Biometrics ElectroMyogram (GRABMyo) v1.1.0 ###

- Electromiografía de superficie.
- Los electrodos se colocaron en forma de anillos alrededor del antebrazo y la muñeca, abarcando: flexores y extensores del antebrazo.
- Rango de edad: 24–35 años.
- Frecuencia de muestreo: 2048 Hz.
- Duración por gesto: 5 segundos por repetición.
- Total de repeticiones por gesto: 7.

Esta fue la base de datos selecionada debido a:

* HD-sEMG (448 canales)
* Datos de antebrazo y muñeca
* Grabacion simultánea de kinomática y fuerza
* Sin filtrar y sin procesar
* Sujetos sanos

### A database of hand kinematics, high-density sEMG of forearm and wrist for motion intent recognition v1.0.0 ###

- Electrodos de superficie de alta densidad (HD-sEMG).Los electrodos se colocaron en forma de anillos alrededor del antebrazo y la muñeca, abarcando: flexores y extensores del antebrazo.
- Rango de edad: 21 a 35 años
- Guante de datos 5DT Data Glove 14 Ultra.
- Frecuencia de muestreo: 200 Hz.

### Complex Upper-Limb Movements v1.0.0 ###

- Sistema de captura de movimiento basado en cámaras (VICON).
- Marcador reflectante en la mano para reconstruir su trayectoria 3D.
- Edad promedio: 26.4 ± 45.2 años
- El enfoque fue en la cinemática (movimiento externo de la mano), no en señales neuromusculares

<image src="/Laboratorios/Laboratorio 10/lab10/11.png">

## **Características e investigación** <a name="id2"></a>

* Coeficientes de aproximación (A):
  
Capturan las tendencias de baja frecuencia, que en EMG representan la señal muscular real (información útil).

* Coeficientes de detalle (D):
 Capturan las frecuencias altas, que muchas veces incluyen el ruido (pero también eventos rápidos de contracción si se analizan correctamente).

* CWT devuelve una matriz de coeficientes:
Filas: escalas (análogas a frecuencias).
Columnas: tiempo.

Escala 16 Mexican Hat → mejor para detectar eventos rápidos.
Escala 32 Symlet 6 → mejor para patrones más lentos o suaves.

* Extraer los coeficientes de una sola escala (16 o 32) que representan bien la actividad muscular que deseas analizar.
  
MAV: Valor absoluto medio →  Nivel de activación muscular
WL: Variación entre muestras sucesivas → Complejidad de la contracción
RMS: Raíz cuadrada media → Energía muscular.
Media y Varianza: Estadísticas básicas → Distribución del patrón muscular
  
## **Base de datos adicional** <a name="id3"></a>

* Se 

## **Proyecciones** <a name="id5"></a>

* Est
