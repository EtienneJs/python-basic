"""
Strings (Cadenas de Texto) en Python

Este archivo muestra cómo trabajar con strings en Python.
"""

# ===== CREAR STRINGS =====
print("=== Creación de Strings ===")
nombre = "Juan"
mensaje = 'Hola mundo'
mensaje_largo = """Este es un
mensaje multilínea
que puede abarcar varias líneas"""

print(f"Nombre: {nombre}")
print(f"Mensaje: {mensaje}")
print(f"Mensaje largo:\n{mensaje_largo}")

print("\n" + "="*50 + "\n")

# ===== OPERACIONES CON STRINGS =====
print("=== Operaciones con Strings ===")
texto1 = "Hola"
texto2 = "Mundo"

# Concatenación
texto_completo = texto1 + " " + texto2
print(f"Concatenación: {texto_completo}")

# Repetición
repeticion = texto1 * 3
print(f"Repetición ('Hola' * 3): {repeticion}")

# Longitud
print(f"Longitud de '{texto_completo}': {len(texto_completo)}")

print("\n" + "="*50 + "\n")

# ===== ACCESO A CARACTERES =====
print("=== Acceso a Caracteres ===")
palabra = "Python"
print(f"Palabra: {palabra}")
print(f"Primer carácter: {palabra[0]}")      # P
print(f"Último carácter: {palabra[-1]}")     # n
print(f"Subcadena [0:2]: {palabra[0:2]}")    # Py
print(f"Subcadena [2:]: {palabra[2:]}")      # thon

print("\n" + "="*50 + "\n")

# ===== MÉTODOS COMUNES DE STRINGS =====
print("=== Métodos Comunes ===")
texto = "  Hola Mundo  "

print(f"Original: '{texto}'")
print(f"upper(): {texto.upper()}")              # Convierte a mayúsculas
print(f"lower(): {texto.lower()}")              # Convierte a minúsculas
print(f"strip(): '{texto.strip()}'")            # Elimina espacios al inicio y final
print(f"replace('Mundo', 'Python'): {texto.strip().replace('Mundo', 'Python')}")
print(f"split(): {texto.strip().split()}")      # Divide en lista

# Verificar contenido
otro_texto = "Python es genial"
print(f"\nTexto: '{otro_texto}'")
print(f"startswith('Python'): {otro_texto.startswith('Python')}")
print(f"endswith('genial'): {otro_texto.endswith('genial')}")
print(f"'es' in texto: {'es' in otro_texto}")

print("\n" + "="*50 + "\n")

# ===== F-STRINGS (FORMATO MODERNO) =====
print("=== F-strings ===")
nombre = "María"
edad = 25
altura = 1.65

# Formato básico
mensaje = f"Mi nombre es {nombre} y tengo {edad} años"
print(mensaje)

# Formato con decimales
mensaje_altura = f"Mi altura es {altura:.2f} metros"
print(mensaje_altura)

# Formato con expresiones
calculo = f"5 + 3 = {5 + 3}"
print(calculo)

