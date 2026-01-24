# Respuestas - Ejemplos Prácticos

## Ejercicio 1: Calculadora Mejorada

```python
# Solución
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora():
    while True:
        print("\n=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == "1":
                    resultado = sumar(num1, num2)
                elif opcion == "2":
                    resultado = restar(num1, num2)
                elif opcion == "3":
                    resultado = multiplicar(num1, num2)
                elif opcion == "4":
                    resultado = dividir(num1, num2)
                
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Error: Por favor ingresa números válidos")
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar
calculadora()
```

**Explicación**: Este ejemplo combina funciones, estructuras de control, manejo de errores y un bucle principal. Usa `try-except` para manejar entradas inválidas.

---

## Ejercicio 2: Lista de Tareas Mejorada

```python
# Solución
import json
import os

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"pendientes": [], "completadas": []}

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)

def mostrar_tareas(tareas):
    print("\n=== Tareas Pendientes ===")
    if tareas["pendientes"]:
        for i, tarea in enumerate(tareas["pendientes"], 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes")
    
    print("\n=== Tareas Completadas ===")
    if tareas["completadas"]:
        for i, tarea in enumerate(tareas["completadas"], 1):
            print(f"{i}. ✓ {tarea}")
    else:
        print("No hay tareas completadas")

def agregar_tarea(tareas):
    tarea = input("Ingresa la nueva tarea: ")
    tareas["pendientes"].append(tarea)
    print("Tarea agregada exitosamente")

def completar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("\nIngresa el número de la tarea a completar: ")) - 1
        if 0 <= indice < len(tareas["pendientes"]):
            tarea = tareas["pendientes"].pop(indice)
            tareas["completadas"].append(tarea)
            print("Tarea marcada como completada")
        else:
            print("Número inválido")
    except ValueError:
        print("Por favor ingresa un número válido")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    tipo = input("¿Eliminar de pendientes (p) o completadas (c)? ").lower()
    try:
        indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
        if tipo == "p" and 0 <= indice < len(tareas["pendientes"]):
            tareas["pendientes"].pop(indice)
            print("Tarea eliminada")
        elif tipo == "c" and 0 <= indice < len(tareas["completadas"]):
            tareas["completadas"].pop(indice)
            print("Tarea eliminada")
        else:
            print("Número o tipo inválido")
    except ValueError:
        print("Por favor ingresa un número válido")

def main():
    tareas = cargar_tareas()
    
    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print("Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
```

**Explicación**: Este ejemplo muestra persistencia de datos usando JSON, manejo de archivos, y una estructura más compleja. Las tareas se guardan entre ejecuciones.

---

## Ejercicio 3: Contador de Palabras Avanzado

```python
# Solución
import string
from collections import Counter

def limpiar_texto(texto):
    # Eliminar puntuación y convertir a minúsculas
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    return texto

def analizar_texto(texto):
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    
    if not palabras:
        return None
    
    total_palabras = len(palabras)
    palabras_unicas = len(set(palabras))
    longitud_promedio = sum(len(p) for p in palabras) / total_palabras
    
    # Contar frecuencia de palabras
    contador = Counter(palabras)
    palabra_mas_frecuente = contador.most_common(1)[0]
    
    return {
        "total": total_palabras,
        "unicas": palabras_unicas,
        "promedio_longitud": longitud_promedio,
        "mas_frecuente": palabra_mas_frecuente[0],
        "frecuencia": palabra_mas_frecuente[1],
        "top_5": contador.most_common(5)
    }

def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            texto = f.read()
        return analizar_texto(texto)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return None

def main():
    print("=== Analizador de Texto ===")
    print("1. Analizar texto ingresado")
    print("2. Analizar archivo")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("Ingresa el texto (presiona Enter dos veces para terminar):")
        lineas = []
        while True:
            linea = input()
            if linea == "":
                break
            lineas.append(linea)
        texto = "\n".join(lineas)
        estadisticas = analizar_texto(texto)
    elif opcion == "2":
        archivo = input("Ingresa el nombre del archivo: ")
        estadisticas = analizar_archivo(archivo)
    else:
        print("Opción inválida")
        return
    
    if estadisticas:
        print("\n=== Estadísticas ===")
        print(f"Total de palabras: {estadisticas['total']}")
        print(f"Palabras únicas: {estadisticas['unicas']}")
        print(f"Longitud promedio: {estadisticas['promedio_longitud']:.2f} caracteres")
        print(f"Palabra más frecuente: '{estadisticas['mas_frecuente']}' ({estadisticas['frecuencia']} veces)")
        print("\nTop 5 palabras más frecuentes:")
        for palabra, frecuencia in estadisticas['top_5']:
            print(f"  {palabra}: {frecuencia} veces")

if __name__ == "__main__":
    main()
```

