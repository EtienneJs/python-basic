"""
Listas en Python

Este archivo muestra cómo trabajar con listas en Python.
"""

# ===== CREAR LISTAS =====
print("=== Crear Listas ===")
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]
mezclada = [1, "dos", 3.0, True]  # Puede contener diferentes tipos
vacia = []

print(f"Números: {numeros}")
print(f"Frutas: {frutas}")
print(f"Mezclada: {mezclada}")
print(f"Vacía: {vacia}")

print("\n" + "="*50 + "\n")

# ===== ACCEDER A ELEMENTOS =====
print("=== Acceder a Elementos ===")
frutas = ["manzana", "banana", "naranja", "uva", "pera"]

print(f"Lista: {frutas}")
print(f"Primer elemento [0]: {frutas[0]}")      # "manzana"
print(f"Último elemento [-1]: {frutas[-1]}")    # "pera"
print(f"Segundo elemento desde el final [-2]: {frutas[-2]}")  # "uva"

print("\n" + "="*50 + "\n")

# ===== MODIFICAR ELEMENTOS =====
print("=== Modificar Elementos ===")
frutas = ["manzana", "banana", "naranja"]
print(f"Antes: {frutas}")

frutas[1] = "pera"
print(f"Después de modificar índice 1: {frutas}")

print("\n" + "="*50 + "\n")

# ===== AGREGAR ELEMENTOS =====
print("=== Agregar Elementos ===")
frutas = ["manzana", "banana", "naranja"]
print(f"Lista original: {frutas}")

# append() - Agrega al final
frutas.append("uva")
print(f"Después de append('uva'): {frutas}")

# insert() - Inserta en posición específica
frutas.insert(1, "mango")
print(f"Después de insert(1, 'mango'): {frutas}")

# extend() - Agrega múltiples elementos
frutas.extend(["kiwi", "fresa"])
print(f"Después de extend(['kiwi', 'fresa']): {frutas}")

print("\n" + "="*50 + "\n")

# ===== ELIMINAR ELEMENTOS =====
print("=== Eliminar Elementos ===")
frutas = ["manzana", "banana", "naranja", "banana", "uva"]
print(f"Lista original: {frutas}")

# remove() - Elimina por valor (solo la primera ocurrencia)
frutas.remove("banana")
print(f"Después de remove('banana'): {frutas}")

# del - Elimina por índice
del frutas[0]
print(f"Después de del frutas[0]: {frutas}")

# pop() - Elimina y devuelve el último elemento
eliminado = frutas.pop()
print(f"Elemento eliminado con pop(): {eliminado}")
print(f"Después de pop(): {frutas}")

# pop(index) - Elimina y devuelve elemento en índice específico
eliminado = frutas.pop(0)
print(f"Elemento eliminado con pop(0): {eliminado}")
print(f"Después de pop(0): {frutas}")

print("\n" + "="*50 + "\n")

# ===== SLICE (REBANADAS) =====
print("=== Slice (Rebanadas) ===")
numeros = [0, 1, 2, 3, 4, 5]
print(f"Lista completa: {numeros}")

print(f"numeros[1:4]: {numeros[1:4]}")      # [1, 2, 3]
print(f"numeros[:3]: {numeros[:3]}")        # [0, 1, 2] (desde el inicio)
print(f"numeros[3:]: {numeros[3:]}")        # [3, 4, 5] (hasta el final)
print(f"numeros[:]: {numeros[:]}")          # [0, 1, 2, 3, 4, 5] (copia completa)
print(f"numeros[::2]: {numeros[::2]}")      # [0, 2, 4] (cada 2 elementos)
print(f"numeros[::-1]: {numeros[::-1]}")    # [5, 4, 3, 2, 1, 0] (inversa)

print("\n" + "="*50 + "\n")

# ===== MÉTODOS ÚTILES =====
print("=== Métodos Útiles ===")
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista: {numeros}")

print(f"Longitud (len): {len(numeros)}")
print(f"Suma: {sum(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")

# count() - Contar ocurrencias
print(f"Cuántas veces aparece 1: {numeros.count(1)}")

# index() - Encontrar índice de elemento
print(f"Índice del primer 4: {numeros.index(4)}")

# sort() - Ordenar (modifica la lista)
numeros_copia = numeros.copy()
numeros_copia.sort()
print(f"Después de sort(): {numeros_copia}")

# reverse() - Invertir orden
numeros_copia.reverse()
print(f"Después de reverse(): {numeros_copia}")

print("\n" + "="*50 + "\n")

# ===== LISTAS ANIDADAS =====
print("=== Listas Anidadas ===")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 3x3:")
for fila in matriz:
    print(fila)

print(f"\nElemento en [1][2]: {matriz[1][2]}")  # 6

