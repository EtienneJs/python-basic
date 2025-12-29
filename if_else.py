"""
Condicionales (if/elif/else) en Python

Este archivo muestra cómo usar estructuras condicionales en Python.
"""

# ===== IF SIMPLE =====
print("=== If Simple ===")
edad = 18

if edad >= 18:
    print("Eres mayor de edad")

print("\n" + "="*50 + "\n")

# ===== IF/ELSE =====
print("=== If/Else ===")
temperatura = 25

if temperatura > 30:
    print("Hace mucho calor")
else:
    print("La temperatura está bien")

print("\n" + "="*50 + "\n")

# ===== IF/ELIF/ELSE =====
print("=== If/Elif/Else ===")
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")

print("\n" + "="*50 + "\n")

# ===== EJEMPLOS ADICIONALES =====
print("=== Ejemplos Adicionales ===")

# Calificación
nota = 85

if nota >= 90:
    calificacion = "A"
elif nota >= 80:
    calificacion = "B"
elif nota >= 70:
    calificacion = "C"
elif nota >= 60:
    calificacion = "D"
else:
    calificacion = "F"

print(f"Nota: {nota}, Calificación: {calificacion}")

# Número positivo, negativo o cero
numero = -5

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

print("\n" + "="*50 + "\n")

# ===== CONDICIONALES ANIDADOS =====
print("=== Condicionales Anidados ===")
usuario_activo = True
edad_usuario = 20

if usuario_activo:
    if edad_usuario >= 18:
        print("Usuario activo y mayor de edad")
    else:
        print("Usuario activo pero menor de edad")
else:
    print("Usuario no activo")

print("\n" + "="*50 + "\n")

# ===== OPERADORES LÓGICOS EN CONDICIONALES =====
print("=== Operadores Lógicos ===")
tiene_licencia = True
edad = 25
tiene_seguro = True

if edad >= 18 and tiene_licencia and tiene_seguro:
    print("Puede conducir")
elif edad >= 18 and tiene_licencia:
    print("Puede conducir pero necesita seguro")
else:
    print("No puede conducir")

