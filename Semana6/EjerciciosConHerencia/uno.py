#Clases: Universidad carrera estudiante
#Universidad: NIT, nombres, direccion, representante legal
#Carrera: carreras que dependen de la U
#Estudiantes: se pueden inscribir a la carrera de la universidad 
#Mostrar las carreras a las que esta suscrito el estudiante
class Estudiante:
    def __init__(self, nombre_estudiante):
        self.nombre_estudiante = nombre_estudiante

class Carrera(Estudiante):
    def __init__(self, nombre_carrera, nombre_estudiante):
        self.nombre_carrera = nombre_carrera
        super().__init__(nombre_estudiante)

class Universidad(Carrera):
    def __init__(self, nombre_universidad, direccion, representante, nit):
        self.nombre_universidad = nombre_universidad
        self.direccion = direccion
        self.representante = representante
        self.nit = nit

    def inscripcion(self, nombre_carrera, nombre_estudiante):
        super().__init__(nombre_carrera, nombre_estudiante)

    def certificado(self):
        print(f"\nElestudiante {self.nombre_estudiante}, esta inscrito en la carrera {self.nombre_carrera}, en la universidad {self.nombre_universidad}\n")

mi_universidad = Universidad("Tecnologico de antioquia", "CL 78B #72 A-220", "Leonardo García Botero", "890.905.419")
mi_universidad.inscripcion("Ingenieria de software", "Daniel Alvarez Moncada")
mi_universidad.certificado()