"""
Funciones en Python

Este archivo muestra cómo crear y usar funciones en Python.
"""

# ===== FUNCIÓN BÁSICA =====
print("=== Función Básica ===")

def saludar(nombre):
    return f"¡Hola, {nombre}!"

# Llamar la función
mensaje = saludar("María")
print(mensaje)

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN CON MÚLTIPLES PARÁMETROS =====
print("=== Función con Múltiples Parámetros ===")

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"5 + 3 = {resultado}")

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN CON PARÁMETROS POR DEFECTO =====
print("=== Función con Parámetros por Defecto ===")

def presentarse(nombre, edad=18):
    return f"Soy {nombre} y tengo {edad} años"

# Usa edad=18 por defecto
print(presentarse("Juan"))

# Pasa edad explícitamente
print(presentarse("Ana", 25))

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN CON MÚLTIPLES VALORES DE RETORNO =====
print("=== Función con Múltiples Valores de Retorno ===")

def dividir(a, b):
    cociente = a // b
    resto = a % b
    return cociente, resto

coc, rest = dividir(17, 5)
print(f"17 dividido entre 5:")
print(f"Cociente: {coc}, Resto: {rest}")

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN SIN RETORNO =====
print("=== Función sin Retorno ===")

def imprimir_info(nombre, edad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    # No necesita return

imprimir_info("Carlos", 30)

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN CON ARGUMENTOS POSICIONALES Y POR NOMBRE =====
print("=== Argumentos Posicionales y por Nombre ===")

def crear_persona(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

# Por posición
persona1 = crear_persona("Juan", 25, "Madrid")
print(persona1)

# Por nombre
persona2 = crear_persona(ciudad="Barcelona", edad=30, nombre="Ana")
print(persona2)

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN CON NÚMERO VARIABLE DE ARGUMENTOS =====
print("=== Función con *args ===")

def sumar_varios(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

resultado1 = sumar_varios(1, 2, 3)
resultado2 = sumar_varios(1, 2, 3, 4, 5)

print(f"Suma de (1, 2, 3): {resultado1}")
print(f"Suma de (1, 2, 3, 4, 5): {resultado2}")

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN CON **kwargs (KEYWORD ARGUMENTS) =====
print("=== Función con **kwargs ===")

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Pedro", edad=28, ciudad="Valencia")

print("\n" + "="*50 + "\n")

# ===== FUNCIÓN DENTRO DE FUNCIÓN =====
print("=== Función dentro de Función ===")

def operacion_matematica(operacion, a, b):
    def sumar(x, y):
        return x + y
    
    def multiplicar(x, y):
        return x * y
    
    if operacion == "sumar":
        return sumar(a, b)
    elif operacion == "multiplicar":
        return multiplicar(a, b)
    else:
        return "Operación no válida"

print(f"Sumar 5 y 3: {operacion_matematica('sumar', 5, 3)}")
print(f"Multiplicar 5 y 3: {operacion_matematica('multiplicar', 5, 3)}")

