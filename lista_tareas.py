"""
Lista de Tareas (To-Do List)

Ejemplo práctico de una aplicación de lista de tareas usando listas y funciones.
"""

# Lista global para almacenar las tareas
tareas = []

def agregar_tarea(tarea):
    """Agrega una nueva tarea a la lista"""
    tareas.append(tarea)
    print(f"✓ Tarea '{tarea}' agregada")

def ver_tareas():
    """Muestra todas las tareas pendientes"""
    if tareas:
        print("\n📋 Lista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"  {i}. {tarea}")
    else:
        print("\n✓ No hay tareas pendientes")

def eliminar_tarea(numero):
    """Elimina una tarea por su número"""
    if 1 <= numero <= len(tareas):
        tarea_eliminada = tareas.pop(numero - 1)
        print(f"✓ Tarea '{tarea_eliminada}' eliminada")
    else:
        print(f"✗ Número de tarea inválido. Debe estar entre 1 y {len(tareas)}")

def marcar_completada(numero):
    """Marca una tarea como completada (la elimina de la lista)"""
    if 1 <= numero <= len(tareas):
        tarea_completada = tareas.pop(numero - 1)
        print(f"✓ Tarea '{tarea_completada}' marcada como completada")
    else:
        print(f"✗ Número de tarea inválido")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*40)
    print("MENÚ DE TAREAS")
    print("="*40)
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Marcar como completada")
    print("5. Salir")
    print("="*40)

# Ejemplo de uso
if __name__ == "__main__":
    print("=== Lista de Tareas ===\n")
    
    # Ejemplos básicos
    agregar_tarea("Estudiar Python")
    agregar_tarea("Hacer ejercicio")
    agregar_tarea("Comprar comida")
    
    ver_tareas()
    
    print("\n" + "-"*40)
    eliminar_tarea(1)
    
    ver_tareas()
    
    print("\n" + "-"*40)
    marcar_completada(1)
    
    ver_tareas()
    
    # Versión interactiva (descomenta para usar)
    """
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            tarea = input("Ingresa la tarea: ")
            agregar_tarea(tarea)
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            ver_tareas()
            if tareas:
                num = int(input("Número de tarea a eliminar: "))
                eliminar_tarea(num)
        elif opcion == "4":
            ver_tareas()
            if tareas:
                num = int(input("Número de tarea completada: "))
                marcar_completada(num)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")
    """

