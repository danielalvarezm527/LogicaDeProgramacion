"""
1. Gestión de tareas: Implementa un programa que permita a los usuarios gestionar sus tareas diarias. 
Crea clases como Tarea, ListaTareas y Usuario. La clase Tarea debe contener información sobre la descripción y estado de la tarea. 
La clase ListaTareas debe permitir a los usuarios agregar, eliminar y marcar tareas como completadas. 
La clase Usuario debe gestionar las listas de tareas para cada usuario.
"""

'''class ListaTareas():
    def __init__(self, lista_de_tareas=[]):
        self.lista_tareas = lista_de_tareas

    def agregarTarea(self, descripcion, estado):
        mi_tarea = {"Descripcion":descripcion, "Estado":estado}
        self.lista_tareas.append(mi_tarea)

    def eliminarTarea(self, indice_tarea):
        self.lista_tareas.pop(indice_tarea)

    def completarTarea(self, indice_tarea):
        self.lista_tareas[indice_tarea].update({'Estado': True})

    def imprimirTareas(self):
        num = 0
        for k in self.lista_tareas:
            print(f"{num}:{k}")
            num = num + 1

class Tarea(ListaTareas):
    def __init__(self, tareas):
        super().__init__()
        for i in tareas:
            super().agregarTarea(i[0], i[1])

class Usuario(Tarea):
    def __init__(self):
        pass

    def crearTareas(self, lista_de_tareas):
        super().__init__(lista_de_tareas)

daniel = Usuario()
seleccion = 1

while seleccion != 5:
    mis_tareas = []
    seleccion = int(input("Selecciona una opcion\n1.Agregar tarea\n2.Eliminar tarea\n3.Completar tarea\n4.Imprimir tareas\n5.Salir\n"))

    if seleccion > 0 and seleccion < 5:
        if seleccion == 1:
            descripcion_tarea = input("Ingresa la descripcion de la tarea: ")
            mis_tareas.append([descripcion_tarea, False])
            daniel.crearTareas(mis_tareas)
        elif seleccion == 2:
            daniel.imprimirTareas()
            tarea_a_eliminar = int(input("\nEscoge el numero de la tarea que deseas eliminar: "))
            if tarea_a_eliminar < 0 or tarea_a_eliminar > len(daniel.lista_tareas):
                print("Numero no valido")
            else:
                daniel.eliminarTarea(tarea_a_eliminar)
        elif seleccion == 3:
            daniel.imprimirTareas()
            tarea_a_completar = int(input("\nEscoge el numero de la tarea que deseas completar: "))
            if tarea_a_completar < 0 or tarea_a_completar > len(daniel.lista_tareas):
                print("Numero no valido")
            else:
                daniel.completarTarea(tarea_a_completar)
        elif seleccion == 4:
            daniel.imprimirTareas()
'''


"""
2. Simulación de un sistema de reservas de vuelos: Diseña un programa que simule un sistema de reservas de vuelos. 
Crea clases como Vuelo, Pasajero y Reserva. La clase Vuelo debe contener información sobre el número de vuelo, aeropuerto de origen y destino, y capacidad. 
La clase Pasajero debe representar a los pasajeros que desean reservar un vuelo. La clase Reserva debe gestionar las reservas de los pasajeros para los vuelos disponibles.
"""

class Vuelo():
    def __init__(self):
        pass

class Reserva(Vuelo):
    def __init__(self):
        pass

class Pasajero(Reserva):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento


daniel = Pasajero("Daniel Alvarez", "1037656417")

    