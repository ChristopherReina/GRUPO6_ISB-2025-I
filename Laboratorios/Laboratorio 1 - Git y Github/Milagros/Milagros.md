## Métodos para Crear Repositorios

Existen dos maneras principales de crear un repositorio en GitHub:

### 1. Mediante la Línea de Comandos (CLI) - Ideal para Empresas

Este método es más eficiente para proyectos grandes y empresas porque permite automatizar tareas y manejar grandes volúmenes de código, además de que varios desarrolladores pueden trabajar y editar a la vez con el **Flujo de trabajo que ofrece Git**.

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

## Flujo de Trabajo en Git

El flujo de trabajo en Git se basa en diferentes áreas:

| **Área**            | **Acción**               | **Comando**            |
|---------------------|-------------------------|------------------------|
| **Working Directory** | Modificación de archivos | Edición normal        |
| **Staging Area**    | Añadir archivos          | `git add <archivo>`   |
| **Local Repository**| Confirmar cambios       | `git commit -m "Mensaje"` |
| **Remote Repository** | Subir cambios          | `git push`             |


### Explicación de los Comandos 

- **`git add <archivo>`**: Mueve archivos del **Working Directory** al **Staging Area**.
- **`git commit -m "mensaje"`**: Mueve archivos del **Staging Area** al **Local Repository**.
- **`git push origin main`**: Envía los cambios del **Local Repository** al **Remote Repository**.
- **`git pull origin main`**: Trae los cambios más recientes del repositorio remoto al local.
- **`git checkout <rama>`**: Cambia de rama o revierte cambios en archivos específicos.

### Flujo de Trabajo Representado

```plaintext
Working Directory → (git add) → Staging Area → (git commit) → Local Repo → (git push) → Remote Repo
Remote Repo → (git pull) → Local Repo
Local Repo → (git checkout) → Working Directory
```

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

### 2. Mediante la Interfaz Gráfica (GUI) - Ideal para Proyectos Pequeños

Si el proyecto no requiere una gestión avanzada y también si no se tiene mucha experiencia o dominio de Git, GitHub es una manera más sencilla ya que se trabaja mediante su interfaz gráfica, donde se pueden ver y buscar los iconos para el trabajo con mayor comodidad:

#### Pasos:
1. Iniciar sesión en [GitHub](https://github.com/).
2. Hacer clic en **New Repository**.
   ![Crear un nuevo repositorio] (<image src="/Laboratorios/Laboratorio 1 - Git y Github/Milagros/New_repository.jpeg" >) 
4. Completar los detalles del repositorio (nombre, descripción, visibilidad).
5. Elegir si incluir un archivo README y una licencia.
6. Hacer clic en **Create Repository**.
7. Copiar el enlace del repositorio y clonar si se desea trabajar en local:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```

---


