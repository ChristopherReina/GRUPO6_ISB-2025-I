

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
     5.4 [Analisis cuantitativo](#id10)
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
|                **Estado Basal 1**                |<video src="[dirección]"></video>|
|                **Estado Basal 2**                |<video src="[dirección]"></video>|
| **Realizando una tarea cognitiva**         |<video src="[dirección]"></video>|
|                **Parpadeando y masticando cada 2 segundos**                |<video src="[dirección]"></video>|
|       **Leyendo trabalenguas**         |<video src="[dirección]"></video>|


     
### **Ploteo de la señal en Python** <a name="id9"></a>

a)   Estado basal 1: Ojos abiertos con punto fijo</p>
<p align="center"><img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/Captura de pantalla 2025-05-03 210916.png" width="800" height="300"></p>    
<p align="justify"> [agregar comentario]</p>

b)   Estado basal 2: Ojos cerrados </p>
<p align="center"><img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/Captura de pantalla 2025-05-03 213637.png" width="800" height="300"></p>    
<p align="justify"> [agregar comentario]</p>

c)   Realizando una tarea cognitiva</p>
<p align="center"><img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/Captura de pantalla 2025-05-03 211626.png" width="800" height="300"></p>  #D1 (2 mediciones)
<p align="justify"> A partir de una inspección visual de la señal, es posible estimar que hay entre 10 y 20 ciclos por segundo, lo cual corresponde a frecuencias entre 10 a 20 Hz. Estas frecuencias indican la presencia de ondas Alfa (8–13 Hz) o Beta (13–30 Hz). Dado que la medición se realizó durante una tarea cognitiva activa, es más probable que predominen las ondas Beta. </p>
<p align="justify"> La literatura neurofisiológica indica que las ondas Beta están asociadas con estados de alerta, procesamiento mental activo y resolución de problemas. En contraste, las ondas Alfa suelen estar más relacionadas con estados de relajación o de inactividad mental, y tienden a disminuir durante tareas cognitivas exigentes.</p>
<p align="justify"> En base en la frecuencia visual estimada y el contexto de la actividad realizada, se puede afirmar que esta señal EEG corresponde a ondas Beta, lo cual es coherente con el estado de activación cognitiva que se espera durante una tarea de este tipo. </p>


c)   Artefactos: Parpadeando y masticando cada 2 segundos</p>
<p align="center"><img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/Captura de pantalla 2025-05-03 211646.png" width="800" height="300"></p>  #D1 (2 mediciones), inhalacion 5sec, exhalacion 5sec
<p align="justify">Se observan fluctuaciones más abruptas e irregulares, con picos que no siguen un patrón fisiológico típico. Las caídas bruscas o transiciones casi verticales, como las que se ven aquí, suelen estar asociadas a artefactos musculares, movimientos oculares, parpadeos o incluso interferencia eléctrica. Esta señal refleja una actividad dominada por artefactos, con características no fisiológicas como transiciones abruptas y ruido inconsistente. </p>

d)   Actividad libre: Leyendo trabalenguas</p>
<p align="center"><img src="/Laboratorios/Laboratorio 6 - Adquisición de señal EEG/Fotos/Captura de pantalla 2025-05-03 211702.png" width="800" height="300"></p>
<p align="justify">  Drante tareas lingüísticas complejas como la lectura (y más aún con trabalenguas, que requieren mayor esfuerzo articulatorio y atención fonológica), se incrementa la actividad en las bandas beta alta (18–30 Hz) e incluso gamma (>30 Hz). Estas bandas están asociadas con el procesamiento cognitivo activo, la planificación motora del habla, la atención sostenida y la integración sensorial-motora. La señal durante la lectura de trabalenguas refleja una mayor actividad cerebral respecto al estado basal con ojos abiertos. Esto es coherente con el incremento de oscilaciones rápidas y la posible aparición de componentes gamma, lo que concuerda con lo reportado en la literatura [3] </p>


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
[3] https://oa.upm.es/44379/1/TFM_LEONARDO_JOSE_GOMEZ_FIGUEROA.pdf

