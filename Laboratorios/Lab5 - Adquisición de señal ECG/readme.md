

# **LABORATORIO 5: – USO DE BITalino PARA ECG**

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados](#id4)\
     5.1 [Conexión usada](#id5)\
     5.2 [Video de la señal](#id6)\
     5.3 [Archivos](#id8)\
     5.4 [Ploteo de la señal en Python](#id9)
6. [Conclusiones](#id10)
7. [Referencias](#id11)

## **Introducción al laboratorio** <a name="id0"></a>
---
<p align="justify"> Un electrocardiograma (o electrocardiografía) es una prueba rápida en la que se revisan los latidos cardíacos y se registran las señales eléctricas del corazón. Muestra cuán rápido o cuán lento late el corazón.[1] Los resultados de un electrocardiograma pueden ayudar a diagnosticar:

* Arritmia
* Cardiomiopatía
* Enfermedad de las arterias coronarias
* Ataque cardiaco
* Insuficiencia cardiaca
* Enfermedades de las válvulas del corazón
* Defectos cardiacos congénitos

<p align=> 
     
### Señal ECG

<img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/SEÑALECG.png" >

|  **Segmento**  | **Descripción** |
|:------------:|:---------------:|
| Onda P |  La onda P representa la despolarización auricular.  |  
| Intervalo PR |  El intervalo PR es el período entre el comienzo de la despolarización auricular y la despolarización ventricular.  |  
| Complejo QRS |    Representa la despolarización ventricular.    | 
| Intervalo QT |  Período entre el comienzo de la despolarización ventricular y el final de la repolarización ventricular.   |       
| Segmento ST |    Representa la despolarización completa del miocardio ventricular.   |       
| Onda T |    Refleja la repolarización ventricular.    |       
| Onda U |   Refleja la repolarización tardía de las fibras de Purkinje y ciertos miocitos ventriculares. |     


### Electrocardiograma

<p align="justify"> La electrocardiografía convencional ofrece 12 imágenes (derivaciones) diferentes de la actividad eléctrica del corazón, representadas a partir de las diferencias de potencial eléctrico entre electrodos positivos y negativos colocados en los miembros y la pared torácica. Seis de estas derivaciones son verticales (emplean las derivaciones frontales I, II y III y las derivaciones de los miembros aVR, aVL y aVF) y 6 son horizontales (emplean las derivaciones precordiales V1, V2, V3, V4, V5 y V6). [2]

---
## **Objetivos** <a name="id1"></a>

* Adquirir al menos una derivación de ECG.
* Realizar una correcta configuración de BiTalino.
* Plotear la información de las señales ECG en software OpenSignals (r)evolution.
* Analizar las ondas obtenidas.

<div align=>

## **Materiales y equipos** <a name="id2"></a>
---

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|    Samsung Galaxy A55    |      Celular     |       1      |
|   3M RedDot    |     Electrodos desechables autoadhesivos gelificados      |       3      |

</div>

## **Procedimiento** <a name="id3"></a>

1. Limpieza de las zonas en las que se colocarán los electrodos. 
2. Se colocaron los electrodos en las regiones de interés y posteriormente se conectaron los cables. Para este caso:
     * Positivo en muñeca izquierda
     * Negativo en mmuñeca derecha
     * Referencia en cresta ilíaca

3. Se registraron los datos en formato .txt y video en los siguientes estados:
     * Estado basal.
     * Ciclos de respiración (Inhalación, retención y exhalación).
     * Antes, durante y después de ejercicios intensos.
       

### **Conexión usada** <a name="id5"></a>
#
Para la posición de los electrodos se utilizo el documento "BITalino (r)evolution Lab Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS" La configuración es la que se muestra en la siguiente imagen: 
  
<img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/CONFIGURACIONFISICA.png" >

</div>

### **Sujeto de prueba 01**
---

### **Videos de las señales** <a name="id6"></a>
#
1. **Estado basal**: El sujeto de prueba se quedó quieto y manteniendo la calma.
2. **Manteniendo la respiración por 10 segundos**: El sujeto de prueba mantuvo la respiración por 10 segundos y se midió la inspiración y expiración.
3. **Reposo basal**: Reposo después de mantener la respiración.
4. **Después de una actividad física**:El sujeto de prueba realizó actividad física hasta agotarse.
   
     
|                 **Modelo**                 | **Video** |
|:------------------------------------------:|:---------:|
|                **Estado Basal**                |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D1_videos/Basal_D1.mp4"></video>|
| **Manteniendo la respiración por 10 segundos** |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D1_videos/Respiracion10_D1.mp4"></video>|
|                **Reposo basal**                |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D1_videos/Respiracion5_D1.mp4"></video>|
|       **Después de la actividad física**       |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D1_videos/despues_ejercicio_D1.mp4"></video>|


     
### **Ploteo de la señal en Python** <a name="id9"></a>
<p align="justify"> Se observan los cambios en las ondas de la señal ECG, dependiendo de la derivación utilizada. 

a)   Estado basal</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Basal_D1.png" width="800" height="300"></p>    
<p align="justify"> El sujeto se encontraba sentado, no realizaba actividad. Las ondas P, el complejo QRS y las ondas T son claramente visibles. En la Derivación I, la onda T es comúnmente positiva, indicando que la repolarización sigue la misma dirección que la despolarización.</p>
     b)   Manteniendo la respiración por 10 segundos</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Resp10_D1.png" width="800" height="300"></p>  #D1 (2 mediciones)
<p align="justify"> En esta situación, el sujeto realizaba una inhalación máxima, mantenía la respiración por 10 segundos, y luego exhalaba lentamente. Al comenzar la inhalación, se observa un aumento de la frecuencia cardíaca, evidenciado por una disminución en el intervalo RR (el tiempo entre dos complejos QRS consecutivos). Durante la fase donde mantiene la respiración, el trazado del ECG muestra una tendencia a la estabilización, con intervalos RR más regulares y una frecuencia cardíaca que se mantiene relativamente constante. Al iniciar la exhalación, se aprecia un ligero aumento en el intervalo RR (indicando una reducción de la frecuencia cardíaca), como consecuencia de la disminución del retorno venoso y la normalización de la presión intratorácica.</p>
     c)   Reposo basal</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Resp5_D1.png" width="800" height="300"></p>  #D1 (2 mediciones), inhalacion 5sec, exhalacion 5sec
<p align="justify"> Se realizó la medición cuando el sujero realizaba una inhalación y exhalación durante 5 segundos cada uno. Durante la exhalación de 5 segundos,  los intervalos R-R tienden a hacerse más largos, durante la inhalación de 5 segundos, los intervalos R-R tienden a acortarse. Se observa la respuesta cardíaca a la respiración típica de una persona, mostrando la arritmia sinusal respiratoria fisiológica.</p>
     d)   Después de actividad física rigurosa</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Ejercicio_D1.png" width="800" height="200"></p>
<p align="justify"> La señal de ECG muestra un aumento notable en la frecuencia cardíaca, evidenciado por una reducción en los intervalos RR, con complejos QRS que aparecen con mayor frecuencia. Se observa una ligera variabilidad en la distancia entre latidos, propia del proceso de recuperación tras el esfuerzo</p>

</div>

### **Sujeto de prueba 02**
---
### **Videos de las señales** <a name="id6"></a>
#
1. **Estado basal**: El sujeto de prueba se quedó quieto y manteniendo la calma.
2. **Manteniendo la respiración por 10 segundos**: El sujeto de prueba mantuvo la respiración por 10 segundos y se midió la inspiración y expiración.
3. **Reposo basal**: Reposo después de mantener la respiración.
4. **Después de una actividad física**:El sujeto de prueba realizó actividad física hasta agotarse.
   
     
|                 **Modelo**                 | **Video** |
|:------------------------------------------:|:---------:|
|                **Estado Basal**                |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D2_videos/Basal_D2.mp4"></video>|
| **Manteniendo la respiración por 10 segundos** |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D2_videos/Respiracion10_D2.mp4"></video>|
|                **Reposo basal**                |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D2_videos/Respiracion5_D2.mp4"></video>|
|       **Después de la actividad física**       |<video src="/Laboratorios/Lab5 - Adquisición de señal ECG/D2_videos/despues_ejercicio_D2.mp4"></video>|

     
### **Ploteo de la señal en Python** <a name="id9"></a>
<p align="justify"> De la misma forma, se realizan los ploteos para observar cómo varian las señales ante el cambio de derivación (en sujeto 2 se realizó la toma de la derivación II y III) y actividad durante la toma de datos.

a)   Estado basal</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Basal_D2.png" width="800" height="300"></p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Basal_D3.png" width="800" height="300"></p>
<p align="justify"> Durante el estado de reposo basal en las derivaciones II y III, se observa un trazado de ECG estable, con complejos QRS bien definidos, indicando una frecuencia cardíaca normal y rítmica. En la derivación II, la señal presenta una amplitud moderada, mientras que en la derivación III los complejos QRS son de mayor amplitud y la señal es más limpia, mostrando menos variabilidad entre latidos. En ambos casos, el análisis en el dominio de la frecuencia (FFT) revela un pico notable en los 60 Hz, correspondiente a la contaminación típica de la red eléctrica, además de un contenido de energía más concentrado entre 10 y 30 Hz, lo que coincide con la actividad eléctrica cardíaca normal.</p>
     b)   Manteniendo la respiración por 10 segundos</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Resp10_D2.png" width="800" height="300"></p>
<p align="justify"> En la derivación II se observan complejos QRS rítmicos y bien definidos. Al analizar las señales, no se aprecia un aumento significativo de la frecuencia, lo que sugiere que la maniobra de apnea breve provoca una regulación del sistema nervioso autónomo que estabiliza el ritmo cardíaco. </p>
     c)   Reposo basal</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Resp5_D2.png" width="600" height="300"></p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Resp5_D3.png" width="600" height="300"></p>
