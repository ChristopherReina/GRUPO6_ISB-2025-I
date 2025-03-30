# Creación de repositorio en github

1. Una vez creada la cuenta en Github, busque en la parte derecha de la web la opción de “New Repository”
   <image src="/Laboratorios/Laboratorio 1 - Git y Github/Valeria/photos/git1.png" >
   
3. Podremos configurar los datos del nuevo repositorio. Se pueden personalizar los datos del repositorio:<br>
   **Configuración del Nuevo Repositorio**<br>
    - **Nombre del repositorio:** Nombre claro y descriptivo para el proyecto.
    - **Descripción:** Breve explicación sobre el propósito o contenido del repositorio.
    - **Visibilidad:** Elige si el repositorio será público o privado.
    - **Archivo README:** Incluye un archivo README para proporcionar una introducción detallada, instrucciones de uso o cualquier información relevante sobre el contenido del repositorio.
   <image src="/Laboratorios/Laboratorio 1 - Git y Github/Valeria/photos/git2.png" > 
4. Una vez creado el repositorio, se pueden agregar archivos de dos maneras:<br>
   **Método 1: Directamente desde Github**<br>
   - En la página principal del repositorio, haz clic en el botón Add file y selecciona Upload files (Subir archivos).
     <image src="/Laboratorios/Laboratorio 1 - Git y Github/Valeria/photos/git3.png" >
   - Arrastra y suelta los archivos que deseas subir
     o haz clic en choose your files (seleccionar archivos) para buscarlos en tu computadora. En la sección Commit changes (Confirmar cambios), escribe un mensaje breve
     que describa los cambios realizados (por ejemplo, "Agregar archivo README"). Finalmente, Haz clic en Commit changes (Confirmar cambios) para guardar los archivos en el repositorio.
    <image src="/Laboratorios/Laboratorio 1 - Git y Github/Valeria/photos/git4.png" >
     
   **Método 2: Usando Git**<br>
   - `git clone https://github.com/tu-usuario/tu-repositorio.git` Clonar un repositorio
   - `cd tu-repositorio` Navegar a la carpeta del repositorio
   - `git status` Verificar el estado del repositorio
   - `git add nombre-del-archivo` Agregar un archivo específico al área de preparación (staging area)
   - `git add .` Agregar todos los archivos nuevos o modificados al área de preparación
   - `git commit -m "Agregar nuevos archivos"` Confirmar los cambios con un mensaje descriptivo
   - `git push origin main` Subir los cambios al repositorio remoto (GitHub)
   
