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


