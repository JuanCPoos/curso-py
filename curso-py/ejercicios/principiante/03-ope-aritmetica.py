import math

val1 = int(input("primer valor: "))
val2 = int(input("segundo valor: "))


def sumar(a, b):
    resultado = a + b
    return resultado


def multiplicar(b):
    resultado = b * 5
    return resultado


print(((3+2)/(2*5))**2)
resulDiv = math.pow((sumar(val1, val2) / multiplicar(val2)), 2)
print(resulDiv)
