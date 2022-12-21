"""Se crea una clase que llama a otras para realizar operaciones"""
def suma(x, y):     #Funcion para sumar 2 numeros
    return x + y

def resta(x, y):    #Funcion para restar 2 numeros
    return x - y

def multiplica(x, y):   #Funcion para multiplicar 2 numeros
    return x*y

def divide(x, y):       #Funcion para dividir 2 numeros
    return x/y

class Operaciones:
    def __init__(self, Numero1, Numero2, Operador):

        if Operador == 'suma':
            self.Operador = suma(Numero1, Numero2)
        elif Operador == 'resta':
            self.Operador = resta(Numero1, Numero2)
        elif Operador == 'multiplicacion':
            self.Operador = multiplica(Numero1, Numero2)
        elif Operador == 'division':
            self.Operador = divide(Numero1, Numero2)

""" Programa principal del codigo """
numero1 = float(input("Teclee el primer numero: "))
numero2 = float(input("Teclee el segundo numero: "))
operacion = input("Teclee la operacion a realizar: ")

t = Operaciones(numero1, numero2, operacion)
print("El resultado es: ", t.Operador)
