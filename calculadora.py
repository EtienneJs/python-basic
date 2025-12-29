"""
Calculadora Simple

Ejemplo práctico de una calculadora básica usando funciones y condicionales.
"""

def calculadora():
    """
    Calculadora simple que realiza operaciones básicas.
    
    Solicita dos números y una operación al usuario,
    y devuelve el resultado.
    """
    try:
        num1 = float(input("Ingresa el primer número: "))
        operacion = input("Ingresa la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                return "Error: No se puede dividir por cero"
        else:
            return "Error: Operación no válida"
        
        return f"Resultado: {resultado}"
    
    except ValueError:
        return "Error: Por favor ingresa números válidos"

# Ejecutar calculadora
if __name__ == "__main__":
    print("=== Calculadora Simple ===\n")
    resultado = calculadora()
    print(resultado)