**Explicación**: Usa `Counter` de `collections` para contar frecuencias eficientemente. Muestra manejo de strings, listas, y análisis de datos.

---

## Ejercicio 4: Gestor de Contactos

```python
# Solución
import json
import os

ARCHIVO_CONTACTOS = "contactos.json"

def cargar_contactos():
    if os.path.exists(ARCHIVO_CONTACTOS):
        with open(ARCHIVO_CONTACTOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def guardar_contactos(contactos):
    with open(ARCHIVO_CONTACTOS, 'w', encoding='utf-8') as f:
        json.dump(contactos, f, ensure_ascii=False, indent=2)

def agregar_contacto(contactos):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    
    contactos[nombre] = {
        "telefono": telefono,
        "email": email
    }
    print(f"Contacto '{nombre}' agregado exitosamente")

def buscar_contacto(contactos):
    nombre = input("Ingresa el nombre a buscar: ")
    if nombre in contactos:
        info = contactos[nombre]
        print(f"\nNombre: {nombre}")
        print(f"Teléfono: {info['telefono']}")
        print(f"Email: {info['email']}")
    else:
        print(f"No se encontró el contacto '{nombre}'")

def mostrar_todos(contactos):
    if not contactos:
        print("No hay contactos guardados")
        return
    
    print("\n=== Todos los Contactos ===")
    for nombre, info in contactos.items():
        print(f"\n{nombre}:")
        print(f"  Teléfono: {info['telefono']}")
        print(f"  Email: {info['email']}")

def eliminar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado")
    else:
        print(f"No se encontró el contacto '{nombre}'")

def main():
    contactos = cargar_contactos()
    
    while True:
        print("\n=== Gestor de Contactos ===")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            mostrar_todos(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            guardar_contactos(contactos)
            print("Contactos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
```

**Explicación**: Similar al gestor de tareas pero usando diccionarios anidados. Muestra cómo estructurar datos más complejos.

---

## Ejercicio 5: Juego de Adivinanza

```python
# Solución
import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    
    print("¡Bienvenido al juego de adivinanza!")
    print("He pensado en un número entre 1 y 100")
    print(f"Tienes {max_intentos} intentos")
    
    while intentos < max_intentos:
        try:
            intento = int(input(f"\nIntento {intentos + 1}: Ingresa tu número: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("El número es mayor")
            elif intento > numero_secreto:
                print("El número es menor")
            else:
                print(f"¡Felicidades! Adivinaste en {intentos} intentos")
                return True
        except ValueError:
            print("Por favor ingresa un número válido")
    
    print(f"\n¡Se acabaron los intentos! El número era {numero_secreto}")
    return False

def main():
    while True:
        jugar()
        continuar = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if continuar != 's':
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
```

**Explicación**: Usa `random.randint()` para generar números aleatorios. Combina bucles, condicionales y manejo de entrada.

---

## Ejercicio 6: Análisis de Notas

```python
# Solución
def ingresar_estudiantes():
    estudiantes = {}
    
    while True:
        nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        
        notas = []
        print(f"Ingresa las notas de {nombre} (o 'fin' para terminar):")
        while True:
            entrada = input("Nota: ")
            if entrada.lower() == 'fin':
                break
            try:
                nota = float(entrada)
                if 0 <= nota <= 100:
                    notas.append(nota)
                else:
                    print("La nota debe estar entre 0 y 100")
            except ValueError:
                print("Por favor ingresa un número válido")
        
        if notas:
            estudiantes[nombre] = notas
    
    return estudiantes

def analizar_notas(estudiantes):
    if not estudiantes:
        print("No hay estudiantes para analizar")
        return
    
    print("\n=== Análisis de Notas ===")
    aprobados = 0
    todas_las_notas = []
    
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        todas_las_notas.extend(notas)
        estado = "Aprobado" if promedio >= 70 else "Reprobado"
        
        if promedio >= 70:
            aprobados += 1
        
        print(f"\n{nombre}:")
        print(f"  Notas: {notas}")
        print(f"  Promedio: {promedio:.2f}")
        print(f"  Estado: {estado}")
    
    if todas_las_notas:
        promedio_grupo = sum(todas_las_notas) / len(todas_las_notas)
        print(f"\n=== Estadísticas Generales ===")
        print(f"Promedio del grupo: {promedio_grupo:.2f}")
        print(f"Estudiantes aprobados: {aprobados}/{len(estudiantes)}")
        print(f"Porcentaje de aprobación: {(aprobados/len(estudiantes)*100):.2f}%")

def main():
    estudiantes = ingresar_estudiantes()
    analizar_notas(estudiantes)

if __name__ == "__main__":
    main()
```

