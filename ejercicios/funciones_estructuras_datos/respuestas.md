# Respuestas - Funciones y Estructuras de Datos

## Ejercicio 1: Función Básica

```python
# Solución
def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido."

# Uso
mensaje = saludar("Ana")
print(mensaje)
```

**Explicación**: Las funciones se definen con `def`. El `return` devuelve un valor. Si no hay `return`, la función devuelve `None`.

---

## Ejercicio 2: Función con Múltiples Parámetros

```python
# Solución
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Uso
area = calcular_area_rectangulo(5, 3)
print(f"El área es: {area}")
```

**Explicación**: Las funciones pueden recibir múltiples parámetros separados por comas. El orden importa a menos que uses argumentos con nombre.

---

## Ejercicio 3: Función con Valor por Defecto

```python
# Solución
def potencia(base, exponente=2):
    return base ** exponente

# Uso
print(potencia(3))        # 9 (usa el valor por defecto)
print(potencia(3, 4))     # 81 (usa el exponente proporcionado)
```

**Explicación**: Los parámetros con valor por defecto deben ir después de los parámetros sin valor por defecto. Permiten llamar la función con menos argumentos.

---

## Ejercicio 4: Función que Devuelve Múltiples Valores

```python
# Solución
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

# Uso
s, r, m, d = operaciones(10, 5)
print(f"Suma: {s}, Resta: {r}, Multiplicación: {m}, División: {d}")
```

**Explicación**: Python permite devolver múltiples valores usando tuplas. Se pueden desempaquetar en variables separadas o recibir como una tupla.

---

## Ejercicio 5: Trabajo con Listas

```python
# Solución
numeros = [5, 2, 8, 1, 9, 3]

# Ordenar (modifica la lista original)
numeros.sort()
print(f"Ordenada: {numeros}")

# O sin modificar la original
numeros_ordenados = sorted(numeros)

# Mayor y menor
mayor = max(numeros)
menor = min(numeros)
print(f"Mayor: {mayor}, Menor: {menor}")

# Suma
suma_total = sum(numeros)
print(f"Suma total: {suma_total}")

# Agregar al final
numeros.append(10)
print(f"Con 10 agregado: {numeros}")
```

**Explicación**: 
- `.sort()` modifica la lista original
- `sorted()` devuelve una nueva lista ordenada
- `max()`, `min()`, `sum()` son funciones built-in
- `.append()` agrega un elemento al final

---

## Ejercicio 6: Listas - Slicing

```python
# Solución
letras = ['a', 'b', 'c', 'd', 'e', 'f']

primeros_tres = letras[:3]        # ['a', 'b', 'c']
ultimos_dos = letras[-2:]         # ['e', 'f']
del_medio = letras[2:5]           # ['c', 'd', 'e']
invertida = letras[::-1]          # ['f', 'e', 'd', 'c', 'b', 'a']

print(f"Primeros 3: {primeros_tres}")
print(f"Últimos 2: {ultimos_dos}")
print(f"Del medio: {del_medio}")
print(f"Invertida: {invertida}")
```

**Explicación**: El slicing usa la sintaxis `[inicio:fin:paso]`. Los índices negativos cuentan desde el final. `[::-1]` invierte la lista.

---

## Ejercicio 7: Diccionarios

```python
# Solución
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Madrid"
}

# Mostrar valores
print(f"Valores: {persona.values()}")
print(f"Claves: {persona.keys()}")
print(f"Items: {persona.items()}")

# Agregar nueva clave
persona["profesion"] = "Ingeniero"
print(f"Con profesión: {persona}")

# Modificar valor
persona["edad"] = 29
print(f"Edad actualizada: {persona}")

# Eliminar clave
del persona["ciudad"]
# O: persona.pop("ciudad")
print(f"Sin ciudad: {persona}")
```

**Explicación**: Los diccionarios almacenan pares clave-valor. Se accede con `[]` o `.get()`. `del` elimina una clave, y `.pop()` también elimina pero devuelve el valor.

---

## Ejercicio 8: Diccionarios Anidados

```python
# Solución
estudiantes = {
    "estudiante1": {
        "nombre": "Laura",
        "edad": 20,
        "calificaciones": [85, 90, 88]
    },
    "estudiante2": {
        "nombre": "Pedro",
        "edad": 21,
        "calificaciones": [92, 87, 95]
    }
}

# Acceder a información
print(estudiantes["estudiante1"]["nombre"])
print(estudiantes["estudiante2"]["calificaciones"])

# Calcular promedio de calificaciones
for clave, info in estudiantes.items():
    promedio = sum(info["calificaciones"]) / len(info["calificaciones"])
    print(f"{info['nombre']}: Promedio = {promedio:.2f}")
```

**Explicación**: Los diccionarios pueden contener otros diccionarios, listas, o cualquier tipo de dato. Se accede con múltiples `[]` o usando `.get()` para evitar errores.

---

## Ejercicio 9: Tuplas

```python
# Solución
coordenadas = (10, 20, 30)

# Desempaquetar
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}")

# Intentar modificar (genera error)
# coordenadas[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Convertir a lista, modificar, y volver a tupla
lista_coords = list(coordenadas)
lista_coords[0] = 15
nuevas_coords = tuple(lista_coords)
print(f"Nuevas coordenadas: {nuevas_coords}")
```

**Explicación**: Las tuplas son inmutables (no se pueden modificar después de crearlas). Son útiles para datos que no deben cambiar. Se pueden convertir a lista, modificar, y volver a convertir.

---

## Ejercicio 10: Sets

```python
# Solución
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2  # O: set1.union(set2)
interseccion = set1 & set2  # O: set1.intersection(set2)
diferencia = set1 - set2  # O: set1.difference(set2)
diferencia_simetrica = set1 ^ set2  # O: set1.symmetric_difference(set2)

print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia: {diferencia}")
print(f"Diferencia simétrica: {diferencia_simetrica}")
```

**Explicación**: Los sets almacenan elementos únicos. Los operadores `|`, `&`, `-`, `^` realizan operaciones de conjuntos. También existen métodos equivalentes.

---

## Ejercicio 11: Función con Lista

```python
# Solución
def filtrar_pares(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares

# Versión más "pythónica" con list comprehension
def filtrar_pares_v2(numeros):
    return [num for num in numeros if num % 2 == 0]

# Uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(lista)
print(f"Números pares: {pares}")
```

**Explicación**: Las list comprehensions son una forma concisa de crear listas. La sintaxis `[expresión for elemento in iterable if condición]` es muy común en Python.

---

## Ejercicio 12: Función con Diccionario

```python
# Solución
def producto_mas_caro(productos):
    if not productos:
        return None
    
    producto_caro = max(productos, key=productos.get)
    precio = productos[producto_caro]
    return producto_caro, precio

# Uso
tienda = {
    "laptop": 1200,
    "mouse": 25,
    "teclado": 80,
    "monitor": 300
}

producto, precio = producto_mas_caro(tienda)
print(f"El producto más caro es {producto} con un precio de ${precio}")
```

**Explicación**: `max()` puede recibir un parámetro `key` que especifica cómo comparar los elementos. `productos.get` es una función que obtiene el valor (precio) de cada clave.
