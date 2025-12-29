"""
Bucles While en Python

Este archivo muestra cómo usar bucles while en Python.
"""

# ===== WHILE BÁSICO =====
print("=== While Básico ===")
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar contador

print("\n" + "="*50 + "\n")

# ===== WHILE CON CONDICIÓN =====
print("=== While con Condición ===")
numero = 1

while numero <= 10:
    print(numero, end=" ")
    numero += 1
print("\n")

print("\n" + "="*50 + "\n")

# ===== WHILE CON ENTRADA DEL USUARIO =====
print("=== While con Entrada del Usuario ===")
# Ejemplo comentado (descomenta para probar)
"""
respuesta = ""

while respuesta.lower() != "salir":
    respuesta = input("Escribe 'salir' para terminar: ")
    print(f"Escribiste: {respuesta}")
"""

print("\n" + "="*50 + "\n")

# ===== WHILE CON BREAK =====
print("=== While con Break ===")
contador = 0

while True:
    print(contador, end=" ")
    contador += 1
    if contador >= 5:
        break  # Sale del bucle cuando contador es 5

print("\n")

print("\n" + "="*50 + "\n")

# ===== WHILE CON CONTINUE =====
print("=== While con Continue ===")
numero = 0

while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  # Salta números pares
    print(numero, end=" ")  # Solo imprime impares

print("\n")

print("\n" + "="*50 + "\n")

# ===== EJEMPLO: ADIVINAR NÚMERO =====
print("=== Ejemplo: Adivinar Número ===")
numero_secreto = 7
intentos = 0
max_intentos = 3

# Ejemplo comentado (descomenta para probar)
"""
while intentos < max_intentos:
    adivinanza = int(input("Adivina el número (1-10): "))
    intentos += 1
    
    if adivinanza == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos")
        break
    elif adivinanza < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    
    if intentos == max_intentos:
        print(f"Se acabaron los intentos. El número era {numero_secreto}")
"""

print("\n" + "="*50 + "\n")

# ===== WHILE CON LISTA =====
print("=== While con Lista ===")
numeros = [1, 2, 3, 4, 5]
indice = 0

while indice < len(numeros):
    print(f"Elemento en índice {indice}: {numeros[indice]}")
    indice += 1

