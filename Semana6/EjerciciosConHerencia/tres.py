class UserRole:
    def __init__(self):
        self.roles = ["Profesor", "Alumno"]

class User(UserRole):
    def __init__(self, users):
        self.estudiantes = []
        super().__init__()
        for user in users:
            if user["role"] == 0:
                self.profesor = user["name"]
            else:
                self.estudiantes.append(user["name"])

    def imprimir(self):
        print(f"Profesor:\n{self.profesor}\n")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(estudiante)

class notas(User):
    def __init__(self, users):
        super().__init__(users)
        pass

    def setNotas(self):
        self.notas = []
        for estudiante in self.estudiantes:
            self.nota = {}
            nota_estudiante = float(input(f"Ingrese la nota para el o la estudiante {estudiante}: "))
            self.nota.update({"Nombre":estudiante})
            self.nota.update({"Nota":nota_estudiante})
            self.notas.append(self.nota)

    def imprimirNotas(self):
        print("\n")
        num = 0
        for estudiante in self.estudiantes:
            num = num + 1
            print(f"{num}. {estudiante}")
        num = num + 1
        print(f"{num}. Salir")
        print("\n")

        valor = int(input("Ingresa el numero del estudiante: "))
        while valor > num or valor <= 0:
            self.imprimirNotas()

        if valor == num:
            return
        else:
            for nota in self.notas:
                if nota["Nombre"] == self.estudiantes[valor-1]:
                    print("La nota del estudiante es:",nota["Nota"])



list = [{"name":"Daniel","role":1},{"name":"santiago","role":1},{"name":"Jeison","role":0},{"name":"Laura","role":1},{"name":"Camila","role":1},{"name":"Carlos","role":1}]
usuario = notas(list)
usuario.setNotas()
usuario.imprimirNotas()