"""
Sets (Conjuntos) en Python

Este archivo muestra cómo trabajar con sets en Python.
Los sets almacenan elementos únicos (sin duplicados) y no tienen orden.
"""

# ===== CREAR SETS =====
print("=== Crear Sets ===")
# Usando llaves {}
numeros = {1, 2, 3, 4, 5}
colores = {"rojo", "verde", "azul"}

# Desde una lista (elimina duplicados automáticamente)
lista_con_duplicados = [1, 2, 2, 3, 3, 4, 5]
numeros_unicos = set(lista_con_duplicados)

# Set vacío (usar set(), no {})
vacio = set()

print(f"Números: {numeros}")
print(f"Colores: {colores}")
print(f"Lista original: {lista_con_duplicados}")
print(f"Set sin duplicados: {numeros_unicos}")
print(f"Vacío: {vacio}")

print("\n" + "="*50 + "\n")

# ===== AGREGAR Y ELIMINAR ELEMENTOS =====
print("=== Agregar y Eliminar Elementos ===")
colores = {"rojo", "verde", "azul"}
print(f"Original: {colores}")

# add() - Agregar un elemento
colores.add("amarillo")
print(f"Después de add('amarillo'): {colores}")

# update() - Agregar múltiples elementos
colores.update(["naranja", "morado"])
print(f"Después de update(['naranja', 'morado']): {colores}")

# remove() - Eliminar elemento (error si no existe)
colores.remove("azul")
print(f"Después de remove('azul'): {colores}")

# discard() - Eliminar elemento (no da error si no existe)
colores.discard("verde")
colores.discard("rosa")  # No da error aunque no existe
print(f"Después de discard('verde') y discard('rosa'): {colores}")

# pop() - Elimina y devuelve un elemento aleatorio
elemento = colores.pop()
print(f"Elemento eliminado con pop(): {elemento}")
print(f"Después de pop(): {colores}")

# clear() - Vaciar el set
colores.clear()
print(f"Después de clear(): {colores}")

print("\n" + "="*50 + "\n")

# ===== OPERACIONES DE CONJUNTOS =====
print("=== Operaciones de Conjuntos ===")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set1: {set1}")
print(f"Set2: {set2}")

# Unión (elementos en cualquiera de los dos sets)
union = set1.union(set2)
print(f"Unión (set1 | set2): {union}")

# Intersección (elementos en ambos sets)
interseccion = set1.intersection(set2)
print(f"Intersección (set1 & set2): {interseccion}")

# Diferencia (elementos en set1 pero no en set2)
diferencia = set1.difference(set2)
print(f"Diferencia (set1 - set2): {diferencia}")

# Diferencia simétrica (elementos en uno u otro, pero no en ambos)
diferencia_simetrica = set1.symmetric_difference(set2)
print(f"Diferencia simétrica (set1 ^ set2): {diferencia_simetrica}")

print("\n" + "="*50 + "\n")

# ===== VERIFICAR RELACIONES =====
print("=== Verificar Relaciones ===")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Set3: {set3}")

# issubset() - ¿set1 es subconjunto de set2?
print(f"set1 es subconjunto de set2: {set1.issubset(set2)}")
print(f"set1 <= set2: {set1 <= set2}")

# issuperset() - ¿set2 es superconjunto de set1?
print(f"set2 es superconjunto de set1: {set2.issuperset(set1)}")
print(f"set2 >= set1: {set2 >= set1}")

# isdisjoint() - ¿No tienen elementos en común?
print(f"set1 y set3 son disjuntos: {set1.isdisjoint(set3)}")

print("\n" + "="*50 + "\n")

# ===== ITERAR SOBRE SETS =====
print("=== Iterar sobre Sets ===")
colores = {"rojo", "verde", "azul", "amarillo"}

print("Elementos del set:")
for color in colores:
    print(f"  {color}")

print("\n" + "="*50 + "\n")

# ===== VERIFICAR MEMBRESÍA =====
print("=== Verificar Membresía ===")
colores = {"rojo", "verde", "azul"}

print(f"Colores: {colores}")
print(f"'rojo' in colores: {'rojo' in colores}")
print(f"'amarillo' in colores: {'amarillo' in colores}")
print(f"'verde' not in colores: {'verde' not in colores}")

print("\n" + "="*50 + "\n")

# ===== EJEMPLOS PRÁCTICOS =====
print("=== Ejemplo Práctico: Eliminar Duplicados ===")
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista original: {lista_con_duplicados}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")

print("\n" + "="*50 + "\n")

print("=== Ejemplo Práctico: Votación ===")
votos = ["A", "B", "A", "C", "B", "A", "A", "C"]
votos_unicos = set(votos)
print(f"Votos: {votos}")
print(f"Candidatos únicos: {votos_unicos}")
for candidato in votos_unicos:
    cantidad = votos.count(candidato)
    print(f"  {candidato}: {cantidad} votos")

print("\n" + "="*50 + "\n")

print("=== Ejemplo Práctico: Amigos en Común ===")
amigos_ana = {"Juan", "María", "Carlos", "Pedro"}
amigos_carlos = {"Carlos", "Pedro", "Ana", "Luis"}

amigos_comunes = amigos_ana.intersection(amigos_carlos)
solo_ana = amigos_ana.difference(amigos_carlos)
todos_los_amigos = amigos_ana.union(amigos_carlos)

print(f"Amigos de Ana: {amigos_ana}")
print(f"Amigos de Carlos: {amigos_carlos}")
print(f"Amigos en común: {amigos_comunes}")
print(f"Solo amigos de Ana: {solo_ana}")
print(f"Todos los amigos: {todos_los_amigos}")

