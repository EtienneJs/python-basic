"""
Tuplas en Python

Este archivo muestra cómo trabajar con tuplas en Python.
Las tuplas son inmutables (no se pueden modificar después de crearlas).
"""

# ===== CREAR TUPLAS =====
print("=== Crear Tuplas ===")
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")

# Tupla de un solo elemento (necesita coma)
tupla_simple = (5,)  # Nota la coma
numero = (5)  # Esto NO es una tupla, es un int

# Sin paréntesis también funciona
otra_tupla = 1, 2, 3

print(f"Coordenadas: {coordenadas}")
print(f"Colores: {colores}")
print(f"Tupla simple: {tupla_simple}")
print(f"Otra tupla: {otra_tupla}")

print("\n" + "="*50 + "\n")

# ===== ACCEDER A ELEMENTOS =====
print("=== Acceder a Elementos ===")
coordenadas = (10, 20, 30)
colores = ("rojo", "verde", "azul", "amarillo")

print(f"Coordenadas: {coordenadas}")
print(f"Primer elemento [0]: {coordenadas[0]}")      # 10
print(f"Último elemento [-1]: {coordenadas[-1]}")    # 30
print(f"Segundo elemento [1]: {coordenadas[1]}")     # 20

print(f"\nColores: {colores}")
print(f"Subtupla [1:3]: {colores[1:3]}")  # ("verde", "azul")

print("\n" + "="*50 + "\n")

# ===== DESEMPAQUETADO =====
print("=== Desempaquetado ===")
coordenadas = (10, 20)

# Desempaquetar en variables
x, y = coordenadas
print(f"Coordenadas: {coordenadas}")
print(f"x: {x}, y: {y}")

# Múltiples valores
colores = ("rojo", "verde", "azul")
color1, color2, color3 = colores
print(f"\nColores: {colores}")
print(f"color1: {color1}, color2: {color2}, color3: {color3}")

# Intercambiar valores fácilmente
a = 5
b = 10
print(f"\nAntes: a={a}, b={b}")
a, b = b, a  # Intercambio
print(f"Después: a={a}, b={b}")

print("\n" + "="*50 + "\n")

# ===== TUPLAS SON INMUTABLES =====
print("=== Tuplas son Inmutables ===")
colores = ("rojo", "verde", "azul")
print(f"Tupla original: {colores}")

# Esto causaría un error (descomenta para ver el error):
# colores[0] = "amarillo"  # TypeError: 'tuple' object does not support item assignment

# Pero puedes crear una nueva tupla
nuevos_colores = ("amarillo",) + colores[1:]
print(f"Nueva tupla: {nuevos_colores}")

print("\n" + "="*50 + "\n")

# ===== MÉTODOS DE TUPLAS =====
print("=== Métodos de Tuplas ===")
numeros = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla: {numeros}")

# count() - Contar ocurrencias
print(f"Cuántas veces aparece 2: {numeros.count(2)}")

# index() - Encontrar índice de elemento
print(f"Índice del primer 3: {numeros.index(3)}")

# Longitud
print(f"Longitud: {len(numeros)}")

# Verificar si existe elemento
print(f"5 in numeros: {5 in numeros}")
print(f"10 in numeros: {10 in numeros}")

print("\n" + "="*50 + "\n")

# ===== TUPLAS COMO CLAVES DE DICCIONARIOS =====
print("=== Tuplas como Claves de Diccionarios ===")
# Las tuplas pueden usarse como claves porque son inmutables
coordenadas_puntos = {
    (0, 0): "Origen",
    (1, 2): "Punto A",
    (3, 4): "Punto B"
}

print("Diccionario con tuplas como claves:")
for punto, nombre in coordenadas_puntos.items():
    print(f"  {punto}: {nombre}")

print(f"\nValor en (1, 2): {coordenadas_puntos[(1, 2)]}")

print("\n" + "="*50 + "\n")

# ===== TUPLAS VS LISTAS =====
print("=== Tuplas vs Listas ===")
# Tupla (inmutable, más rápida, usa menos memoria)
tupla = (1, 2, 3)

# Lista (mutable, más flexible)
lista = [1, 2, 3]

print(f"Tupla: {tupla} (no se puede modificar)")
print(f"Lista: {lista} (se puede modificar)")

# Convertir entre tupla y lista
lista_de_tupla = list(tupla)
tupla_de_lista = tuple(lista)

print(f"\nLista de tupla: {lista_de_tupla}")
print(f"Tupla de lista: {tupla_de_lista}")

print("\n" + "="*50 + "\n")

# ===== EJEMPLO PRÁCTICO =====
print("=== Ejemplo Práctico: Coordenadas ===")
def calcular_distancia(punto1, punto2):
    """Calcula la distancia entre dos puntos"""
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distancia

punto_a = (0, 0)
punto_b = (3, 4)

distancia = calcular_distancia(punto_a, punto_b)
print(f"Distancia entre {punto_a} y {punto_b}: {distancia:.2f}")

