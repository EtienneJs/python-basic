# Aprende Python - Guía Básica

Esta guía te ayudará a aprender los conceptos fundamentales de Python desde cero.

## 📋 Tabla de Contenidos

- [¿Qué es Python?](#qué-es-python)
- [Instalación](#instalación)
- [Conceptos Básicos](#conceptos-básicos)
- [Estructuras de Control](#estructuras-de-control)
- [Funciones](#funciones)
- [Estructuras de Datos](#estructuras-de-datos)
- [Ejemplos Prácticos](#ejemplos-prácticos)
- [Recursos Adicionales](#recursos-adicionales)

## ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su sintaxis clara y legible, lo que lo hace ideal para principiantes.

**Características principales:**
- Sintaxis simple y fácil de leer
- Multiparadigma (orientado a objetos, funcional, imperativo)
- Gran comunidad y ecosistema de librerías
- Ideal para desarrollo web, ciencia de datos, IA y automatización

## Instalación

### Windows

1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Ejecuta el instalador y marca la opción "Add Python to PATH"
3. Verifica la instalación abriendo PowerShell y escribiendo:
```bash
python --version
```

### macOS/Linux

```bash
# macOS (usando Homebrew)
brew install python3

# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install python3 python3-pip
```

## Archivos de Ejemplo

Este repositorio contiene ejemplos separados por tema. Cada archivo incluye explicaciones y código ejecutable:

### Conceptos Básicos
- **`variables.py`** - Variables y tipos de datos (int, float, string, bool, None)
- **`operadores.py`** - Operadores aritméticos, de comparación y lógicos
- **`strings.py`** - Trabajo con cadenas de texto y f-strings
- **`entrada_salida.py`** - Función `print()` e `input()`

### Estructuras de Control
- **`if_else.py`** - Estructuras condicionales (if, elif, else)
- **`for_loop.py`** - Bucles for y diferentes formas de iteración
- **`while_loop.py`** - Bucles while
- **`break_continue.py`** - Control de flujo con break y continue

### Funciones y Estructuras de Datos
- **`funciones.py`** - Definición y uso de funciones
- **`listas.py`** - Trabajo con listas (arrays)
- **`diccionarios.py`** - Trabajo con diccionarios (objetos clave-valor)
- **`tuplas.py`** - Tuplas (estructuras inmutables)
- **`sets.py`** - Conjuntos (sets) - elementos únicos

### Ejemplos Prácticos
- **`calculadora.py`** - Calculadora simple con funciones
- **`lista_tareas.py`** - Aplicación de lista de tareas (to-do list)
- **`contador_palabras.py`** - Análisis de texto y conteo de palabras

Para ejecutar cualquier archivo, usa:
```bash
python nombre_archivo.py
```

## Conceptos Básicos

Python es un lenguaje de tipado dinámico, no necesitas declarar el tipo de variable explícitamente.

Ver los archivos: `variables.py`, `operadores.py`, `strings.py`, `entrada_salida.py`

## Estructuras de Control

Ver los archivos: `if_else.py`, `for_loop.py`, `while_loop.py`, `break_continue.py`

## Funciones

Las funciones te permiten reutilizar código. Ver el archivo: `funciones.py`

## Estructuras de Datos

Ver los archivos:
- **`listas.py`** - Listas (arrays mutables)
- **`diccionarios.py`** - Diccionarios (estructuras clave-valor)
- **`tuplas.py`** - Tuplas (estructuras inmutables)
- **`sets.py`** - Conjuntos (elementos únicos)

## Ejemplos Prácticos

Ejemplos completos y ejecutables:
- **`calculadora.py`** - Calculadora simple con funciones
- **`lista_tareas.py`** - Aplicación de lista de tareas (to-do list)
- **`contador_palabras.py`** - Análisis de texto y conteo de palabras

## Recursos Adicionales

### Documentación Oficial
- [Documentación de Python](https://docs.python.org/es/3/)
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/)

### Práctica
- [Exercism - Python Track](https://exercism.org/tracks/python)
- [LeetCode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/domains/python)

### Librerías Populares
- **NumPy**: Cálculos numéricos y arrays
- **Pandas**: Análisis de datos
- **Matplotlib**: Visualización de datos
- **Flask/Django**: Desarrollo web
- **Requests**: Peticiones HTTP

### Comandos Útiles

```bash
# Ejecutar un archivo Python
python archivo.py

# Instalar una librería
pip install nombre_libreria

# Ver librerías instaladas
pip list

# Crear entorno virtual (recomendado)
python -m venv mi_entorno

# Activar entorno virtual (Windows)
mi_entorno\Scripts\activate

# Activar entorno virtual (macOS/Linux)
source mi_entorno/bin/activate
```

## Consejos para Principiantes

1. **Practica regularmente**: La práctica constante es clave para aprender programación
2. **Empieza con lo básico**: No te apresures, domina los fundamentos primero
3. **Lee código de otros**: Aprende de proyectos en GitHub
4. **Resuelve problemas**: Intenta resolver pequeños problemas programáticamente
5. **Usa la documentación**: Python tiene excelente documentación oficial
6. **No tengas miedo de experimentar**: Prueba cosas nuevas y aprende de los errores

¡Feliz programación! 🐍

