# **LABORATORIO 12: Avance de proyecto**

# Sindrome del túnel carpiano en trabajadores de oficina #

# **Tabla de contenidos**

1. [Introducción](#id0)
2. [Bases de datos](#id1)
3. [Características e investigación](#id2)
4. [Base de datos adicional](#id3)
5. [Avances y siguientes pasos](#id4)

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

### Dataset on Bilateral Idiopathic Carpal Tunnel Syndrome: Crossover Study of Two Combined Physiotherapeutic Treatment Methods on Chirurgical and Clinical Patients ###

Estos datos describen un ensayo cruzado controlado aleatorio de 73 participantes con síndrome del túnel carpiano bilateral idiopático (STC) que se sometieron a dos métodos de tratamiento fisioterapéutico combinados: movilización miofascial (IASTM) y estiramiento; en condiciones quirúrgicas y clínicas. 

Utilizaremos esta base de datos para tener data de pacientes con la enfermedad. 

## ** Avances y siguientes pasos** <a name="id5"></a>

El código con los avances se encuentra en la carpeta "Laboratorio 12- Proyecto Avance".

Se hizo el cambio a visual studio code para usar las caracteristicas de una mejor computadora a las que presta el servicio de google colab, para agilizar el procesamiento de los cientos de archivos de las dos bases de datos utilizadas. 

* PCA 

El siguiente gráfico PCA, se muestra la distribución de gestos musculares capturados por las señales EMG tras aplicar reducción de dimensiones con PCA a características estadísticas como media, RMS y entropía. Cada punto representa un canal EMG, coloreado según el gesto realizado.

<image src="/Laboratorios/Laboratorio 12 - Proyecto Avance/1.png">

* ROC

Curva ROC tras entrenar un clasificador Random Forest sobre señales EMG etiquetadas como “sano”.

<image src="/Laboratorios/Laboratorio 12 - Proyecto Avance/2.png">

* PCA según gesto

Gráfico de dispersión 2D que muestra la distribución de gestos musculares a partir de señales EMG, utilizando reducción de dimensiones con PCA.
<image src="/Laboratorios/Laboratorio 12-Proyecto Avance/3.png">

* Siguientes pasos

- Comparar la data de personas sanas vs personas con síndrome del tunel carpiano.
- Utilizar la data para clasificar entre personas sanas y personas con STC. 
