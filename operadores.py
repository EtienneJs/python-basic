"""
Operadores en Python

Este archivo muestra los diferentes tipos de operadores disponibles en Python.
"""

# ===== OPERADORES ARITMÉTICOS =====
print("=== Operadores Aritméticos ===")
suma = 5 + 3        # 8
resta = 10 - 4      # 6
multiplicacion = 3 * 4  # 12
division = 15 / 3   # 5.0 (siempre devuelve float)
division_entera = 15 // 3  # 5 (devuelve int)
modulo = 15 % 4     # 3 (resto de la división)
potencia = 2 ** 3   # 8

print(f"5 + 3 = {suma}")
print(f"10 - 4 = {resta}")
print(f"3 * 4 = {multiplicacion}")
print(f"15 / 3 = {division}")
print(f"15 // 3 = {division_entera}")
print(f"15 % 4 = {modulo}")
print(f"2 ** 3 = {potencia}")

print("\n" + "="*50 + "\n")

# ===== OPERADORES DE COMPARACIÓN =====
print("=== Operadores de Comparación ===")
print(f"5 == 5: {5 == 5}")      # True (igual)
print(f"5 != 3: {5 != 3}")      # True (diferente)
print(f"5 > 3: {5 > 3}")        # True (mayor que)
print(f"5 < 10: {5 < 10}")      # True (menor que)
print(f"5 >= 5: {5 >= 5}")      # True (mayor o igual)
print(f"5 <= 4: {5 <= 4}")      # False (menor o igual)

print("\n" + "="*50 + "\n")

# ===== OPERADORES LÓGICOS =====
print("=== Operadores Lógicos ===")
print(f"True and False: {True and False}")  # False
print(f"True or False: {True or False}")    # True
print(f"not True: {not True}")              # False

# Ejemplos prácticos
edad = 25
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia
print(f"\nEdad: {edad}, Tiene licencia: {tiene_licencia}")
print(f"Puede conducir: {puede_conducir}")

