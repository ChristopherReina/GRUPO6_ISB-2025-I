## Métodos para Crear Repositorios

Existen dos maneras principales de crear un repositorio en GitHub:

### 1. Mediante la Línea de Comandos (CLI) - Ideal para Empresas

Este método es más eficiente para proyectos grandes y empresas porque permite automatizar tareas y manejar grandes volúmenes de código.

#### Pasos:
1. **Inicializar un repositorio en local:**
   ```bash
   git init
   ```
2. **Configurar el repositorio remoto:**
   ```bash
   git remote add origin https://github.com/usuario/repositorio.git
   ```
3. **Agregar archivos al área de staging:**
   ```bash
   git add .
   ```
4. **Confirmar los cambios en el repositorio local:**
   ```bash
   git commit -m "Primer commit"
   ```
5. **Subir los cambios al repositorio remoto:**
   ```bash
   git push -u origin main
   ```

### 2. Mediante la Interfaz Gráfica (GUI) - Ideal para Proyectos Pequeños

Si el proyecto no requiere una gestión avanzada, GitHub ofrece una manera sencilla mediante su interfaz gráfica:

#### Pasos:
1. Iniciar sesión en [GitHub](https://github.com/).
2. Hacer clic en **New Repository**.
3. Completar los detalles del repositorio (nombre, descripción, visibilidad).
4. Elegir si incluir un archivo README y una licencia.
5. Hacer clic en **Create Repository**.
6. Copiar el enlace del repositorio y clonar si se desea trabajar en local:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```

---

## Flujo de Trabajo en Git

En Git, los archivos pasan por varias etapas antes de ser enviados al repositorio remoto:

| Estado             | Descripción                                            | Comando para Mover |
|--------------------|----------------------------------------------------|----------------------|
| **Working Directory** | Donde se crean y editan los archivos.            | `git add <archivo>`  |
| **Staging Area**   | Área temporal antes de confirmar los cambios.      | `git commit -m "mensaje"` |
| **Local Repository** | Confirmación en el repositorio local.             | `git push origin main` |
| **Remote Repository** | Los cambios se suben a GitHub.                   | `git pull origin main` |

---

## Comandos Claves

- **Ver el estado de los archivos:**
  ```bash
  git status
  ```
- **Descartar cambios en un archivo:**
  ```bash
  git checkout -- <archivo>
  ```
- **Revertir un commit:**
  ```bash
  git reset --soft HEAD~1
  ```

---

## Tips Importantes

1. **Usar `.gitignore`** para evitar subir archivos innecesarios.
2. **Mantener commits pequeños y descriptivos**.
3. **Trabajar con ramas** para evitar conflictos en el código.
   ```bash
   git checkout -b nueva-rama
   ```
4. **Hacer `pull` antes de `push`** para evitar conflictos.
   ```bash
   git pull origin main
   ```
