class Calculadora:
    def __init__(self):
        pass

    def leer(self, n1, n2, operacion):
        if operacion == 1:
            resultado = self.sumar(n1, n2)
            return resultado
        elif operacion == 2:
            resultado = self.resta(n1, n2)
            return resultado
        elif operacion == 3:
            resultado = self.multiplicar(n1, n2)
            return resultado
        elif operacion == 4:
            resultado = self.dividir(n1, n2)
            return resultado

    def sumar(self, n1:float, n2:float):
        return n1 + n2
    
    def resta(self, n1:float, n2:float):
        return n1 - n2
    
    def multiplicar(self, n1:float, n2:float):
        return n1 * n2
    
    def dividir(self, n1:float, n2:float):
        if n2 != 0:
            return n1 / n2
        else:
            return "No es posible dividir por cero"
        
mi_calculadora = Calculadora()

seleccion = 1

while seleccion != 5:
    seleccion = int(input("Selecciona una opcion\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n"))

    if seleccion > 0 and seleccion < 5:
        numero_uno = float(input("Ingresa el primer numero: "))
        numero_dos = float(input("Ingresa el segundo numero: "))
        resultado = mi_calculadora.leer(numero_uno,numero_dos,seleccion)
        print(f"El resultado es: ",resultado,"\n")