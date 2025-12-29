"""
Variables y Tipos de Datos en Python

Este archivo muestra los diferentes tipos de datos básicos en Python.
Python es un lenguaje de tipado dinámico, no necesitas declarar el tipo explícitamente.
"""

# ===== NÚMEROS ENTEROS (int) =====
print("=== Números Enteros (int) ===")
edad = 25
temperatura = -10
poblacion = 1000000

print(f"Edad: {edad}")
print(f"Temperatura: {temperatura}")
print(f"Población: {poblacion}")
print(f"Tipo de edad: {type(edad)}")

print("\n" + "="*50 + "\n")

# ===== NÚMEROS DECIMALES (float) =====
print("=== Números Decimales (float) ===")
precio = 19.99
pi = 3.14159
temperatura_decimal = -5.5

print(f"Precio: {precio}")
print(f"Pi: {pi}")
print(f"Temperatura decimal: {temperatura_decimal}")
print(f"Tipo de precio: {type(precio)}")

print("\n" + "="*50 + "\n")

# ===== TEXTO (string) =====
print("=== Texto (string) ===")
nombre = "Juan"
mensaje = 'Hola mundo'
descripcion = """Este es un texto
que puede abarcar
varias líneas"""

print(f"Nombre: {nombre}")
print(f"Mensaje: {mensaje}")
print(f"Descripción:\n{descripcion}")
print(f"Tipo de nombre: {type(nombre)}")

print("\n" + "="*50 + "\n")

# ===== BOOLEANOS (bool) =====
print("=== Booleanos (bool) ===")
es_estudiante = True
tiene_trabajo = False
es_mayor = 18 >= 18

print(f"Es estudiante: {es_estudiante}")
print(f"Tiene trabajo: {tiene_trabajo}")
print(f"Es mayor: {es_mayor}")
print(f"Tipo de es_estudiante: {type(es_estudiante)}")

print("\n" + "="*50 + "\n")

# ===== TIPO NONE =====
print("=== Tipo None ===")
valor = None
resultado = None

print(f"Valor: {valor}")
print(f"Resultado: {resultado}")
print(f"Tipo de valor: {type(valor)}")

# None se usa comúnmente para indicar ausencia de valor
def buscar_elemento(lista, elemento):
    for item in lista:
        if item == elemento:
            return item
    return None  # No encontrado

print("\n" + "="*50 + "\n")

# ===== CONVERSIÓN DE TIPOS =====
print("=== Conversión de Tipos ===")

# Convertir a int
numero_texto = "25"
numero_entero = int(numero_texto)
print(f"'25' convertido a int: {numero_entero} (tipo: {type(numero_entero)})")

# Convertir a float
numero_float = float(numero_entero)
print(f"25 convertido a float: {numero_float} (tipo: {type(numero_float)})")

# Convertir a string
edad = 30
edad_texto = str(edad)
print(f"30 convertido a string: '{edad_texto}' (tipo: {type(edad_texto)})")

# Convertir a bool
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('texto'): {bool('texto')}")
print(f"bool(''): {bool('')}")  # String vacío es False
print(f"bool(None): {bool(None)}")

print("\n" + "="*50 + "\n")

# ===== VARIABLES MÚLTIPLES =====
print("=== Asignación Múltiple ===")

# Asignar múltiples variables
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Asignar mismo valor a múltiples variables
a = b = c = 10
print(f"a={a}, b={b}, c={c}")

print("\n" + "="*50 + "\n")

# ===== REGLAS DE NOMBRES DE VARIABLES =====
print("=== Reglas de Nombres de Variables ===")
print("""
Las variables en Python deben seguir estas reglas:
- Pueden contener letras, números y guiones bajos
- Deben empezar con una letra o guión bajo
- Son sensibles a mayúsculas y minúsculas
- No pueden ser palabras reservadas (if, for, def, etc.)

Ejemplos válidos:
- nombre
- edad_persona
- _variable_privada
- variable123

Ejemplos inválidos:
- 2nombre (empieza con número)
- nombre-persona (guión no permitido)
- if (palabra reservada)
""")