**Explicación**: Muestra cómo trabajar con diccionarios que contienen listas, cálculos estadísticos básicos, y procesamiento de datos.

---

## Ejercicio 7: Conversor de Unidades

```python
# Solución
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def metros_a_pies(metros):
    return metros * 3.28084

def pies_a_metros(pies):
    return pies / 3.28084

def kilogramos_a_libras(kg):
    return kg * 2.20462

def libras_a_kilogramos(lb):
    return lb / 2.20462

def menu_temperatura():
    print("\n1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Selecciona: ")
    try:
        valor = float(input("Ingresa el valor: "))
        if opcion == "1":
            resultado = celsius_a_fahrenheit(valor)
            print(f"{valor}°C = {resultado:.2f}°F")
        elif opcion == "2":
            resultado = fahrenheit_a_celsius(valor)
            print(f"{valor}°F = {resultado:.2f}°C")
        else:
            print("Opción inválida")
    except ValueError:
        print("Por favor ingresa un número válido")

def menu_longitud():
    print("\n1. Metros a Pies")
    print("2. Pies a Metros")
    opcion = input("Selecciona: ")
    try:
        valor = float(input("Ingresa el valor: "))
        if opcion == "1":
            resultado = metros_a_pies(valor)
            print(f"{valor} m = {resultado:.2f} ft")
        elif opcion == "2":
            resultado = pies_a_metros(valor)
            print(f"{valor} ft = {resultado:.2f} m")
        else:
            print("Opción inválida")
    except ValueError:
        print("Por favor ingresa un número válido")

def menu_peso():
    print("\n1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    opcion = input("Selecciona: ")
    try:
        valor = float(input("Ingresa el valor: "))
        if opcion == "1":
            resultado = kilogramos_a_libras(valor)
            print(f"{valor} kg = {resultado:.2f} lb")
        elif opcion == "2":
            resultado = libras_a_kilogramos(valor)
            print(f"{valor} lb = {resultado:.2f} kg")
        else:
            print("Opción inválida")
    except ValueError:
        print("Por favor ingresa un número válido")

def main():
    while True:
        print("\n=== Conversor de Unidades ===")
        print("1. Temperatura")
        print("2. Longitud")
        print("3. Peso")
        print("4. Salir")
        
        opcion = input("Selecciona el tipo de conversión: ")
        
        if opcion == "1":
            menu_temperatura()
        elif opcion == "2":
            menu_longitud()
        elif opcion == "3":
            menu_peso()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
```

**Explicación**: Organiza el código en funciones específicas para cada tipo de conversión. Muestra cómo estructurar programas más grandes.

---

## Ejercicio 8: Generador de Contraseñas

```python
# Solución
import random
import string

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_minusculas=True, 
                      incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        return "Error: Debes incluir al menos un tipo de carácter"
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("=== Generador de Contraseñas ===")
    
    try:
        longitud = int(input("Longitud de la contraseña: "))
        if longitud < 1:
            print("La longitud debe ser mayor a 0")
            return
        
        print("\nOpciones (s/n):")
        mayusculas = input("Incluir mayúsculas? ").lower() == 's'
        minusculas = input("Incluir minúsculas? ").lower() == 's'
        numeros = input("Incluir números? ").lower() == 's'
        simbolos = input("Incluir símbolos? ").lower() == 's'
        
        cantidad = int(input("\n¿Cuántas contraseñas generar? "))
        
        print("\n=== Contraseñas Generadas ===")
        for i in range(cantidad):
            contraseña = generar_contraseña(longitud, mayusculas, minusculas, numeros, simbolos)
            print(f"{i+1}. {contraseña}")
            
    except ValueError:
        print("Por favor ingresa números válidos")

if __name__ == "__main__":
    main()
```

**Explicación**: Usa el módulo `string` para obtener diferentes tipos de caracteres y `random.choice()` para seleccionar aleatoriamente. Muestra generación de datos aleatorios.
