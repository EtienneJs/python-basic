"""
Entrada y Salida en Python

Este archivo muestra cómo obtener datos del usuario y mostrar información.
"""

# ===== SALIDA (PRINT) =====
print("=== Función print() ===")

# Imprimir texto simple
print("Hola, mundo!")

# Imprimir múltiples valores
nombre = "Juan"
edad = 25
print("Nombre:", nombre, "Edad:", edad)

# Usando f-strings (formato moderno)
print(f"Tu nombre es {nombre}")

# Imprimir con formato
print("Tu nombre es {} y tienes {} años".format(nombre, edad))

# Imprimir con separador personalizado
print("Python", "es", "genial", sep="-")  # Python-es-genial

# Imprimir sin salto de línea (end)
print("Hola", end=" ")
print("Mundo")  # Hola Mundo

print("\n" + "="*50 + "\n")

# ===== ENTRADA (INPUT) =====
print("=== Función input() ===")

# Leer entrada del usuario (texto)
# nombre_usuario = input("¿Cuál es tu nombre? ")
# print(f"Hola, {nombre_usuario}!")

# Leer y convertir a entero
# edad_usuario = int(input("¿Cuántos años tienes? "))
# print(f"Tienes {edad_usuario} años")

# Leer y convertir a float
# precio = float(input("Ingresa un precio: "))
# print(f"El precio es: {precio}")

# Ejemplo completo comentado (descomenta para probar)
"""
print("\n--- Ejemplo Interactivo ---")
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿En qué ciudad vives? ")

print(f"\nInformación ingresada:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")
"""

