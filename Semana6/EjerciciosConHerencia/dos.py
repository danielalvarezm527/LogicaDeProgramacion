#Clases: Universidad carrera estudiante
#Universidad: NIT, nombres, direccion, representante legal
#Carrera: carreras que dependen de la U
#Estudiantes: se pueden inscribir a la carrera de la universidad 
#Mostrar las carreras a las que esta suscrito el estudiante

#Reestructurar el modelo estudiante, se va a llamar usuario, agregar una nueva clase userRol, diferenciar si es un docente o un estudiante, agregar clase notas de la asignatura
#nombre profe - nombre materia - nombre estudiantes - agregar notas - buscar notas

class Estudiante:
    def __init__(self, nombre_estudiante):
        self.nombre_estudiante = nombre_estudiante

class Carrera(Estudiante):
    def __init__(self):
        pass
        
    def setCarreras(self, carreras):
        self.carreras = carreras

    def inscribir(self, numero_carrera, nombre_estudiante):
        self.numero_carrera = int(numero_carrera)
        super().__init__(nombre_estudiante)

class Universidad(Carrera):
    def __init__(self, nombre_universidad, direccion, representante, nit):
        self.nombre_universidad = nombre_universidad
        self.direccion = direccion
        self.representante = representante
        self.nit = nit

    def crearCarreras(self, nombres_carreras):
        super().setCarreras(nombres_carreras)

    def inscribirEstudiante(self):
        print("Selecciona una carrera.")
        num = 0
        for x in self.carreras:
            num = num + 1
            print(f"{num}. {x}")
        num = num + 1
        print(f"{num}. Salir")

        valor = int(input("Ingresa el numero de la carrera: "))
        while valor > num or valor <= 0:
            self.inscribirEstudiante()

        if valor == num:
            return
        else:
            nombre_del_estudiante = input("Ingresa el nombre del estudiante: ")
            super().inscribir(valor-1, nombre_del_estudiante)
            self.certificado()

    def certificado(self):
        print(f"\nEl o la estudiante {self.nombre_estudiante}, esta inscrito en la carrera {self.carreras[self.numero_carrera]}, en la universidad {self.nombre_universidad}\n")

mi_universidad = Universidad("Tecnologico de antioquia", "CL 78B #72 A-220", "Leonardo García Botero", "890.905.419")
mi_universidad.crearCarreras(["Ingenieria de software", "Ingenieria electronica", "Ingenieria electrica", "Gastronomia", "Artes"])

mi_universidad.inscribirEstudiante()