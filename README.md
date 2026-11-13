# Trabajo Práctico Integrador Programación 1.

## Gestion de Datos y Países en Python

El proyecto es una aplicación interactiva de consola, desarrollada en Python para gestionar información sobre Países.
El código permite funciones como agregar países, ordenarlos de la manera que el usuario quiera, dar estadísticas e información sobre el país que quiera; Utilizando estructuras de datos
como listas y diccionarios y modularización.

# Funcionalidades

El sistema cuenta con un menú interactivo que permite realizar las siguientes operaciones:

1. Agregar un país: Permite ingresar un nuevo registro asegurando que no haya campos vacíos y validando tipos de datos numéricos.
2. Actualiar datos: Buscar un país por coincidencia exacta y permite modificar población y superficie.
3. Buscar un país: Encuentra países mediante coincidencia exacta o parcial, ignorando mayúsculas y minúsculas.
4. Filtrar por países:
   Permite filtrar por: Continente específico - Por rango numérico de población - Por rango numérico de superficie
5. Ordenar países: Permite ordenar la lista de países de forma ascendente o descendente según el Nombre, la Población o la Superficie.
6. Mostrar estadísticas: 
    - País con mayor y menor población.
    - Promedio global de población y superficie.
    - Cantidad total de países agrupados por continente.

# Instrucciones de Uso y Ejecución

# Requisitos
- Python 3.x Instalado en el sistema
- Consola de comandos (Git bash, CMD, o terminal)

# Pasos para su correcta ejecución
1. Clonar este repositorio o descargar los archivos.
2. Comprobar que los archivos 'main.py' y 'paises.csv' se encuentren en el mismo directorio.
3. Abrir la terminal en la ruta de la carpeta del proyecto.
4. Ejecutar el siguiente comando:
   ```bash
   python main.py

# Ejemplos de Entrada y Salida

--- Buscar País --
Ingrese el nombre del país: arg

Se encontraron 1 coincidencia(s):
- Argentina (América) | Población: 45376763 | Superficie: 2780400 km2

# Ejemplo estadísticas [Opción 6]

--- Estadísticas Generales ---
País con mayor población: Brasil (213993437 Habitantes.)
País con menor población: Alemania (83149300 Habitantes.)
Promedio de población: 117,079,875 Habitantes.
Promedio de superficie: 2,933,791 km2
Cantidad de países por continente:
 - América: 2
 - Asia: 1
 - Europa: 1

# Integrantes del Equipo: [COM3]
- Facundo Peña
- Renzo Narvaez

# Enlaces de Entrega

# Video demostrativo:
https://youtu.be/BTyFEYHSK30
