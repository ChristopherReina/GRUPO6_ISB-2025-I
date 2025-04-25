# **LABORATORIO 4: – USO DE BITalino PARA ECG**

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados](#id4)\
     4.1 [Conexión usada](#id5)\
     4.2 [Video de la señal](#id6)\
     4.3 [Archivos](#id8)\
     4.4 [Ploteo de la señal en Python](#id9)
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

### **Video de la señal** <a name="id6"></a>
#
1. **Estado basal**: El sujeto de prueba se quedó quieto y manteniendo la calma
2. **Manteniendo la respiración por 10 segundos**: El sujeto de prueba mantuvo la respiración por 10 segundos y se midió la inspiración y expiración
3. **Reposo basal**: Reposo después de mantener la respiración
4. **Después de una actividad física**:El sujeto de prueba realizó movimientos aeróbicos por 5 minutos
   
     
|                 **Modelo**                 | **Video** |
|:------------------------------------------:|:---------:|
|                **Estado Basal**                |<video src=""></video>|
| **Manteniendo la respiración por 10 segundos** |<video src=""></video>|
|                **Reposo basal**                |<video src=""></video>|
|       **Después de la actividad física**       |<video src=""></video>|

     
### **Archivos** <a name="id8"></a>
#

     
### **Ploteo de la señal en Python** <a name="id9"></a>
<p align="justify"> P

     a)   Estado basal</p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
[Agregar comentario]</p>
     b)   Manteniendo la respiración por 10 segundos</p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
[Agregar comentario]</p>
     c)   Reposo basal</p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
[Agregar comentario]</p>
     d)   Después de una actividad física</p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
<p align="center"><img src="[direccion]" width="600" height="300"></p>
[Agregar comentario]</p>

</div>
     
## **Conclusiones** <a name="id10"></a>
* P

* P

* P

* P

---
## **Referencias** <a name="id11"></a>
---
[1] “Electrocardiograma”, Medlineplus.gov. [En línea]. Disponible en: https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/. </p>
[2] T. Cascino y M. J. Shea, “Electrocardiografía”, Manual MSD versión para profesionales, 01-dic-2023. [En línea]. Disponible en: https://www.msdmanuals.com/es/professional/trastornos-cardiovasculares/pruebas-y-procedimientos-cardiovasculares/electrocardiograf%C3%ADa. </p>
