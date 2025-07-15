#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para practicar comandos de Git en el proyecto de análisis de retrasos de vuelos.
Este archivo contiene ejemplos y explicaciones de los comandos Git más útiles.
"""

print("=== COMANDOS GIT PARA EL PROYECTO DE ANÁLISIS DE RETRASOS DE VUELOS ===")

# Lista de comandos Git básicos con ejemplos y explicaciones
git_commands = {
    "git init": "Inicializa un nuevo repositorio Git en el directorio actual.",
    
    "git status": "Muestra el estado del repositorio: archivos modificados, preparados o sin seguimiento.",
    
    "git add": """Añade archivos al área de preparación para el próximo commit.
    Ejemplos:
    - git add delay_analysis.py  # Añade un archivo específico
    - git add .                  # Añade todos los archivos modificados
    - git add *.py               # Añade todos los archivos Python""",
    
    "git commit": """Guarda los cambios en el repositorio con un mensaje descriptivo.
    Ejemplos:
    - git commit -m "Implementada función de análisis avanzado"
    - git commit -am "Corregido bug en limpieza de datos"  # Para archivos ya rastreados""",
    
    "git checkout": """Cambia entre ramas o restaura archivos.
    Ejemplos:
    - git checkout analisis-avanzado  # Cambiar a una rama existente
    - git checkout -b nueva-rama      # Crear y cambiar a una nueva rama
    - git checkout -- delay_analysis.py  # Restaurar archivo al último commit""",
    
    "git branch": """Gestiona las ramas del repositorio.
    Ejemplos:
    - git branch                 # Lista todas las ramas
    - git branch mejora-graficas # Crea una nueva rama
    - git branch -d rama-vieja   # Elimina una rama""",
    
    "git merge": """Combina cambios de una rama a otra.
    Ejemplo:
    - git merge analisis-avanzado  # Estando en main, incorpora cambios de otra rama""",
    
    "git config": """Configura opciones de Git.
    Ejemplos:
    - git config --global user.name "Tu Nombre"
    - git config --global user.email "tu.email@ejemplo.com"
    - git config --list  # Ver configuración actual""",
    
    "git reset": """Deshace cambios o commits.
    Ejemplos:
    - git reset --soft HEAD~1  # Deshace último commit manteniendo cambios
    - git reset --hard HEAD~1  # Deshace último commit y los cambios
    - git reset HEAD archivo.py  # Quita archivo del área de preparación""",
    
    "git log": """Muestra el historial de commits.
    Ejemplos:
    - git log
    - git log --oneline  # Formato resumido
    - git log --graph --oneline --all  # Historial gráfico""",
    
    "git reflog": "Muestra registro de todos los cambios en HEAD, útil para recuperar commits perdidos.",
    
    "git diff": """Muestra diferencias entre commits, ramas, etc.
    Ejemplos:
    - git diff  # Diferencias entre área de trabajo y último commit
    - git diff --staged  # Diferencias en área de preparación
    - git diff commit1 commit2  # Diferencias entre dos commits""",
    
    "git mv": """Mueve o renombra archivos rastreados por Git.
    Ejemplo:
    - git mv old_name.py new_name.py""",
    
    "git rm": """Elimina archivos del repositorio y del área de trabajo.
    Ejemplo:
    - git rm archivo_obsoleto.py""",
    
    "git tag": """Marca puntos específicos en la historia como importantes.
    Ejemplos:
    - git tag v1.0.0  # Etiqueta ligera
    - git tag -a v1.0.0 -m "Versión 1.0.0"  # Etiqueta anotada
    - git tag  # Listar etiquetas""",
    
    "git show": """Muestra información sobre objetos Git (commits, tags, etc.).
    Ejemplos:
    - git show  # Información del último commit
    - git show v1.0.0  # Información de una etiqueta"""
}

# Comandos adicionales útiles
additional_commands = {
    "git pull": """Obtiene cambios del repositorio remoto y los integra.
    Ejemplo:
    - git pull origin main""",
    
    "git push": """Envía los commits locales al repositorio remoto.
    Ejemplo:
    - git push origin main""",
    
    "git remote": """Gestiona repositorios remotos.
    Ejemplos:
    - git remote -v  # Ver repositorios remotos
    - git remote add origin https://github.com/usuario/repo.git""",
    
    "git stash": """Guarda temporalmente cambios que no están listos para commit.
    Ejemplos:
    - git stash  # Guardar cambios actuales
    - git stash pop  # Aplicar y eliminar el último stash""",
    
    "git fetch": "Descarga objetos y referencias del repositorio remoto sin integrarlos.",
    
    "git blame": """Muestra quién modificó cada línea de un archivo y cuándo.
    Ejemplo:
    - git blame delay_analysis.py""",
    
    "git cherry-pick": """Aplica cambios introducidos por commits específicos.
    Ejemplo:
    - git cherry-pick abc123""",
    
    "git rebase": """Reorganiza commits, útil para mantener un historial limpio.
    Ejemplos:
    - git rebase main
    - git rebase -i HEAD~3  # Modo interactivo"""
}

# Función para mostrar los comandos
def mostrar_comandos():
    print("\n=== COMANDOS BÁSICOS ===")
    for cmd, desc in git_commands.items():
        print(f"\n{cmd}:")
        print(f"{desc}")
    
    print("\n\n=== COMANDOS ADICIONALES ÚTILES ===")
    for cmd, desc in additional_commands.items():
        print(f"\n{cmd}:")
        print(f"{desc}")
    
    print("\n\n=== FLUJO DE TRABAJO TÍPICO PARA ESTE PROYECTO ===")
    print("""
1. Inicializar el repositorio (una sola vez):
   git init
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu.email@ejemplo.com"

2. Crear una rama para una nueva característica:
   git checkout -b nueva-caracteristica

3. Realizar cambios y guardarlos:
   # Editar archivos...
   git add .
   git commit -m "Implementada nueva característica de análisis"

4. Integrar cambios a la rama principal:
   git checkout main
   git merge nueva-caracteristica

5. Si trabajas con un repositorio remoto:
   git push origin main
    """)

# Ejecutar si se llama directamente
if __name__ == "__main__":
    mostrar_comandos()
    print("\nPara obtener ayuda sobre cualquier comando: git help comando")