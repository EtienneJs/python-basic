"""
Break y Continue en Python

Este archivo muestra cómo usar break y continue para controlar bucles.
"""

# ===== BREAK: SALIR DEL BUCLE =====
print("=== Break: Salir del Bucle ===")
print("For con break (sale cuando i == 5):")

for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i, end=" ")
print("\n")

print("\n" + "="*50 + "\n")

# ===== CONTINUE: SALTAR ITERACIÓN =====
print("=== Continue: Saltar Iteración ===")
print("For con continue (salta números pares):")

for i in range(10):
    if i % 2 == 0:
        continue  # Salta números pares
    print(i, end=" ")  # Solo imprime impares
print("\n")

print("\n" + "="*50 + "\n")

# ===== EJEMPLO: BUSCAR EN LISTA =====
print("=== Ejemplo: Buscar en Lista ===")
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
numero_buscado = 7

print(f"Buscando {numero_buscado} en la lista...")
for numero in numeros:
    print(f"Revisando {numero}...")
    if numero == numero_buscado:
        print(f"¡Encontrado! {numero_buscado}")
        break
else:
    # Este else se ejecuta si el bucle termina sin break
    print(f"{numero_buscado} no encontrado")

print("\n" + "="*50 + "\n")

# ===== EJEMPLO: FILTRAR NÚMEROS =====
print("=== Ejemplo: Filtrar Números ===")
print("Imprimir números del 1 al 20, pero saltar los múltiplos de 3:")

for i in range(1, 21):
    if i % 3 == 0:
        continue  # Salta múltiplos de 3
    print(i, end=" ")
print("\n")

print("\n" + "="*50 + "\n")

# ===== BREAK EN WHILE =====
print("=== Break en While ===")
contador = 0

while contador < 100:
    contador += 1
    if contador > 5:
        break  # Sale cuando contador > 5
    print(f"Contador: {contador}")

print("\n" + "="*50 + "\n")

# ===== CONTINUE EN WHILE =====
print("=== Continue en While ===")
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Salta números pares
    print(f"Contador impar: {contador}")

print("\n" + "="*50 + "\n")

# ===== BREAK Y CONTINUE EN BUCLES ANIDADOS =====
print("=== Break y Continue en Bucles Anidados ===")
print("Buscar el primer número par en cada fila:")

matriz = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 9, 11]
]

for fila in matriz:
    for numero in fila:
        if numero % 2 == 0:
            print(f"Encontrado número par: {numero}")
            break  # Solo sale del bucle interno
    else:
        print("No hay números pares en esta fila")

