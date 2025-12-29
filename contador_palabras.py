"""
Contador de Palabras

Ejemplo práctico que cuenta palabras, caracteres y palabras únicas en un texto.
"""

def contar_palabras(texto):
    """
    Cuenta el número total de palabras en un texto.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: Número de palabras
    """
    palabras = texto.split()
    return len(palabras)

def contar_caracteres(texto):
    """
    Cuenta el número total de caracteres en un texto.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: Número de caracteres
    """
    return len(texto)

def contar_caracteres_sin_espacios(texto):
    """
    Cuenta el número de caracteres sin espacios.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: Número de caracteres sin espacios
    """
    texto_sin_espacios = texto.replace(" ", "")
    return len(texto_sin_espacios)

def contar_palabras_unicas(texto):
    """
    Cuenta el número de palabras únicas en un texto.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: Número de palabras únicas
    """
    palabras = texto.lower().split()
    return len(set(palabras))

def analizar_texto(texto):
    """
    Realiza un análisis completo del texto.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        dict: Diccionario con las estadísticas
    """
    palabras = texto.split()
    palabras_unicas = set(palabra.lower() for palabra in palabras)
    
    estadisticas = {
        "total_palabras": len(palabras),
        "palabras_unicas": len(palabras_unicas),
        "total_caracteres": len(texto),
        "caracteres_sin_espacios": len(texto.replace(" ", "")),
        "promedio_letras_por_palabra": sum(len(p) for p in palabras) / len(palabras) if palabras else 0
    }
    
    return estadisticas

# Ejemplo de uso
if __name__ == "__main__":
    print("=== Contador de Palabras ===\n")
    
    # Texto de ejemplo
    texto = "Python es genial Python es fácil Python es poderoso"
    
    print(f"Texto analizado: '{texto}'\n")
    print("="*50)
    
    # Funciones individuales
    print(f"Total de palabras: {contar_palabras(texto)}")
    print(f"Total de caracteres: {contar_caracteres(texto)}")
    print(f"Caracteres sin espacios: {contar_caracteres_sin_espacios(texto)}")
    print(f"Palabras únicas: {contar_palabras_unicas(texto)}")
    
    print("\n" + "="*50)
    
    # Análisis completo
    print("\n📊 Análisis Completo:")
    estadisticas = analizar_texto(texto)
    
    for clave, valor in estadisticas.items():
        if isinstance(valor, float):
            print(f"  {clave.replace('_', ' ').title()}: {valor:.2f}")
        else:
            print(f"  {clave.replace('_', ' ').title()}: {valor}")
    
    # Ejemplo interactivo (descomenta para usar)
    """
    print("\n" + "="*50)
    print("Modo Interactivo")
    print("="*50)
    texto_usuario = input("\nIngresa un texto para analizar: ")
    
    if texto_usuario.strip():
        estadisticas = analizar_texto(texto_usuario)
        print("\n📊 Estadísticas:")
        for clave, valor in estadisticas.items():
            if isinstance(valor, float):
                print(f"  {clave.replace('_', ' ').title()}: {valor:.2f}")
            else:
                print(f"  {clave.replace('_', ' ').title()}: {valor}")
    else:
        print("No se ingresó texto válido")
    """

