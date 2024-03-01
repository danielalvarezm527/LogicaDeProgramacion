class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_attr(self, nombre="", edad="", dni=""):
        if nombre != "":
            self.nombre = nombre

        if edad != "":
            self.edad = edad

        if dni != "":
            self.dni = dni

    def get_m_attr(self, nombre=False, edad=False, dni=False):
        if nombre == True:
            return self.nombre

        if edad == True:
            return self.edad

        if dni == True:
            return self.dni

        return ""

    def mostrar(self):
       print(f"Mi nombre es {self.nombre}, tengo {self.edad} años y mi dni es {self.dni}")

    def mayorDeEdad(self):
       if self.edad >= 18:
           print(f"{self.nombre} es mayor de edad {True}")
       else:
           print(f"{self.nombre} no es mayor de edad {False}")
            
daniel = Persona("Daniel", 26, "1037656417")
daniel.mostrar()
daniel.mayorDeEdad()

print(f"Utilizando getter para el nombre: {daniel.get_m_attr(True, False, False)}")
