class Cuenta:
    def __init__(self, titular:str, cantidad:float=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"El titular de la cuenta es {self.titular} y tiene {self.cantidad}")

    def ingresar(self, ingreso:float):
        self.cantidad += ingreso

    def retirar(self, egreso:float):
        self.cantidad -= egreso

mi_cuenta = Cuenta("Daniel Alvarez",1000)

mi_cuenta.mostrar()
mi_cuenta.ingresar(1000)
mi_cuenta.mostrar()
mi_cuenta.retirar(500.7)
mi_cuenta.mostrar()
