"""
1. Gestión de tareas: Implementa un programa que permita a los usuarios gestionar sus tareas diarias. 
Crea clases como Tarea, ListaTareas y Usuario. La clase Tarea debe contener información sobre la descripción y estado de la tarea. 
La clase ListaTareas debe permitir a los usuarios agregar, eliminar y marcar tareas como completadas. 
La clase Usuario debe gestionar las listas de tareas para cada usuario.
"""

'''
class ListaTareas():
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

'''
class Vuelo():
    def __init__(self, vuelos = []):
        self.vuelos = vuelos

    def imprimirVuelos(self):
        num = 0
        for v in self.vuelos:
            print(f"{num}:{v}")
            num = num + 1
        print("\n")

class Reserva(Vuelo):
    def __init__(self, reservas = []):
        self.reservas = reservas

    def agregarReserva(self, nombre, nombre_vuelo, documento):
        self.reservas.append({"Nombre": nombre, "Documento": documento, "Vuelo": nombre_vuelo})

    def imprimirReservas(self):
        for r in self.reservas:
            print(r)

class Pasajero(Reserva):
    def __init__(self, nombre, documento):
        super().__init__()
        self.nombre = nombre
        self.documento = documento

    def reservar(self, n_vuelo):
        super().agregarReserva(self.nombre, n_vuelo, self.documento)

vuelos_disponibles = Vuelo(["Cancun", "Londres", "Madrid", "Berlin"])
daniel = Pasajero("Daniel Alvarez", "1037656417")

seleccion = 1
while seleccion != 4:
    seleccion = int(input("Selecciona una opcion\n1.Reservar\n2.Ver vuelos\n3.Ver reservas\n4.Salir\n"))

    if seleccion > 0 and seleccion < 4:
        if seleccion == 1:
            vuelos_disponibles.imprimirVuelos()
            seleccion_vuelo = int(input("Selecciona el numero del vuelo: "))
            if seleccion_vuelo < 0 or seleccion_vuelo > len(vuelos_disponibles.vuelos):
                print("Numero no valido")
            else:
                daniel.reservar(vuelos_disponibles.vuelos[seleccion_vuelo])

        elif seleccion == 2:
            vuelos_disponibles.imprimirVuelos()

        elif seleccion == 3:
            daniel.imprimirReservas()
'''

"""
3. Simulación de un juego de rol: Diseña un juego de rol simple utilizando clases y objetos. 
Crea clases como Jugador, Enemigo y Arma. La clase Jugador debe tener atributos como puntos de vida y un inventario de armas. 
La clase Enemigo debe representar a los oponentes del jugador. Implementa métodos para que el jugador pueda atacar a los enemigos y viceversa.
"""

class Arma():
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

class Jugador():
    def __init__(self, nombre, vida):
        self.inventario = []
        self.nombre = nombre
        self.vida = vida

    def recoger_arma(self, nombre, daño):
        nueva_arma = Arma(nombre, daño)
        self.inventario.append({"Nombre":nueva_arma.nombre, "Daño":int(nueva_arma.daño)})

    def ver_inventario(self):
        num = 0
        for i in self.inventario:
            print(f"{num}:{i}")
            num = num + 1
        print("\n")

    def desenfundar_arma(self, n_arma):
        self.arma_seleccionada = n_arma
        print(f"Arma seleccionada: {self.inventario[n_arma]}")

    def daño(self, enemigo):
        print(f"{enemigo.nombre} ataca a {self.nombre} con", enemigo.inventario[0]["Nombre"])
        self.vida = self.vida - enemigo.inventario[0]["Daño"]
        print(f"Vida restante de {self.nombre}: {self.vida}")

class Enemigo():
    def __init__(self, nombre, vida):
        self.inventario = []
        self.inventario.append({"Nombre":"Puño", "Daño":3})
        self.nombre = nombre
        self.vida = vida

    def daño(self, jugador):
        print(f"{jugador.nombre} ataca a {self.nombre} con",jugador.inventario[jugador.arma_seleccionada]["Nombre"])
        self.vida = self.vida - jugador.inventario[jugador.arma_seleccionada]["Daño"]
        print(f"Vida restante de {self.nombre}: {self.vida}")

enemigo_uno = Enemigo("Goblin", 50)
jugador_uno = Jugador("Daniel", 100)

jugador_uno.recoger_arma("Espada", 10)
jugador_uno.recoger_arma("Arco", 8)
jugador_uno.ver_inventario()
jugador_uno.desenfundar_arma(0)

enemigo_uno.daño(jugador_uno)
jugador_uno.daño(enemigo_uno)