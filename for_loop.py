"""
Bucles For en Python

Este archivo muestra diferentes formas de usar bucles for en Python.
"""

# ===== ITERAR SOBRE UNA LISTA =====
print("=== Iterar sobre una Lista ===")
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

print("\n" + "="*50 + "\n")

# ===== ITERAR CON RANGE =====
print("=== Iterar con range() ===")

# range(5) genera: 0, 1, 2, 3, 4
print("range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")

# range(2, 6) genera: 2, 3, 4, 5
print("range(2, 6):")
for i in range(2, 6):
    print(i, end=" ")
print("\n")

# range(0, 10, 2) genera: 0, 2, 4, 6, 8 (salto de 2)
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

print("\n" + "="*50 + "\n")

# ===== ITERAR SOBRE STRING =====
print("=== Iterar sobre String ===")
palabra = "Python"

for letra in palabra:
    print(letra, end="-")
print("\n")

print("\n" + "="*50 + "\n")

# ===== ITERAR CON ÍNDICES (enumerate) =====
print("=== Iterar con Índices (enumerate) ===")
frutas = ["manzana", "banana", "naranja"]

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Con índice inicial personalizado
print("\nCon índice inicial en 1:")
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")

print("\n" + "="*50 + "\n")

# ===== ITERAR SOBRE DICCIONARIO =====
print("=== Iterar sobre Diccionario ===")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Iterar sobre claves
print("Claves:")
for clave in persona:
    print(clave)

# Iterar sobre valores
print("\nValores:")
for valor in persona.values():
    print(valor)

# Iterar sobre items (clave, valor)
print("\nItems (clave: valor):")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

print("\n" + "="*50 + "\n")

# ===== BUCLES ANIDADOS =====
print("=== Bucles Anidados ===")
print("Tabla de multiplicar del 2:")
for i in range(1, 6):
    for j in range(1, 6):
        resultado = i * j
        print(f"{i} x {j} = {resultado}", end="  ")
    print()  # Nueva línea después de cada fila

print("\n" + "="*50 + "\n")

# ===== EJEMPLO PRÁCTICO =====
print("=== Ejemplo Práctico: Sumar números ===")
numeros = [1, 2, 3, 4, 5]
suma = 0

for numero in numeros:
    suma += numero
    print(f"Sumando {numero}, total hasta ahora: {suma}")

print(f"\nSuma total: {suma}")

