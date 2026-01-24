# Respuestas - Conceptos Básicos

## Ejercicio 1: Variables y Tipos de Datos

```python
# Solución
nombre = "Juan"  # string
edad = 25        # int
altura = 1.75    # float
tiene_mascota = True  # bool

print(f"Nombre: {nombre}, Tipo: {type(nombre)}")
print(f"Edad: {edad}, Tipo: {type(edad)}")
print(f"Altura: {altura}, Tipo: {type(altura)}")
print(f"Tiene mascota: {tiene_mascota}, Tipo: {type(tiene_mascota)}")
```

**Explicación**: En Python, no necesitamos declarar el tipo de variable explícitamente. El tipo se infiere automáticamente del valor asignado. Podemos verificar el tipo usando la función `type()`.

---

## Ejercicio 2: Operadores Aritméticos

```python
# Solución
a = 10
b = 3

suma = a + b              # 13
resta = a - b             # 7
multiplicacion = a * b    # 30
division = a / b          # 3.333...
division_entera = a // b  # 3
modulo = a % b            # 1
potencia = a ** b         # 1000

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")
```

**Explicación**: 
- `/` siempre devuelve un float
- `//` devuelve la parte entera de la división
- `%` devuelve el resto de la división
- `**` es el operador de exponenciación

---

## Ejercicio 3: Operadores de Comparación

```python
# Solución
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

son_iguales = num1 == num2
primero_mayor = num1 > num2
primero_menor_igual = num1 <= num2

print(f"¿Son iguales? {son_iguales}")
print(f"¿El primero es mayor? {primero_mayor}")
print(f"¿El primero es menor o igual? {primero_menor_igual}")
```

**Explicación**: Los operadores de comparación devuelven valores booleanos (`True` o `False`). Usamos `float()` para convertir la entrada del usuario a número decimal.

---

## Ejercicio 4: Operadores Lógicos

```python
# Solución
numero = float(input("Ingresa un número: "))

esta_en_rango = numero >= 10 and numero <= 50

print(f"¿El número está entre 10 y 50? {esta_en_rango}")
```

**Explicación**: El operador `and` devuelve `True` solo si ambas condiciones son verdaderas. También podríamos usar `10 <= numero <= 50` que es más "pythónico".

---

## Ejercicio 5: Trabajo con Strings

```python
# Solución
texto = "Python es genial"

longitud = len(texto)
mayusculas = texto.upper()
minusculas = texto.lower()
reemplazado = texto.replace("genial", "increíble")
contiene_python = "Python" in texto

print(f"Longitud: {longitud}")
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")
print(f"Reemplazado: {reemplazado}")
print(f"¿Contiene 'Python'? {contiene_python}")
```

**Explicación**: 
- `len()` devuelve la cantidad de caracteres
- `.upper()` y `.lower()` convierten el caso
- `.replace()` reemplaza subcadenas
- `in` verifica si una subcadena está contenida

---

## Ejercicio 6: F-strings

```python
# Solución
nombre = "María"
edad = 30
resultado = 15 * 3
precio = 100.50

# F-strings permiten insertar variables y expresiones
mensaje1 = f"Mi nombre es {nombre} y tengo {edad} años"
mensaje2 = f"El resultado de 15 * 3 es {resultado}"
mensaje3 = f"El precio es ${precio:.2f}"

print(mensaje1)
print(mensaje2)
print(mensaje3)
```

**Explicación**: Los f-strings (formatted string literals) permiten insertar variables y expresiones dentro de cadenas usando `{}`. El formato `.2f` muestra el número con 2 decimales.

---

## Ejercicio 7: Entrada y Salida

```python
# Solución
nombre = input("¿Cuál es tu nombre? ")
año_nacimiento = int(input("¿En qué año naciste? "))
año_actual = 2024  # O usar: from datetime import datetime; año_actual = datetime.now().year

edad = año_actual - año_nacimiento

print(f"¡Hola {nombre}! Tienes {edad} años.")
print(f"Es un placer conocerte, {nombre}.")
```

**Explicación**: 
- `input()` pausa la ejecución y espera que el usuario ingrese texto
- `int()` convierte el string a número entero
- Podemos combinar `input()` con `int()` o `float()` para obtener números directamente
