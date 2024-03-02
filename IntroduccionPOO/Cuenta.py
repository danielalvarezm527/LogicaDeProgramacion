class Cuenta:
    def __init__(self, titular:str, cantidad:float=0):
        self.__titular = titular
        self.__cantidad = cantidad

    def mostrar(self):
        print(f"El titular de la cuenta es {self.__titular} y tiene {self.__cantidad}")

    def set_cantidad_attr(self, valor:float):
        self.__cantidad = valor

    def get_cantidad_attr(self):
        return self.__cantidad

    def ingresar(self, ingreso:float):
        cantidad = self.__cantidad + ingreso
        self.set_cantidad_attr(cantidad)

    def retirar(self, egreso:float):
        if egreso > 0:
            cantidad = self.__cantidad - egreso
            self.set_cantidad_attr(cantidad)

mi_cuenta = Cuenta("Daniel Alvarez",1000)

mi_cuenta.mostrar()
mi_cuenta.ingresar(1000)
mi_cuenta.mostrar()
mi_cuenta.retirar(500.7)
mi_cuenta.mostrar()

print(f"Cantidad utilizando getters {mi_cuenta.get_cantidad_attr()}")
