import heapq
import time
class Tareas:
    def __init__(self):
        self.heap = []  # Usaremos una lista para implementar el heap
        self.contador = 0  # Para diferenciar tareas con igual prioridad

    def agregar_tarea(self, nombre, prioridad):
        heapq.heappush(self.heap, (prioridad, self.contador, nombre))
        self.contador += 1
        print(f"Tarea '{nombre}' con prioridad {prioridad} añadida.")
    def mostrar_tareas(self):
        if not self.heap:
            print("No hay tareas pendientes.")
        else:
            print("Tareas en orden de prioridad:")
            for prioridad, nombre in sorted(self.heap):
                print(f"  - {nombre} (Prioridad: {prioridad})")

    def eliminar_tarea_completa(self, nombre):
        nueva_lista = [tarea for tarea in self.heap if tarea[2] != nombre]
        if len(nueva_lista) == len(self.heap):
            print(f"No se encontró la tarea '{nombre}'.")
        else:
            self.heap = nueva_lista
            heapq.heapify(self.heap)
            print(f"Tarea '{nombre}' eliminada.")

    def mayor_prioridad(self):
        if not self.heap:
            print("No hay tarea prioritaria")
        else:
            tarea_imp=self.heap[0]
            print("la tarea mas importante es",tarea_imp)
    def verificar_orden_completadas(self):
        # Filtramos solo las tareas completadas
        completadas = [tarea for tarea in self.tareas if tarea["completada"]]

        # Ordenamos por prioridad para verificar el orden de completado
        completadas_por_prioridad = sorted(completadas, key=lambda x: x["prioridad"])

        # Comprobamos si las tareas completadas están en orden de prioridad ascendente
        for i, tarea in enumerate(completadas):
            if tarea != completadas_por_prioridad[i]:
                print("Error: Las tareas no se completaron en orden de prioridad.")
                return False
        print("Todas las tareas completadas están en el orden correcto de prioridad.")
        return True
# Programa principal
if __name__ == "__main__":
    tareas = Tareas()

    while True:
        print("\nGestor de Tareas:")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea completa")
        print("4. mayor prioridad")
        print("5. verificar_orden_completadas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la tarea: ")
            try:
                prioridad = int(input("Ingrese la prioridad de la tarea (número, menor = más urgente): "))
                tareas.agregar_tarea(nombre, prioridad)
                time.sleep(2)
            except ValueError:
                print("Por favor, ingrese un número válido para la prioridad.")
                time.sleep(2)
        elif opcion == "2":
            tareas.mostrar_tareas()
            time.sleep(2)
        elif opcion == "3":
            nombre = input("Ingrese el nombre de la tarea a eliminar: ")
            tareas.eliminar_tarea_completa(nombre)
            time.sleep(2)
        elif opcion == "4":
            tareas.mayor_prioridad()
        elif opcion=="5":
            tareas.verificar_orden_completadas()
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            time.sleep(2)
