class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años y mi dni es {self.dni}")

    def mayorDeEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} no es mayor de edad")
            
daniel = Persona("Daniel", 26, "1037656417")

daniel.mostrar()
daniel.mayorDeEdad()