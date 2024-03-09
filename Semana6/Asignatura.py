from Alumno import Alumno

class Asignatura(Alumno):
    def __init__(self, nombre_asignatura, nombre, apellido, edad):
        self.nombre_asignatura = nombre_asignatura
        super().__init__(nombre, apellido, edad)

    def mostrar(self):
        print(f"El nombre de la asignatura es {self.nombre_asignatura} y el nombre de mi estudiante es {self.nombre}, con apellido {self.apellido} y edad {self.edad}")
        
mi_asignatura = Asignatura("Logica","Daniel","Alvarez",26)
mi_asignatura.mostrar()