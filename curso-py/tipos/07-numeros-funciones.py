import math

print(round(1.3))  # devuelve el n° más cercado al valor
print(round(1.7))
print(round(1.5))

print(abs(-77))
print(abs(55))

# - todas estos métodos pertenecen al módulo math
# - la función ceil() devuelve el valor más cercano entero hacía arriba del argumento de ceil()
print(math.ceil(1.1))
# - la función floor() devuelve el valor más cercano entero hacía arriba del argumento de ceil()
print(math.floor(1.9999999))
# - metodo isnan() devuelve true si el argumento no es un n° "is not a number"
print(math.isnan(23))
# print(math.isnan(23))

print(math.pow(10, 3))  # - potencia
print(math.sqrt(9))  # - raíz cuadrada