<p align="justify"> Se observa en la señal una serie de complejos QRS regulares y bien definidos, sin cambios abruptos en la amplitud o la forma de las ondas, lo cual indica que la respiración lenta y profunda no altera significativamente la conducción eléctrica cardíaca. </p>
     d)   Después de una actividad física</p>
<p align="center"><img src="/Laboratorios/Lab5 - Adquisición de señal ECG/Fotos/Ejercicio_D2.png" width="600" height="200"></p>
<p align="justify"> Justo después del ejercicio, la variabilidad del ritmo puede aumentar de nuevo, pero el ritmo se mantiene relativamente alto hasta que el cuerpo comienza a volver a la frecuencia cardíaca en reposo. La onda T, durante esta fase post-ejercicio, podría ser más aguda o indicar un cambio en la repolarización debido a la fatiga muscular.</p>

</div>
     
## **Conclusiones** <a name="id10"></a>
* Las diversas derivaciones (I, II y III) ofrecen perspectivas complementarias sobre la actividad cardíaca. Cada derivación captura el comportamiento eléctrico del corazón desde ángulos diferentes, lo que ayuda a garantizar un análisis completo
  
* Un factor crucial en la obtención de la señal del electrocardiograma (ECG) es el tipo de electrodos que se emplean. Estos electrodos son el medio a través del cual se capturan los impulsos eléctricos del corazón, por lo que es fundamental que estén posicionados correctamente y sean adecuados para este procedimiento.

