### Tutorial básico de git y github

## 1. Comandos básicos de Git

**git init**: Inicia un repositorio de git del proyecto.
```bash
git init
```
---
**git add**: Se utiliza para añadir archivos al **área de preparación** de git.
```bash
git add pruebita.txt
```
---
**git commit**: Una vez agregados los archivos al **área de preparación** este comando se usa para comprometerso con los cambios en realizados.
```bash
git commit -m "actualización"
```
---
**git push**: Después de comprometerse con los cambios, puede enviarlos al **repositorio remoto** utilizando push.
```bash
git push nombre_del_remoto nombre_de_la_rama
```
---
**git pull**:  Se utiliza para descargar los cambios más recientes del **servidor remoto**.
```bash
git pull nombre_del_remoto nombre_de_la_rama
```
---
**git branch**: Se utiliza para crear, eliminar y listar **ramas** en su proyecto. 
```bash
git branch nombre_de_la_rama
```
---
**git checkout**: Cambia una rama existente.
```bash
git checkout nombre_de_la_rama
```
---
## 2. Uso de markdown para Github

**Encabezados**: Para crear encabezados, se usa el símbolo de numeral `#`. El número de numerales indica el nivel del encabezado.
```markdown
# Encabezado nivel 1
## Encabezado nivel 2
### Encabezado nivel 3
```
---
**Texto en Negrita y Cursiva**: Se puede enfatizar el texto usando asteriscos o guiones bajos.

- **Negrita**: Usa dos asteriscos `**texto**` o guiones bajos `__texto__`. <br>
  **Este es un texto en negrita**
- *Cursiva*: Usa un asterisco `*texto*` o un guion bajo `_texto_`. <br>
  *Este es un texto en cursiva*

---
**Listas**

Usa asteriscos `*` o guiones `-` antes de cada elemento.
```markdown
* Elemento 1
* Elemento 2
  * Sub-elemento
```

Para listas ordenadas se usa números seguidos por un punto.
```markdown
1. Primer elemento
2. Segundo elemento
   1. Sub-elemento
```
---
**Enlaces e Imágenes**

- **Enlaces**: `[texto del enlace](URL)`
- **Imágenes**: `![texto alternativo](URL_de_la_imagen)`


[Enlace a Google](https://www.google.com)

![Logo de GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)


---
**Bloques de Código**

Para incluir bloques de código, usa tres acentos invertidos ```` ``` ````.

```markdown
def hola_mundo():
    print("¡Hola, mundo!")
```
---
## 3. Creación de repositorio en Github

Ir a la parte derecha de la web donde aparecerá la opción de “New Repository”
imagen 1
Seguidamente aparecerá lo siguiente, aquí se recomienda llenar todos los campos como 
nombre del repositorio, descripción, establecerlo modopúblico y adicionar un Readme file.
Luego ya se tendrá un repositorio listo para ser modificado en
contenido.
imagen2
Finalmente habremos creado nuestro repositorio
imagen3

