# Respuestas - Estructuras de Control

## Ejercicio 1: If-Else Básico

```python
# Solución
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
```

**Explicación**: El operador `%` (módulo) devuelve el resto de la división. Si un número dividido entre 2 tiene resto 0, es par; de lo contrario, es impar.

---

## Ejercicio 2: If-Elif-Else

```python
# Solución
edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Menor de edad")
elif edad <= 65:
    print("Adulto")
else:
    print("Adulto mayor")
```

**Explicación**: `elif` permite encadenar múltiples condiciones. Se evalúan en orden y solo se ejecuta el bloque de la primera condición verdadera.

---

## Ejercicio 3: Bucle For - Rango

```python
# Solución
for i in range(1, 11):
    print(i)
```

**Explicación**: `range(1, 11)` genera números del 1 al 10 (el segundo parámetro es exclusivo). También podríamos usar `range(1, 11, 1)` para ser explícitos sobre el paso.

---

## Ejercicio 4: Bucle For - Lista

```python
# Solución
frutas = ["manzana", "banana", "naranja"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
```

**Explicación**: `enumerate()` devuelve tanto el índice como el valor de cada elemento. Es más eficiente que usar `range(len(frutas))`.

---

## Ejercicio 5: Bucle While

```python
# Solución
suma = 0
numero = float(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = float(input("Ingresa otro número (0 para terminar): "))

print(f"La suma total es: {suma}")
```

**Explicación**: El bucle `while` se ejecuta mientras la condición sea verdadera. Aquí se repite hasta que el usuario ingrese 0. El operador `+=` es equivalente a `suma = suma + numero`.

---

## Ejercicio 6: Bucle While con Contador

```python
# Solución
limite = int(input("Ingresa un número límite: "))
contador = 1

while contador <= limite:
    print(contador)
    contador += 1
```

**Explicación**: Usamos un contador que se incrementa en cada iteración. Es importante incrementar el contador dentro del bucle para evitar un bucle infinito.

---

## Ejercicio 7: Break

```python
# Solución
while True:
    numero = float(input("Ingresa un número (negativo para salir): "))
    
    if numero < 0:
        print("Número negativo detectado. Saliendo...")
        break
    
    print(f"Has ingresado: {numero}")
```

**Explicación**: `break` termina inmediatamente el bucle más cercano. `while True` crea un bucle infinito que solo se detiene con `break`.

---

## Ejercicio 8: Continue

```python
# Solución
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
```

**Explicación**: `continue` salta el resto de la iteración actual y pasa a la siguiente. Aquí, cuando el número es múltiplo de 3, se omite y no se imprime.

---

## Ejercicio 9: Bucles Anidados

```python
# Solución
for i in range(1, 6):
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  # Línea en blanco entre tablas
```

**Explicación**: Los bucles anidados permiten iterar sobre múltiples dimensiones. El bucle externo controla las filas (tablas) y el interno las columnas (multiplicaciones).

---

## Ejercicio 10: Estructuras Combinadas

```python
# Solución
lista_resultado = []

while True:
    entrada = input("Ingresa un número o 'salir' para terminar: ")
    
    if entrada.lower() == "salir":
        break
    
    try:
        numero = int(entrada)
        
        if numero % 2 == 0:
            lista_resultado.append(numero)
        else:
            lista_resultado.append(numero * 2)
    except ValueError:
        print("Por favor, ingresa un número válido o 'salir'")

print(f"Lista resultante: {lista_resultado}")
```

**Explicación**: 
- Combinamos `while`, `if-else`, y manejo de errores con `try-except`
- `.lower()` convierte la entrada a minúsculas para comparación
- `try-except` maneja errores si el usuario ingresa algo que no es un número
- `.append()` agrega elementos a la lista
