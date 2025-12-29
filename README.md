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

## Conceptos Básicos

### Variables y Tipos de Datos

Python es un lenguaje de tipado dinámico, no necesitas declarar el tipo de variable explícitamente.

```python
# Números enteros
edad = 25
temperatura = -10

# Números decimales (float)
precio = 19.99
pi = 3.14159

# Texto (string)
nombre = "Juan"
mensaje = 'Hola mundo'

# Booleanos
es_estudiante = True
tiene_trabajo = False

# Tipo None (equivalente a null)
valor = None
```

### Operadores

```python
# Operadores aritméticos
suma = 5 + 3        # 8
resta = 10 - 4      # 6
multiplicacion = 3 * 4  # 12
division = 15 / 3   # 5.0 (siempre devuelve float)
division_entera = 15 // 3  # 5 (devuelve int)
modulo = 15 % 4     # 3 (resto de la división)
potencia = 2 ** 3   # 8

# Operadores de comparación
5 == 5    # True (igual)
5 != 3    # True (diferente)
5 > 3     # True (mayor que)
5 < 10    # True (menor que)
5 >= 5    # True (mayor o igual)
5 <= 4    # False (menor o igual)

# Operadores lógicos
True and False  # False
True or False   # True
not True        # False
```

### Entrada y Salida

```python
# Imprimir en consola
print("Hola, mundo!")
print(f"Tu nombre es {nombre}")  # f-strings (formato moderno)

# Leer entrada del usuario
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))  # Convertir a entero
```

## Estructuras de Control

### Condicionales (if/elif/else)

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

### Bucles (Loops)

#### For Loop

```python
# Iterar sobre una secuencia
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Iterar con rango
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)
```

#### While Loop

```python
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar contador
```

#### Break y Continue

```python
# Break: salir del bucle
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)

# Continue: saltar a la siguiente iteración
for i in range(10):
    if i % 2 == 0:
        continue  # Salta números pares
    print(i)  # Solo imprime impares
```

## Funciones

Las funciones te permiten reutilizar código.

```python
# Definir una función
def saludar(nombre):
    return f"¡Hola, {nombre}!"

# Llamar la función
mensaje = saludar("María")
print(mensaje)

# Función con múltiples parámetros
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8

# Función con parámetros por defecto
def presentarse(nombre, edad=18):
    return f"Soy {nombre} y tengo {edad} años"

print(presentarse("Juan"))  # Usa edad=18 por defecto
print(presentarse("Ana", 25))  # Pasa edad explícitamente

# Función con múltiples valores de retorno
def dividir(a, b):
    cociente = a // b
    resto = a % b
    return cociente, resto

coc, rest = dividir(17, 5)
print(f"Cociente: {coc}, Resto: {rest}")
```

## Estructuras de Datos

### Listas

```python
# Crear una lista
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]

# Acceder a elementos (índices empiezan en 0)
print(frutas[0])  # "manzana"
print(frutas[-1])  # "naranja" (último elemento)

# Modificar elementos
frutas[1] = "pera"

# Agregar elementos
frutas.append("uva")  # Agrega al final
frutas.insert(1, "mango")  # Inserta en posición 1

# Eliminar elementos
frutas.remove("banana")  # Elimina por valor
del frutas[0]  # Elimina por índice

# Longitud de la lista
print(len(frutas))

# Slice (rebanadas)
numeros = [0, 1, 2, 3, 4, 5]
print(numeros[1:4])    # [1, 2, 3]
print(numeros[:3])     # [0, 1, 2] (desde el inicio)
print(numeros[3:])     # [3, 4, 5] (hasta el final)
```

### Diccionarios

```python
# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a valores
print(persona["nombre"])  # "Juan"
print(persona.get("edad"))  # 30 (método seguro)

# Agregar o modificar
persona["profesion"] = "Programador"
persona["edad"] = 31

# Eliminar
del persona["ciudad"]

# Iterar sobre diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Obtener solo claves o valores
print(persona.keys())    # dict_keys(['nombre', 'edad', 'profesion'])
print(persona.values())  # dict_values(['Juan', 31, 'Programador'])
```

### Tuplas

```python
# Las tuplas son inmutables (no se pueden modificar)
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")

# Acceder a elementos
print(coordenadas[0])  # 10

# Desempaquetado
x, y = coordenadas
print(f"x: {x}, y: {y}")
```

### Conjuntos (Sets)

```python
# Los sets almacenan elementos únicos (sin duplicados)
numeros = {1, 2, 3, 4, 5}
colores = set(["rojo", "verde", "azul", "rojo"])  # {"rojo", "verde", "azul"}

# Agregar elementos
colores.add("amarillo")

# Operaciones de conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2))   # {1, 2}
```

## Ejemplos Prácticos

### Calculadora Simple

```python
def calculadora():
    num1 = float(input("Ingresa el primer número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))
    
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Error: No se puede dividir por cero"
    else:
        return "Operación no válida"
    
    return f"Resultado: {resultado}"

print(calculadora())
```

### Lista de Tareas

```python
tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada")

def ver_tareas():
    if tareas:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes")

def eliminar_tarea(numero):
    if 1 <= numero <= len(tareas):
        tarea_eliminada = tareas.pop(numero - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada")
    else:
        print("Número de tarea inválido")

# Ejemplo de uso
agregar_tarea("Estudiar Python")
agregar_tarea("Hacer ejercicio")
ver_tareas()
eliminar_tarea(1)
ver_tareas()
```

### Contador de Palabras

```python
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def contar_caracteres(texto):
    return len(texto)

def contar_palabras_unicas(texto):
    palabras = texto.lower().split()
    return len(set(palabras))

texto = "Python es genial Python es fácil"
print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Total de caracteres: {contar_caracteres(texto)}")
print(f"Palabras únicas: {contar_palabras_unicas(texto)}")
```

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