* El análisis de datos del ECG  puede verse afectado por el ruido generado de dispositivos electrónicos y otros factores ambientales que se encuentren en el laboratorio. Este ruido puede interferir con la calidad de la señal, produciendo resultados imprecisos o erróneos. Es por ello que se utilizan filtros para procesar la señal.
  
* Los intervalos RR  dependen de varios factores relacionados con la fisiología y la respuesta del corazón a diferentes estímulos. Durante los ciclos de respiración, los intervalos RR se acortan en la inhalación y se alargan en la exhalación, mostrando la arritmia sinusal respiratoria. En la actividad física rigurosa, estos intervalos se reducen significativamente, reflejando la demanda metabólica incrementada, y luego fluctúan durante la recuperación antes de volver a la normalidad. En reposo, los intervalos RR son más constantes, demostrando un ritmo cardíaco regular y un sistema de conducción eléctrica eficiente.
---
## **Referencias** <a name="id11"></a>
---
[1] “Electrocardiograma”, Medlineplus.gov. [En línea]. Disponible en: https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/. </p>
[2] T. Cascino y M. J. Shea, “Electrocardiografía”, Manual MSD versión para profesionales, 01-dic-2023. [En línea]. Disponible en: https://www.msdmanuals.com/es/professional/trastornos-cardiovasculares/pruebas-y-procedimientos-cardiovasculares/electrocardiograf%C3%ADa. </p>
