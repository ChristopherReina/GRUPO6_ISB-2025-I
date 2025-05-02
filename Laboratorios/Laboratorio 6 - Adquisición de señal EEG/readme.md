

# **LABORATORIO 6: – USO DE BITalino PARA EEG**

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados](#id4)\
     5.1 [Conexión usada](#id5)\
     5.2 [Video de la señal](#id6)\
     5.3 [Archivos](#id8)\
     5.4 [Ploteo de la señal en Python](#id9)\
     5.5 [Análisis cuantitativo (PSD)].(#id10).
7. [Conclusiones](#id11)
8. [Referencias](#id12)

## **Introducción al laboratorio** <a name="id0"></a>
---
<p align="justify"> El electroencefalograma (EEG) es una herramienta esencial que estudia la actividad eléctrica cerebral.[1] 
Se utiliza principalmente para:

* Clasificar el tipo de convulsión y localizar el inicio de las convulsiones
* Prueba de amobarbital sódico o Wada para determinar el predominio hemisférico para el lenguaje y la memoria
* Manejo del estado epiléptico e inducción del coma terapéutico
* Pacientes con estado mental alterado por diversas etiologías como encefalopatías metabólicas tóxicas
* Pacientes encefalopáticos con etiologías inexplicables para evaluar el grado de encefalopatía
* Síncope o síntomas de pérdida de conciencia con evaluación cardíaca negativa
* Pacientes comatosos en la unidad de cuidados intensivos con confusión deteriorada o persistente o disminución de la capacidad de respuesta
* Pronóstico después de un paro cardíaco
* Identificar cambios isquémicos retardados después de una hemorragia subaracnoidea e intracraneal
* Procedimientos anestésicos para monitorear la profundidad de la anestesia
* Determinación de muerte cerebral 

<img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/FOTO4.png" >
Bandas de frecuencia de EEG, ocurrencia y tareas para activar la potencia de la banda. [2]

<p align=> 
     

### Electroencefalograma (EEG)

<p align="justify"> Las principales áreas son frontopolar (Fp), frontal (F), central (C), temporal (T), parietal (P) y occipital (O). En cuanto a su ubicación lateralizada, los números impares (1, 3, 5, 7) se refieren a los electrodos colocados en el hemisferio izquierdo, mientras que los números pares (2, 4, 6, 8) se refieren a los del hemisferio derecho.

<img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/FOTO1.png" >
<img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/FOTO2.png" >


---
## **Objetivos** <a name="id1"></a>

* Adquirir la señal EEG de un miembro del equipo al exponerse a distintos estímulos.
* Realizar una correcta configuración de BiTalino.
* Plotear la información de las señales EEG en software OpenSignals (r)evolution.
* Analizar las señales obtenidas.

<div align=>

## **Materiales y equipos** <a name="id2"></a>
---

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|    Samsung Galaxy A55    |      Celular     |       1      |
|   3M RedDot    |     Electrodos desechables autoadhesivos gelificados      |       2      |

</div>

## **Procedimiento** <a name="id3"></a>

1. Limpieza de las zonas en las que se colocarán los electrodos. 
2. Se colocaron los electrodos en las regiones de interés y posteriormente se conectaron los cables. Para este caso:
     * Fp1 conectado al electrodo 1
     * Fp2 conectado a GND
     * Referencia (mastoide) conectado al electrodo 2

3. Se registraron los datos en formato .txt y video en los siguientes estados:
     * Estado basal con ojos abiertos y cerrados.
     * Realizando una tarea cognitiva.
     * Parpadeando y masticando cada 2 segundos.
     * Leyendo trabalenguas.
       

### **Conexión usada** <a name="id5"></a>
#
Para la posición de los electrodos se utilizo el documento "BITalino (r)evolution Lab Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS" La configuración es la que se muestra en la siguiente imagen: 
  
<img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/FOTO3.png" >

</div>

### **Sujeto de prueba 01**
---

### **Videos de las señales** <a name="id6"></a>
#
1. **Estado basal**: El sujeto de prueba tuvo los ojos abiertos (un minuto) y cerrados (un minuto) en distintos tiempos.
2. **Realizando una tarea cognitiva**: El sujeto de prueba resto de siete (07) en siete (07) desde cien (100) durante dos (02) minutos.  
3. **Parpadeando y masticando cada 2 segundos**: El sujeto de prueba parpadeo cada dos (02) segundos y mastico durante dos minutos.
4. **Leyendo trabalenguas**:El sujeto de prueba leyo distintos trabalenguas durante seis (06) minutos.
   
     
|                 **Modelo**                 | **Video** |
|:------------------------------------------:|:---------:|
|                **Estado Basal**                |<video src="[dirección]"></video>|
| **Realizando una tarea cognitiva**         |<video src="[dirección]"></video>|
|                **Parpadeando y masticando cada 2 segundos**                |<video src="[dirección]"></video>|
|       **Leyendo trabalenguas**         |<video src="[dirección]"></video>|


     
### **Ploteo de la señal en Python** <a name="id9"></a>
<p align="justify"> [agregar comentario]

a)   Estado basal</p>
<p align="center"><img src="[dirección]" width="800" height="300"></p>    
<p align="justify"> [agregar comentario]</p>

     b)   Realizando una tarea cognitiva</p>
<p align="center"><img src="[dirección]" width="800" height="300"></p>  #D1 (2 mediciones)
<p align="justify"> [agregar comentario]</p>

     c)   Parpadeando y masticando cada 2 segundos</p>
<p align="center"><img src="[dirección]" width="800" height="300"></p>  #D1 (2 mediciones), inhalacion 5sec, exhalacion 5sec
<p align="justify"> [agregar comentario]</p>

     d)   Leyendo trabalenguas</p>
<p align="center"><img src="[dirección]" width="800" height="200"></p>
<p align="justify"> [agregar comentario]</p>


</div>

---
## **Análisis cuantitativo (PSD)** <a name="id10"></a>
     
[agregar comentario]</p>

## **Conclusiones** <a name="id11"></a>
* L
  
* U

* E
  
* L
---
## **Referencias** <a name="id12"></a>
---
[1] A. Rayi y N. I. Murr, “Electroencephalogram”, en StatPearls, Treasure Island (FL): StatPearls Publishing, 2025. </p>
[2] EXPERIMENTAL GUIDES TO MEET y L. Y. Biosignals, “BITalino (r)evolution Lab Guide”, Pluxbiosignals.com. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf. [Consultado: 02-may-2025].

