"""
Diccionarios en Python

Este archivo muestra cómo trabajar con diccionarios en Python.
"""

# ===== CREAR DICCIONARIOS =====
print("=== Crear Diccionarios ===")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Diccionario vacío
vacio = {}

# Usando dict()
otro_diccionario = dict(nombre="Ana", edad=25)

print(f"Persona: {persona}")
print(f"Vacío: {vacio}")
print(f"Otro diccionario: {otro_diccionario}")

print("\n" + "="*50 + "\n")

# ===== ACCEDER A VALORES =====
print("=== Acceder a Valores ===")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso directo con []
print(f"persona['nombre']: {persona['nombre']}")

# Acceso con get() (más seguro, devuelve None si no existe)
print(f"persona.get('edad'): {persona.get('edad')}")
print(f"persona.get('profesion'): {persona.get('profesion')}")  # None
print(f"persona.get('profesion', 'No especificado'): {persona.get('profesion', 'No especificado')}")

print("\n" + "="*50 + "\n")

# ===== AGREGAR O MODIFICAR =====
print("=== Agregar o Modificar ===")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print(f"Original: {persona}")

# Agregar nueva clave-valor
persona["profesion"] = "Programador"
print(f"Después de agregar 'profesion': {persona}")

# Modificar valor existente
persona["edad"] = 31
print(f"Después de modificar 'edad': {persona}")

print("\n" + "="*50 + "\n")

# ===== ELIMINAR ELEMENTOS =====
print("=== Eliminar Elementos ===")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Programador"
}

print(f"Original: {persona}")

# del
del persona["ciudad"]
print(f"Después de del persona['ciudad']: {persona}")

# pop() - Elimina y devuelve el valor
edad_eliminada = persona.pop("edad")
print(f"Edad eliminada: {edad_eliminada}")
print(f"Después de pop('edad'): {persona}")

# popitem() - Elimina y devuelve el último par clave-valor
ultimo = persona.popitem()
print(f"Último elemento eliminado: {ultimo}")
print(f"Después de popitem(): {persona}")

print("\n" + "="*50 + "\n")

# ===== ITERAR SOBRE DICCIONARIO =====
print("=== Iterar sobre Diccionario ===")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Iterar sobre claves (por defecto)
print("Claves:")
for clave in persona:
    print(f"  {clave}")

# Iterar sobre claves explícitamente
print("\nClaves (con .keys()):")
for clave in persona.keys():
    print(f"  {clave}")

# Iterar sobre valores
print("\nValores:")
for valor in persona.values():
    print(f"  {valor}")

# Iterar sobre items (clave, valor)
print("\nItems (clave: valor):")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

print("\n" + "="*50 + "\n")

# ===== MÉTODOS ÚTILES =====
print("=== Métodos Útiles ===")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print(f"Diccionario: {persona}")
print(f"Claves: {list(persona.keys())}")
print(f"Valores: {list(persona.values())}")
print(f"Items: {list(persona.items())}")
print(f"Longitud: {len(persona)}")

# Verificar si existe una clave
print(f"'nombre' in persona: {'nombre' in persona}")
print(f"'profesion' in persona: {'profesion' in persona}")

print("\n" + "="*50 + "\n")

# ===== DICCIONARIOS ANIDADOS =====
print("=== Diccionarios Anidados ===")
estudiantes = {
    "estudiante1": {
        "nombre": "Ana",
        "edad": 20,
        "notas": [85, 90, 88]
    },
    "estudiante2": {
        "nombre": "Carlos",
        "edad": 21,
        "notas": [92, 87, 95]
    }
}

print("Estudiantes:")
for clave, datos in estudiantes.items():
    print(f"\n{clave}:")
    print(f"  Nombre: {datos['nombre']}")
    print(f"  Edad: {datos['edad']}")
    print(f"  Notas: {datos['notas']}")
    print(f"  Promedio: {sum(datos['notas']) / len(datos['notas']):.2f}")

print("\n" + "="*50 + "\n")

# ===== ACTUALIZAR DICCIONARIO =====
print("=== Actualizar Diccionario ===")
persona = {"nombre": "Juan", "edad": 30}
nuevos_datos = {"ciudad": "Madrid", "profesion": "Programador"}

print(f"Original: {persona}")
persona.update(nuevos_datos)
print(f"Después de update(): {persona}")

